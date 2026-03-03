# Django To-Do List App

This project is a simple To-Do list application built with Django. The backend is fully functional, but the frontend is minimal, serving as a learning tool for using Django without a front-end focus.

## Getting Started

Follow these steps to set up and run the application locally:

### 1. Install Python

Ensure Python is installed on your machine. You can check the version by running:

```bash
python --version
```
or
```bash
python3 --version
```

If Python is not installed, download it from the [official Python website](https://www.python.org/downloads/).

### 2. Navigate to Your Project Folder

Change to your project directory:

```bash
cd path/to/your/project
```

Ensure this folder contains:
- `requirements.txt`
- `manage.py`

### 3. Create a Virtual Environment (venv)

For Windows:
```bash
python -m venv venv
```

For macOS/Linux:
```bash
python3 -m venv venv
```

This will create a folder called `venv` inside your project directory.

### 4. Activate the Virtual Environment

For Windows:
```bash
venv\Scripts\activate
```

For macOS/Linux:
```bash
source venv/bin/activate
```

After activation, you should see the environment name in your terminal prompt, like so: 
```
(venv) your-project-folder$
```

### 5. Upgrade pip (Recommended)

It's a good practice to ensure you have the latest version of pip:

```bash
pip install --upgrade pip
```

### 6. Install Dependencies

Install the necessary packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install Django and any other required packages.

### 7. Apply Migrations

Run the following command to set up your database:

```bash
python manage.py migrate
```
### BEFORE STARTING - Create .env file in root of project and apply those variables:

DEBUG=False or True
SECRET_KEY="Your Secret Key Of Django App"
DATABASE_URL=sqlite:///db.sqlite3

### 8. Run the Development Server

Start your local development server with:

```bash
python manage.py runserver
```

By default, your project will be accessible at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Optional

- **Create a Superuser**: If you need to create a superuser for the admin interface, run:

  ```bash
  python manage.py createsuperuser
  ```

### Deactivate the Virtual Environment

When you're done, you can deactivate the virtual environment by running:

```bash
deactivate
```

---

Feel free to modify any sections as necessary! Would you like help with anything else?

