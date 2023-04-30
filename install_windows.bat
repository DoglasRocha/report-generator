if not exist ".venv/" (
    python -m venv .venv
)

venv/Scripts/activate.bat
pip install -r requirements.txt

echo venv/Scripts/activate.bat > start.bat 
python python/gui.py >> start.bat
