# Glucometer Data Analyzer

A Python program that analyzes glucometer measurements from multiple patients and generates a report highlighting abnormal glucose levels.

The program processes glucose measurements from a structured data file, computes statistics for each patient, and detects measurements that exceed a specified glucose threshold.

---

## Project Context

This project was developed as part of coursework at **Politecnico di Torino (PoliTo)**.

The objective of the project was to practice:

- file parsing
- data aggregation
- simple statistical analysis
- working with Python data structures

---

## Features

- Parse glucometer measurements from a structured file
- Compute the number of measurements per patient
- Detect glucose values above a defined threshold
- Count abnormal measurements
- Identify high-risk patients based on abnormal readings
- Generate a summary report

---

## Input File Format

The program reads an input file called:

glucometer.txt

Each line contains a glucose measurement in the following format:

patient_id;date;time;glucose_value

Example:

P01;2024-02-01;08:00;135
P01;2024-02-01;12:00;210
P02;2024-02-01;09:30;180
P03;2024-02-01;10:15;250

---

## Analysis

The program analyzes the data and identifies glucose measurements above a defined threshold (for example **200 mg/dL**).

For each patient it calculates:

- total number of measurements
- number of abnormal measurements
- maximum glucose value recorded

---

## Output

The program generates a report file summarizing the analysis.

Example output:

Patients

P01  measurements=2  abnormal=1  max_glucose=210
P02  measurements=1  abnormal=0  max_glucose=180
P03  measurements=1  abnormal=1  max_glucose=250

High Risk Patients
P01
P03

---

## How to Run

Make sure the input file is in the same directory as the program.

Run the script:

python main.py

After execution, the program will generate the analysis report.

---

## Technologies

- Python
- File processing
- Data aggregation
- Basic statistical analysis

---

## Learning Objectives

- Processing structured health data
- Detecting abnormal measurements
- Generating automated reports
- Using Python data structures for data analysis
