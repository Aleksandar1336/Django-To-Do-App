# Django To-Do List App
This project is a todo list - the back-end works but the front-end is very poor so it's basically learning how to use django without front-end only back-end

1. Install Python

Make sure Python is installed:

python --version

or

python3 --version

If not installed, download it from the official Python website.

✅ 2. Navigate to Your Project Folder
cd path/to/your/project

Make sure this folder contains:

requirements.txt

manage.py

✅ 3. Create a Virtual Environment (venv)
On Windows:
python -m venv venv
On macOS/Linux:
python3 -m venv venv

This creates a folder called venv inside your project.

✅ 4. Activate the Virtual Environment
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

After activation, you should see:

(venv) your-project-folder$
✅ 5. Upgrade pip (Recommended)
pip install --upgrade pip
✅ 6. Install Dependencies from requirements.txt
pip install -r requirements.txt

This installs:

Django

And all other required packages

✅ 7. Apply Migrations
python manage.py migrate
✅ 8. Run the Development Server
python manage.py runserver

By default, your project will run at:

http://127.0.0.1:8000/
🔹 Optional: If You Need to Create a Superuser
python manage.py createsuperuser
🔹 To Deactivate venv Later
deactivate
