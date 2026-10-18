# Final Project: Enhanced Task Manager CLI
This project is a complete command-line interface (CLI) application for managing tasks,
showcasing the application of various software development principles learned throughout the course.
It leverages Object-Oriented Programming (OOP), modular design, data persistence, and advanced data manipulation techniques.
## Implemented Features
* **Task Types**: Supports standard tasks, tasks with a `due_date` (`DueDateTask`), and tasks with a `priority` (`PriorityTask`).
* **Tags**: Assign multiple customizable tags to any task for better organization.
* **Comprehensive CRUD Operations**:
* **Add Tasks**: Create normal, due date, or priority tasks with descriptions and optional tags.
* **List Tasks**: View all tasks, with detailed information including tags, due dates, and priorities.
* **Complete Tasks**: Mark tasks as completed by their ID.
* **Delete Tasks**: Remove tasks by their ID.
* **Advanced Search**: Find tasks by keywords in their description or tags (case-insensitive).
* **Flexible Filtering**: Filter tasks by:
* Completion status (completed/pending).
* Due date range (tasks due before or after a specific date).
* Priority level (High, Medium, Low).
* Specific tag(s) (tasks must contain ALL specified tags).
* **Dynamic Sorting**: Sort tasks by various criteria:
* Task ID (default)
* Description
* Completion Status
* Due Date (for `DueDateTask`s; other tasks are grouped)
* Priority (for `PriorityTask`s; other tasks are grouped)
* **Robust Data Persistence**: All tasks are automatically saved to `data/tasks.json` and loaded on startup, preserving all task details and types.
* **Modular Design**: Application is structured into distinct modules for clear separation of concerns:
* `task.py`: Data models (Task classes).
* `data_persistence.py`: Handles all file I/O.
* `task_manager.py`: Contains core business logic (search, filter, sort).
* `cli_interface.py`: Manages all user interaction.
* `main.py`: The application entry point.
## How to Run
1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/final-task-manager-project.git](https://github.com/YOUR_USERNAME/final-task-manager-project.git)
cd final-task-manager-project
```
2. **Run the application:**
```bash
python main.py
```
## Project Structure
final-task-manager-project/
├── src/
│ ├── init.py # Makes 'src' a Python package
│ ├── task.py # Task models (Task, DueDateTask, PriorityTask with tags)
│ ├── data_persistence.py # Handles JSON file operations
│ ├── task_manager.py # Core task logic (add, delete, complete, search, filter, sort)
│ └── cli_interface.py # Handles user interaction (menu, input/output)
├── data/
│ └── tasks.json # Stores your tasks (created/updated automatically)
├── main.py # Application entry point
├── .gitignore # Specifies files/folders to ignore in Git
├── README.md # This project overview
└── PLAN.md # Project planning, design notes, and reflections
## Extension Ideas (Future Work)
* **Graphical User Interface (GUI)**: Implement a GUI using libraries like `Tkinter`, `PyQt`, or `Kivy` to provide a more visual and interactive experience.
* **Database Integration**: Replace the JSON file persistence with a more robust database system like SQLite, PostgreSQL, or MongoDB.
* **Reminders/Notifications**: Implement a feature to notify the user about upcoming due dates (e.g., pop-up, email, or a simple command-line alert on startup).
* **User Accounts**: Add a basic user authentication system to allow multiple users to manage their own separate task lists.
* **Recurring Tasks**: Allow creation of tasks that repeat daily, weekly, or monthly.
* **Export/Import**: Add functionality to export tasks to CSV, PDF, or import from other formats.
* **Unit Testing**: Develop a comprehensive suite of unit tests for the `task.py` and `task_manager.py` modules to ensure code correctness and prevent regressions.
* **Web Interface**: Explore building a simple web interface using a framework like Flask or Django.
## Contributing
Feel free to fork this repository and build upon this foundation.
## License
This project is open source. (You might add a specific license here later, e.g., MIT)
9. final-task-manager-project/PLAN.md
(This PLAN.md updates the previous one to include notes on what was implemented and any final reflections)
  Markdown
# Project Plan: Enhanced Task Manager CLI (Final Version)
## 1. Introduction
This document served as the blueprint and now reflects the final state of the Enhanced Command-Line Interface (CLI) Task Manager application. It demonstrates the successful application of software development principles, including modular design, OOP, and structured data handling, to create a robust and feature-rich task management tool.
## 2. Requirements (Implemented Features)
### 2.1. Functional Requirements (What the system *does*)
* **Task Management (Core CRUD):**
* **Implemented:** Create, list, complete, delete tasks.
* **Implemented:** Support for `DueDateTask` and `PriorityTask` types.
* **Implemented:** Tasks now include optional `tags` (list of strings).
* **Advanced Task Retrieval:**
* **Implemented:** **Search:** Search tasks by keywords in description or tags (case-insensitive).
* **Implemented:** **Filter:** Filter tasks by completion status, due date range, priority level, and specific tag(s).
* **Implemented:** **Sort:** Sort tasks by ID, description, completed status, due date, and priority (handling tasks without specific attributes).
* **Data Persistence:**
* **Implemented:** Automatic saving of tasks to `data/tasks.json` and loading on startup, correctly preserving all task types and attributes, including tags.
### 2.2. Non-Functional Requirements (How well the system *does it*)
* **Usability:** User-friendly CLI with clear menus, prompts, and informative messages.
* **Reliability:** Robust error handling for invalid user input (e.g., date formats, non-numeric IDs) and file operations.
* **Maintainability:** Codebase is well-structured, commented, and follows modular design principles, making it easier to understand and extend.
* **Extensibility:** The architecture is designed to allow for relatively easy addition of new task types, filtering criteria, or switching persistence mechanisms.
* **Performance:** All operations are performed efficiently for typical usage within a CLI context.
## 3. High-Level Design / Architecture (As Implemented)
The application fully implements the modular, object-oriented design pattern proposed in Week 11:
├── src/
│ ├── task.py # Data Models (Task, DueDateTask, PriorityTask - fully functional with tags)
│ ├── data_persistence.py # Data Storage/Retrieval Layer (JSON load/save)
│ ├── task_manager.py # Business Logic Layer (Full CRUD, Search, Filter, Sort logic)
│ ├── cli_interface.py # User Interface Layer (CLI Input/Output, menu navigation)
│ └── __init__.py # Python package marker
├── data/ # Directory for data files
│ └── tasks.json # Task storage file
├── main.py # Application Entry Point / Orchestrator
├── README.md # Project overview and features
└── PLAN.md # This planning and reflection document
### 3.1. Module Responsibilities (Final Implementation):
* **`task.py` (Models):** Fully implements task classes, `to_dict`, `__str__`, `__repr__`, and tag management.
* **`data_persistence.py` (Data Layer):** Fully implements robust JSON loading and saving, handling object reconstruction and new `tags` attribute.
* **`task_manager.py` (Business Logic Layer):** Fully implements all CRUD operations, and the complex logic for `search_tasks`, `filter_tasks`, and `sort_tasks`. It relies on `DataPersistence` for I/O.
* **`cli_interface.py` (User Interface Layer):** Fully implements menu display, user input gathering (with validation), and calls to `TaskManager` methods. Handles displaying results.
* **`main.py` (Orchestrator):** Initializes and runs the application flow.
## 4. Implementation Details & Challenges
### 4.1. Tags Implementation:
* Added `tags` as a `list` attribute to the `Task` base class.
* Ensured `to_dict` correctly serializes `tags` and `load_tasks` correctly deserializes them, handling cases where old tasks might not have a `tags` field initially.
* Modified `__str__` methods to display tags.
### 4.2. Search Implementation:
* `search_tasks` iterates through tasks, checking both `description` and `tags` for the `keyword` (case-insensitive). `any()` and `all()` were useful for checking tags.
### 4.3. Filter Implementation:
* `filter_tasks` takes multiple optional parameters. It applies filters sequentially, narrowing down the list of tasks.
* **Challenge: Date Filtering:** Required `isinstance()` checks to ensure only `DueDateTask` objects were considered for date-based filtering. `datetime.date` objects were used for comparison.
* **Challenge: Tag Filtering:** Required checking if *all* specified `contains_tags` were present in a task's `tags` list.
### 4.4. Sort Implementation:
* `sort_tasks` uses Python's built-in `list.sort()` with `lambda` functions for flexible key extraction.
* **Challenge: Polymorphic Sorting (Due Date/Priority):**
* For `due_date`, tasks without a `due_date` (i.e., `Task` or `PriorityTask` instances) were assigned `datetime.date.max` as a sorting key, effectively pushing them to the end (or beginning if reversed).
* For `priority`, a `PRIORITY_MAP` was used to convert "High", "Medium", "Low" to numerical values (1, 2, 3) for proper sorting. Tasks without a priority were assigned a high numerical value (e.g., 99) to group them at the end.
* A secondary sort key (`t.id`) was added to ensure consistent ordering among tasks with the same primary sort key.
### 4.5. Debugging Lessons:
* **Modular Debugging:** Being able to isolate issues to `task_manager.py` (logic errors) versus `cli_interface.py` (input parsing errors) was invaluable.
* **Conditional Breakpoints:** Especially useful for `filter_tasks` to check conditions only when specific filter parameters were present.
* **Inspecting Object State:** The debugger's ability to show `task` object attributes (including `tags`, `due_date`, `priority`) was critical for verifying data integrity after loading and during manipulation.
## 5. Future Work & Extension Ideas
* **Graphical User Interface (GUI)**: Transition from CLI to a visual interface.
* **Database Integration**: Replace JSON with SQLite for more robust data storage.
* **Reminders**: Implement a simple reminder system.
* **User Accounts**: Allow multiple users to manage their own tasks.
* **Recurring Tasks**: Support tasks that repeat on a schedule.
* **Unit Testing**: Develop comprehensive automated tests.
---
แหล่งที่มา
