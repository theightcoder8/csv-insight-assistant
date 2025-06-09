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
2. (Optional) Set Up a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
3. Install the Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
python src/user_interface.py
Follow the on-screen prompts to explore your data. Charts will be saved automatically in the charts/ folder.

Folder Overview
bash
Copy
Edit
csv-insight-assistant/
├── data/           # Input CSV files
├── charts/         # Saved charts
├── src/            # Python scripts
│   ├── cleaning.py
│   ├── visuals.py
│   └── user_interface.py
├── notebooks/      # Optional: Jupyter exploration
├── requirements.txt
└── README.md
Requirements
Python 3.7 or higher

pandas

matplotlib

numpy

To install everything at once:

bash
Copy
Edit
pip install -r requirements.txt
css
Copy
Edit

Let me know if you want to add sample output, screenshots, or a license section.
