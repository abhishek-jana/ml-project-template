from setuptools import setup, find_packages

PROJECT_NAME = "ml_project"  # Update this to match your project folder name

def parse_requirements(filename="requirements.txt"):
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#") and not line.startswith("-e")]

setup(
    name=PROJECT_NAME,
    version="0.1.0",
    description="A modular ML project template",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=parse_requirements(),
    python_requires=">=3.8",
)
