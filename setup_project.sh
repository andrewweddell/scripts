#!/bin/bash

# Check if a project name was provided
if [ -z "$1" ]; then
  echo "Usage: ./setup_project.sh <project_name>"
  exit 1
fi

PROJECT_NAME=$1

# Create project directory and navigate into it
mkdir $PROJECT_NAME
cd $PROJECT_NAME

# Initialize git repository
git init

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Create essential directories and files
mkdir src tests
touch src/__init__.py
touch README.md .gitignore requirements.txt setup.py

# Add common Python files and directories to .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "*.pyo" >> .gitignore
echo "*.pyd" >> .gitignore
echo "*.env" >> .gitignore

# Install common packages
pip install requests pytest

# Freeze the installed packages into requirements.txt
pip freeze > requirements.txt

# Add setup.py content
cat <<EOL > setup.py
from setuptools import setup, find_packages

setup(
    name='$PROJECT_NAME',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'myapp = src.main:main',
        ],
    },
)
EOL

# Create a simple script in src/main.py
cat <<EOL > src/main.py
def main():
    print('Hello, World!')

if __name__ == '__main__':
    main()
EOL

# Commit the initial setup to Git
git add .
git commit -m "Initial project setup"

echo "Project setup complete!"
