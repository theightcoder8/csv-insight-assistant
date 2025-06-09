# CSV Insight Assistant

CSV Insight Assistant is an interactive Python tool that helps you load, clean, explore, and visualize CSV files easily through a simple terminal interface. It is designed for users who want structured data insights without writing analysis code from scratch.

## Features

- Load and preview any CSV file
- Clean missing or inconsistent values
- Choose from several insight options via menu
- Automatically generate and save bar charts
- Organized project structure for further development

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/theightcoder8/csv-insight-assistant.git
cd csv-insight-assistant
```

### 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the assistant
python src/user_interface.py

### 5. Follow the prompts
You will be asked to choose insights such as:

Top 10 cancer sites by count

Patient distribution by age

Tumour type frequency

Stage distribution

Visualizations will be saved automatically in the charts/ folder.

## Project Structure
csv-insight-assistant/
├── charts/              <- Auto-generated PNG charts
├── data/                <- Raw and cleaned CSV files
├── notebooks/           <- Jupyter notebooks for exploration
├── src/                 <- Core Python modules
│   ├── cleaning.py
│   ├── visuals.py
│   └── user_interface.py
├── README.md
└── requirements.txt

## Requirements
Python 3.7 or above
pandas

matplotlib

numpy

Install all with:

bash
Copy
Edit
