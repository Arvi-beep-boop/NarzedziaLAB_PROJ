# installResources.ps1

# Update pip to the latest version
python -m pip install --upgrade pip
pip install pyyaml pyinstaller
pyinstaller --onefile converter.py

# Install required Python packages
