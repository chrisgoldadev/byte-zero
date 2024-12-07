# Project ByteZero
ByteZero is a small job opening project designed to analyze customer behavior and build a customized purchase funnel from scratch. The name reflects the project's focus on creating a detailed, "elementary" understanding of user journey. Like how bytes are fundamental building blocks in programs.

## Description
This project analyzes customer behavior and creates an ETL pipeline, moving data from the source, through transformations, and loading it into a SQL database. It provides insights into user actions on the website and helps identify the customer journey from visiting product pages to making a purchase.

## Objectives
- Analyze provided customer data to identify behaviors and patterns.
- Build a data pipeline for extracting, transforming, and loading (ETL) data.
- Create an analytical report to visualize customer journeys and conversions.

## Requirements
Python 3.12.4
path to you python executable for example default python path is "C:\Program Files\python 3.12.4\python.exe"
pip (Python package installer)
Web Browser

## Setup
1. Unpack the ZIP file to the desired folder, this will be your root folder of the project, should be extract for example to "C:\ByteZero", make sure all your files are inside folder "ByteZero";
2. Open CMD (Command Prompt): make sure you are running CMD as administrator;
3. Navigate to the project folder once unpacked;
3. Create a virtual environement: Note: If python is not recognized, ensure that the path to your Python executable is correct.
-- "path\to\python" -m venv venv;
4. Activate the virtual environement:
-- venv\Scripts\activate;
5. Install dependencies:
-- pip install -r requirements.txt, it can take few minutes to install dependencies, depends on your bandwith connection

Notice: If you are using VS Code just simply copy content of ByteZero folder to your project folder, using your venv you can start the programs. Make sure you have all necessary packages.

Notice: Scripts are designed with Python 3.12.4 version and pip version 24.3.1, if your pip version is different you can run -m pip install --upgrade pip==24.3.1 in CMD.

You are set up, you can run scripts inside the ByteZero folder.

## Files
data_set_da_test.csv -> dataset provided by employer
step_a.py -> python program to analyse provided dataset
step_b.py -> python program to transform provided dataset
requirements.txt -> file which contains all packages necessary to run scripts in ByteZero folder

## Usage
1. Run 'step_a.py' program. CMD: python step_a.py
2. Run 'step_b.py program. CMD: python step_b.py
3. After running both steps, you can open 'Customer Analysis.pbix' file to view the report in PowerBI tool. 

## IMPORTANT NOTICE
To run step_b.py file please make sure you have username and password to SQL database provided in the email, due to security reasons password and username credentials are outside of the repository.
