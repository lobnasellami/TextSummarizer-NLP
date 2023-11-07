import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="TextSummarizer"
list_of_files=[
        #for CI/CD deployment for yaml file 
    "./github/workflows/.gitkeep" 
    #consreucotr file 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Components/_init_.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.py",
    "setup.py",
    "research/trials.ipynb"]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass # we jst want to creta the file 
            logging.info(f"Creating directory :{filedir} for the file {filename}")
    else :
        logging.info(f"File {filename} already exists")
        
