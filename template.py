import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

# Iterate over each file path in the list
for filepath in list_of_files:
    # Convert 'filepath' to a Path object for better path manipulations
    filepath = Path(filepath)
    
    # Split the 'filepath' into directory ('filedir') and file name ('filename')
    filedir, filename = os.path.split(filepath)
    
    # Check if the directory part of the path is not empty
    if filedir != "":
        # Create the directory and any necessary parent directories if they do not exist
        os.makedirs(filedir, exist_ok=True)
        # Log the creation of the directory
        logging.info(f"Creating Directory: {filedir} for the file {filename}")
    
    # Check if the file does not exist or if it is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open the file in write mode, which creates an empty file
        with open(filepath, 'w') as f:
            pass  # No operation (placeholder for future code if needed)
        # Log the creation of the empty file
        logging.info(f"Creating empty file: {filepath}")
