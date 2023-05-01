if [ ! -d .venv ]; then
    python -m venv .venv
fi

. ./.venv/bin/activate
pip install -r requirements.txt

echo "#!/bin/sh
. ./.venv/bin/activate
python python/gui.py" > start.sh

PATH_TO_START=$(realpath start.sh)

echo "[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=sh $PATH_TO_START
Name=Gerador de Relatório" > Gerador\ de\ Relatório.desktop

