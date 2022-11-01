# Project to practice the follow topics:
- Create virtual environments.
- Create dockerfile and dockercompose to execute contenedors.
- Execute python files manual and script mode.
- Create modules, packages, variables, cicles, conditionals, etc..
- Create webserver with the library FastAPI
- Integrate git, github

# Requirements
- Python 3.8 or higger.
- Have install PIP.
- Linux or Mac Operating System. For windows work with WSL.
- Docker.

# Execute the project:
- Clone the project: https://github.com/anfesos/platzi_backend.git

## game package
- Go to "game" folder.
- Execute the command "python3 -m venv env" to create the virtual environment.
- Execute the command "source env/bin/activate"

### Manual Execution:
- Run in the terminal the function "run()" on the module "main.py"

### Script Execution:
- Run the module "main.py" in the terminal.

## app package
- Go to "app" folder.
- Execute the command "python3 -m venv env" to create the virtual environment.
- Execute the command "source env/bin/activate"
- Execute the command "pip install -r requirements.txt"

### Manual Execution:
- Run in the terminal the function "run()" on the module "main.py"

### Script Execution:
- Run the module "main.py" in the terminal.

### Docker Execution:
- Execute the command "docker-compose build" to build the image.
- Execute the command "docket-compose up -d" to up the container.
- Execute the command "docker-compose ps" to validate that the container started.
- Execute the command "docker-compose exec app-csv bash" to run the container.
- Execute the command "python main.py" to run the application.
- Execute the command "exit" for exit the container.
- Execute the command "docker-compose down" to stop and down the container.

## webserver package
- Go to "webserver" folder.
- Execute the command "python3 -m venv env" to create the virtual environment.
- Execute the command "source env/bin/activate"
- Execute the command "pip install -r requirements.txt"

### Script Execution:
- Execute the command "uvicorn main:app --reload"
- Run in the terminal the function "run()" on the module "main.py"
- Go to URL http://127.0.0.1:8000 to see the respond "/".
- Go to URL http://127.0.0.1:8000/contact to see the respond "/Contact".

### Docker Execution:
- Execute the command "docker-compose build" to build the image.
- Execute the command "docket-compose up -d" to up the container.
- Execute the command "docker-compose ps" to validate that the container started.
- Go to URL http://localhost to see the respond "/".
- Go to URL http://localhost/contact to see the respond "/Contact".
- Execute the command "docker-compose down" to stop and down the container.


## Note:
- Remmember for down the virtual envitonment you shoud execute the command "deactivate"
