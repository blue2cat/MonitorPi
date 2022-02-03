# Prerequisites to install Powershell

# Update package lists
sudo apt-get update

# Install libunwind8 and libssl1.0
# Regex is used to ensure that we do not install libssl1.0-dev, as it is a variant that is not required
sudo apt-get install '^libssl1.0.[0-9]$' libunwind8 -y

# Download and extract PowerShell
# Grab the latest tar.gz
wget https://github.com/PowerShell/PowerShell/releases/download/v7.1.3/powershell-7.1.3-linux-arm32.tar.gz

# Make folder to put powershell
sudo mkdir /etc/powershell

# Unpack the tar.gz file
sudo tar -xvf ./powershell-7.1.3-linux-arm32.tar.gz -C /etc/powershell

# Start PowerShell from bash with sudo to create a symbolic link
sudo /etc/powershell/pwsh -c New-Item -ItemType SymbolicLink -Path "/usr/bin/pwsh" -Target "$PSHOME/pwsh" -Force

# Now to start PowerShell you can just run /etc/powershell/pwsh

# Start PowerShell and setup script
/etc/powershell/pwsh ~/setup.ps1
