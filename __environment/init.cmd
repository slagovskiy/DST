mkdir venv
rem compact /c /i /q /f /s:venv
virtualenv venv
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install --upgrade -r requirements.txt
