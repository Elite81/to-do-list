
# ToDoList - Task App

A simple web-based **ToDo List application** built with **Django** and **Bootstrap**, allowing authenticated users to manage their tasks efficiently. Users can **create, read, update, delete (CRUD)**, and **search** their tasks.

---
## Demo
#### Live Demo:   <https://tasks-7ugz.onrender.com/>
#### Video Demo:  <URL HERE>




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

```bash
git clone https://github.com/elite81/to-do-list.git
cd to-do-list

```

**Instalation:**
2. **Clone the repository:**

- Create a virtual environment:

    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. **Install dependencies:**
    pip install -r requirements.txt


4. **Apply migrations:**
    python manage.py migrate


5. **Create a superuser (optional, for admin access):**

    python manage.py createsuperuser


6. **Run the development server:**

    python manage.py runserver


7. **Open your browser and go to:**

    http://127.0.0.1:8000/


8.  **Usage**

    Sign up or log in to your account.

    Add new tasks using the "Add Task" button.

    Edit or delete existing tasks.

    Use the search bar to find tasks by title or description.



## License

    This project is for educational purposes as part of CS50p.


## Author
    Edoh Mensah Akpedzene
    CS50P Student | Full-Stack Developer
---

**Note:** This README.md was written with assistance from ChatGPT to ensure clarity and professionalism.