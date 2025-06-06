import os

PROJECT_NAME = "ml_project"  # Change this to your desired project name

# Folder structure to create
folders = [
    f"src/{PROJECT_NAME}",
    f"src/{PROJECT_NAME}/utils",
    f"src/{PROJECT_NAME}/config",
    "notebooks",
    "tests",
    "logs"
]

# Empty files to create
files = [
    "README.md",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "pyproject.toml",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/logger.py",
    f"src/{PROJECT_NAME}/custom_exception.py",
    f"src/{PROJECT_NAME}/config/config.yaml",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    "tests/test_dummy.py",
    "notebooks/example.ipynb"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file_path in files:
    with open(file_path, "w") as f:
        pass

print(f"✅ Clean template for '{PROJECT_NAME}' created successfully.")
