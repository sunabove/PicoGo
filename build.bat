# PicoGo Build Process
pip install setuptools wheel build twine --upgrade

python setup.py clean sdist bdist_wheel 

python -m twine upload --skip-existing dist/* 