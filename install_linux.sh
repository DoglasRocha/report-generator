if [ ! -d .venv ]; then
    python -m venv .venv
    . ./.venv/bin/activate
    pip install -r requirements.txt
fi

echo "#!/bin/sh
. ./.venv/bin/activate
python python/gui.py" > start.sh