# proj3

Three Steps to set up your virtual environment, run the code, and generate a flake8 file. 

---

## 1. Build & Activate the Virtual Environment

# A. Create the virtual environment
cd proj3

python -m venv enviro

# B. Activate the virtual environment
.\enviro\Scripts\activate


# C. Install project dependencies
pip install --upgrade pip

pip install -r requirements.txt

## 2. Run the Code
python etl_pipeline.py

## 3. Generate a flake8 Report

# A. Install Packages (if not done so previously)
pip install flake8 flake8-html


# B. Generate File 
flake8 . > flake8_report.txt


