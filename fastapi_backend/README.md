# fastapi_backend
The backend part of the [book recommendation web application](https://github.com/Mykhailo20/Book_Recommendation_System) implemented on FastAPI.

## :open_file_folder: Project Files Description
This part of the project consists of 6 folders and 3 files:

**Files**:
1. **main.py**: Is an entry point of the system, imports all routers and contains CORS settings.
2. **requirements.txt** and **requirements_full.txt**: Contains system dependencies (Third-Party Python libraries and their versions):
    * **requirements.txt** contains libraries installed manually during system development using the pip install command.
    * **requirements_full.txt** is the result of the `pip freeze > requirements_full.txt` command (all libraries that were installed during the development of the system).

**Folders**:
1. **artifacts** contains: 
    - **db_schemas** subfolder: Database schema backups, database ER-diagrams, and database creation commands.
    - **jupyter_notebooks** subfolder: Notebooks that contain code for dataset exploration, recommender systems building, and ETL process.
2. **book_recommendation_systems**: Contains files with the code of recommendation systems.
3. **config**: Contains the configuration of project data (data_config.py) and files (files_config.py) used in the backend part.
4. **db**: Contains code for working with the PostgreSQL database (connection to the database, CRUD operations).
5. **routers**: Organizes and contains the route definitions for different parts of the FastAPI application, ensuring a modular and maintainable code structure.
6. **utils**: Contains utility functions and helper modules that provide common functionalities used across the FastAPI application.