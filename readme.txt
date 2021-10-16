
Windows 
1. Create your project folder. 
2. Open up terminal and cd to project folder. 
3. Create venv with the following commands:
- python -m venv env 
- env\Scripts\activate
(Project folder should now appear before the file path, i.e. (env) C:\Users\...
- pip install flask 
- set FLASK_APP=application.py

4. To run flask, run:
- flask run 
or:
- python application.py

4. To enter into development mode, run:
- set FLASK_ENVIRONMENT=development 
