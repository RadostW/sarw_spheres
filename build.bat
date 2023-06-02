export CIBW_BUILD="cp3[891]*-win_amd64"
export CIBW_SKIP="cp31[12]*"
export CIBW_BEFORE_BUILD="python3 -m pip install -U pip wheel numpy==1.22"
cibuildwheel --platform windows
