# Instruction to run this mtfk
- Step 1: Install Python and pip
- Step 2: Install virtual environment by running this in terminal:
```bash
pip install virtualenv
```
You can install virtualvenv, Python and pip globally
- Step 3: Go to our project, and then create virtual environment
```bash
virtualenv env
```
- Step 4: Install all the required packages
```bash
pip install -r requirements/base.txt
```
- Step 5: Run the project
```bash
python3 manage.py runserver
```