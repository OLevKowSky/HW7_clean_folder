
from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme:
    long_description = readme.read


setup(
    name = "clean_folder_HW7_Levkowskyi",
    version = "0.0.1",
    author = "Levkovskyi Oleksandr",
    author_email = "olevkowsky@gmail.com",
    description = "A script that parses the junk folder",
    long_description = "To do this, our application will check the file extension (the last characters in the file name, usually after a dot) and, depending on the extension, make a decision to which category to assign this file. The script accepts one argument at startup — the name of the folder in which it will sort. Let's say the file with the program is called sort.py, then to sort the /user/Desktop/Junk folder, you need to run the script with the python command sort.py /user/Desktop/Junk",
    url = "https://olevkowsky.github.io/HW7_clean_folder/",
    project_urls = {
        "repository": "https://olevkowsky.github.io/HW7_clean_folder/",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir = {"": "src"},
    packages = find_packages("src"),
    python_requires = ">=3.11"
)
