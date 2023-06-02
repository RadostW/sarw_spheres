set CIBW_BUILD=cp3[891]*-win_amd64
set CIBW_SKIP=cp31[12]*
set CIBW_BEFORE_BUILD=python.exe -m pip install -U pip wheel numpy==1.22

python.exe -m cibuildwheel --platform windows
