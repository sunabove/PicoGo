# PicoGo Build Process
pip install setuptools wheel twine

python setup.py sdist bdist_wheel

python -m twine upload dist/*