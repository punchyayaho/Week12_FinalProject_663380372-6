# final-task-manager-project/src/task_manager.py
import datetime
import logging  # For potential logging, though simple prints are used here
# Configure logging (optional, can be removed or modified)
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from .task import Task, DueDateTask, PriorityTask
from .data_persistence import DataPersistence


class TaskManager:
    """
    Manages the collection of various Task objects.
    Focuses on business logic: add, list, complete, delete, search, filter, sort.
    """
    PRIORITY_MAP = {"High": 1, "Medium": 2, "Low": 3}
    REVERSE_PRIORITY_MAP = {1: "High", 2: "Medium", 3: "Low"}

    def __init__(self, data_file='data/tasks.json'):
        self.persistence = DataPersistence(data_file)
        self.tasks = self.persistence.load_tasks()
        self.next_id = self._get_next_task_id()

    def _get_next_task_id(self):
        """Generates the next unique ID for a new task."""
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def _save_changes(self):
        """Internal helper to save tasks via the persistence layer."""
        self.persistence.save_tasks(self.tasks)

    # --- Basic CRUD Operations ---
    def add_normal_task(self, description, tags=None):
        new_task = Task(self.next_id, description, tags=tags)
        self.tasks.append(new_task)
        self.next_id += 1
        self._save_changes()
        return new_task

    def add_due_date_task(self, description, due_date_str, tags=None):
        try:
            # DueDateTask constructor handles string parsing to datetime object
            new_task = DueDateTask(self.next_id, description, due_date_str, tags=tags)
            self.tasks.append(new_task)
            self.next_id += 1
            self._save_changes()
            return new_task
        except ValueError:
            # This should ideally be caught in CLI layer, but for robustness
            return None

    def add_priority_task(self, description, priority, tags=None):
        try:
            new_task = PriorityTask(self.next_id, description, priority, tags=tags)
            self.tasks.append(new_task)
            self.next_id += 1
            self._save_changes()
            return new_task
        except ValueError:
            return None

    def get_task_by_id(self, task_id):
        """Helper to find a task by ID."""
        return next((task for task in self.tasks if task.id == task_id), None)

    def complete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            if not task.completed:
                task.mark_complete()
                self._save_changes()
                return True, "Task marked as completed."
            else:
                return False, "Task is already completed."
        return False, "Task not found."

    def delete_task(self, task_id):
        original_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) < original_len:
            self._save_changes()
            return True, "Task deleted successfully."
        return False, "Task not found."

    # --- New/Enhanced Features ---
    def get_all_tasks(self):
        """Returns all tasks. Useful for listing."""
        return list(self.tasks)

    def search_tasks(self, keyword):
        """
        Searches tasks by keyword in description or tags (case-insensitive).
        """
        if not keyword:
            return []  # No keyword, no results
        keyword_lower = keyword.lower()
        found_tasks = []
        for task in self.tasks:
            # Search in description
            if keyword_lower in task.description.lower():
                found_tasks.append(task)
                continue  # Found in description, no need to check tags
            # Search in tags
            if any(keyword_lower in tag.lower() for tag in task.tags):
                found_tasks.append(task)
        return found_tasks

    def filter_tasks(self, status=None, due_date_before=None, due_date_after=None, priority_level=None, contains_tags=None):
        """
        Filters tasks by various criteria.
        Args:
            status (bool, optional): True for completed, False for pending.
            due_date_before (datetime.date, optional): Tasks due on or before this date.
            due_date_after (datetime.date, optional): Tasks due on or after this date.
            priority_level (str, optional): "High", "Medium", "Low".
            contains_tags (list, optional): List of tags, task must have ALL of these tags.
        """
        filtered_tasks = self.tasks
        # Filter by completion status
        if status is not None:
            filtered_tasks = [t for t in filtered_tasks if t.completed == status]
        # Filter by due date before (only DueDateTask)
        if due_date_before:
            filtered_tasks = [t for t in filtered_tasks
                              if isinstance(t, DueDateTask) and t.due_date <= due_date_before]
        # Filter by due date after (only DueDateTask)
        if due_date_after:
            filtered_tasks = [t for t in filtered_tasks
                              if isinstance(t, DueDateTask) and t.due_date >= due_date_after]
        # Filter by priority level (only PriorityTask)
        if priority_level:
            filtered_tasks = [t for t in filtered_tasks
                              if isinstance(t, PriorityTask) and t.priority == priority_level]
        # Filter by tags (task must contain ALL specified tags)
        if contains_tags:
            contains_tags_lower = [tag.lower() for tag in contains_tags]
            filtered_tasks = [t for t in filtered_tasks
                              if all(ctag in [t_tag.lower() for t_tag in t.tags] for ctag in contains_tags_lower)]
        return filtered_tasks

    def sort_tasks(self, criterion="id", reverse=False):
        """
        Sorts tasks by a given criterion.
        Args:
            criterion (str): "id", "due_date", "priority", "description", "completed".
            reverse (bool): True for descending order.
        """
        # Create a mutable copy of the list for sorting
        tasks_to_sort = list(self.tasks)
        if criterion == "id":
            tasks_to_sort.sort(key=lambda t: t.id, reverse=reverse)
        elif criterion == "description":
            tasks_to_sort.sort(key=lambda t: t.description.lower(), reverse=reverse)
        elif criterion == "completed":
            # Sort by completed status (False first, then True)
            tasks_to_sort.sort(key=lambda t: t.completed, reverse=reverse)
        elif criterion == "due_date":
            # Sort DueDateTasks by date, others (Normal/Priority) go to the end/beginning
            tasks_to_sort.sort(
                key=lambda t: (t.due_date if isinstance(t, DueDateTask) else datetime.date.max, t.id),
                reverse=reverse
            )
        elif criterion == "priority":
            # Sort PriorityTasks by mapped numerical priority, others go to the end/beginning
            tasks_to_sort.sort(
                key=lambda t: (self.PRIORITY_MAP.get(t.priority, 99) if isinstance(t, PriorityTask) else 99, t.id),
                reverse=reverse
            )
        else:
            # Fallback to ID sorting if criterion is unknown
            tasks_to_sort.sort(key=lambda t: t.id, reverse=reverse)
        return tasks_to_sort
