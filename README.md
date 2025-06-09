# CSV Insight Assistant

CSV Insight Assistant is a lightweight Python tool that helps you explore CSV datasets quickly. It’s designed to give you useful summaries and charts without writing analysis code.

## What it Does

- Loads any CSV file
- Cleans inconsistent or missing values
- Lets you pick from common analysis options via a simple menu
- Creates and saves bar charts automatically

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/theightcoder8/csv-insight-assistant.git
cd csv-insight-assistant
```

### 2. (Optional) Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install the Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python src/user_interface.py
```

### 5. Follow the Prompts

You will be guided through menu options like:

- Top 10 cancer sites by count
- Tumor type frequency
- Stage distribution
- Age group breakdowns

The generated charts will be saved automatically in the `charts/` folder.

---

## Project Structure

```
csv-insight-assistant/
├── data/             # Input CSV files
├── charts/           # Saved visualizations
├── src/              # Python scripts
│   ├── cleaning.py
│   ├── visuals.py
│   └── user_interface.py
├── notebooks/        # Optional: Jupyter exploration
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.7 or higher
- pandas
- matplotlib
- numpy

Install everything with:

```bash
pip install -r requirements.txt
```

