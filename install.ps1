# Download Python
Write-Output "Downloading Python..."
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe" -OutFile "$Env:USERPROFILE\Downloads\python-3.8.6.exe"

# Install Python
Write-Output "Installing Python..."
Start-Process -FilePath "$Env:USERPROFILE\Downloads\python-3.8.6.exe" -ArgumentList "/passive", "InstallAllUsers=1", "PrependPath=1", "Include_test=0" -Wait

# Confirm Python Is Installed
python --version

# Install pip
Write-Output "Installing pip..."
python -m ensurepip --upgrade

# Confirm pip Is Installed
pip --version

# Change directory to the location of the requirements.txt file
cd "path_to_your_requirements_file"

# Install Python packages from requirements.txt
pip install -r requirements.txt

Write-Output "Python and the dependencies are now installed. You can now run your Python script using the following command:\r\n python main.py path_to_source_dir path_to_dest_dir"
