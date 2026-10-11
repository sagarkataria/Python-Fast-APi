step -1 

python -m venv venv

step 1.1 - To activate python script

.\venv\Scripts\activate

step - 2

pip install "fastapi[standard]"

step - 3

python.exe -m pip install --upgrade pip

step - 4

pip freeze > requirement.txt

step - 5

uvicorn main:app -- reload

this command will run your app with default port 8000

later on you can change your port by command

uvicorn main:app -- reload --port 3000