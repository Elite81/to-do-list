
# ToDoList - Task App

A simple web-based **ToDo List application** built with **Django** and **Bootstrap**, allowing authenticated users to manage their tasks efficiently. Users can **create, read, update, delete (CRUD)**, and **search** their tasks.

---
## Demo
#### Live Demo:   <https://tasks-7ugz.onrender.com/>
#### Video Demo:  <URL HERE>


## Description:

### Project Structure and File Description

The project follows Django’s standard project structure and uses a single main app named **Task**.

- `models.py`  
  Defines the **Task** model, including fields such as title, description, and user relationship. This file is responsible for database structure and data storage.

- `views.py`  
  Contains the core application logic. It handles user requests, implements CRUD operations, manages authentication checks, and processes search functionality.

- `urls.py`  
  Maps application URLs to their corresponding views, enabling navigation between pages such as login, dashboard, task creation, and task detail views.

- `templates/`  
  Contains all HTML files used to render the frontend interface. These templates are styled using Bootstrap and dynamically populated with data from the backend.

- `forms.py` (if applicable)  
  Manages Django forms used for task creation and editing, ensuring validation and clean input handling.

- `settings.py`  
  Handles global project configuration, including installed apps, database settings, and authentication configuration.

- `db.sqlite3`  
  The default SQLite database used to store users and task data during development.

#### Project Logic and Testing

This project includes two additional files in the root directory: project.py and test_project.py.

- `project.py`
    The project.py file contains helper functions that implement the core business logic used by the view functions in views.py. This separation keeps the views clean and focused on handling requests and rendering responses.

-  `test_project.py`
    The test_project.py file contains tests for the helper functions in project.py. Each helper function has a corresponding test function, named with the required test_ prefix. All helper functions are tested, and the tests were executed from the terminal to verify the correctness of the application logic.

### Testing

    Application testing was performed using Django’s built-in testing tools. Tests were executed from the terminal to ensure that core functionalities, such as authentication, task creation, and data handling, work as expected. Test results were displayed in the terminal during the video demonstration.


---

## Features

- User **authentication** (signup, login, logout)
- **CRUD operations** on tasks
- **Search** tasks by title or description
- Responsive design using **Bootstrap**
- Uses **SQLite3** as the default database

---

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite3 (default)
- **Other:** Python 3.x

---

## Installation

1. **Clone the repository:**

    git clone https://github.com/elite81/to-do-list.git
    cd to-do-list



2. **Clone the repository:**

    - Create a virtual environment:

        python -m venv venv
        source venv/bin/activate  # Linux/macOS
        venv\Scripts\activate     # Windows

3. **Install dependencies:**

    - pip install -r requirements.txt


4. **Apply migrations:**

    - python manage.py migrate


5. **Create a superuser (optional, for admin access):**

    - python manage.py createsuperuser


6. **Run the development server:**

    - python manage.py runserver


7. **Open your browser and go to:**

    - http://127.0.0.1:8000/


8.  **Usage**

    - Sign up or log in to your account.

    - Add new tasks using the "Add Task" button.

    -  View task

    - Edit or delete existing tasks.

    - Use the search bar to find tasks by title or description.



## Conclusion

    The ToDoList Task Application successfully meets the objectives of the final project by demonstrating core web development concepts using Django. It showcases user authentication, database interaction, CRUD operations, and clean application structure. The project provides a solid foundation that can be extended in the future with additional features such as task status tracking, deadlines, or user notifications.

## License

    This project is for educational purposes as part of CS50p.


## Author
    Edoh Mensah Akpedzene
    CS50 Student | Full-Stack Developer
---




**Note:** 
    This README.md was written with assistance from ChatGPT to ensure clarity and professionalism.