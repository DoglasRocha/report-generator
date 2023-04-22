if [ ! -d .venv ]; then
    python -m venv .venv
fi

. ./.venv/bin/activate
pip install -r requirements.txt

echo "#!/bin/sh
. ./.venv/bin/activate
python python/gui.py" > start.sh