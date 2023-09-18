# Software Developer Salary Prediction

Welcome to the Software Developer Salary Prediction project, a machine learning initiative that leverages Streamlit to create an interactive web application. This application predicts a software developer's salary based on data from the Stack Overflow 2020 Developer Survey.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

In today's rapidly evolving tech industry, understanding the factors influencing a software developer's salary is crucial. This project utilizes machine learning to analyze the Stack Overflow 2020 Developer Survey data and predict salaries. The app provides a user-friendly interface to input details like country, education level, and years of experience, generating an estimated salary based on the provided information.

## Features

- **Predictive Model**: Employed machine learning model to predict software developer salaries.
- **Interactive Interface**: Utilizes Streamlit to create an interactive web application.
- **Data Processing**: Cleans and processes the Stack Overflow 2020 Developer Survey data for accurate predictions.

## Installation


Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol ` ; ` but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.


## Usage

- Go to your browser at the following address, to explore the app :
Network URL: http://172.20.10.4:8501

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Make your enhancements or fixes.
4. Submit a pull request.