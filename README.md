# proj3

Three Steps to set up your virtual environment, run the code, and generate a flake8-html file. 

---

## 1. Build & Activate the Virtual Environment

# A. Create the venv
cd proj3
python -m venv enviro

# B. Activate the venv
.\enviro\Scripts\activate


# C. Install project dependencies
pip install --upgrade pip
pip install -r requirements.txt

## 2. Run the Code
python etl_pipeline.py

## 3. Generate a flake8 Report

# A. Install
pip install flake8 flake8-html

# B. Run flake8 with HTML output
flake8 --format=html --htmldir=deliverables/flake8-report

# C. View the report
start deliverables\flake8-report\index.html
