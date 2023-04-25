# ucl-cloud-tutorial

Some intro

-------
## Creating and connecting to a VM

### A. Create a public/private key

- Open the PowerShell
- cd to the location where you want to store the keys 
- Execute the following command

```bash
ssh-keygen -t rsa -f [KEY_FILENAME] -C [USERNAME]
```

### B. Create a VM in GCP

Manually create a virtual machine. Make sure to:

- Add your public key to the security information of the VM
- Allow HTTP and HTTPS 
- Unclik the special GCP security options

### C. Connect to the VM via the terminal

- Locate the IP address of your VM (e.g. 34.30.159.216)
- cd to the folder with your private key
- Run the following command

```bash
ssh -i [PATH-TO-PRIVATE-KEY] [USERNAME]@[VM-IP-ADDRESS]
```

### D. Connect to the VM through VSCode

1. Download the *Remote Explorer* extension

2. Edit the config file to add the information of the VM and the keys. Add the following block to the file:

    ```python
    Host [VM-IP-ADDRESS]
        IdentityFile [FULL-PATH-TO-PRIVATE-KEY]
        #IdentityFile C:\Users\yabra\.ssh\test_key
        User [USERNAME]
        IdentitiesOnly=yes
        CheckHostIP=no
    ```

3. Connect by clicking on the IP address of the VM

## Mini VSCode tour and Linux installations

### A. Tour

- File explorer
- Terminal
- Extensions

### B. Linux installations

Basic linux commands

- Change Directory (cd)
- List (ls)
- sudo apt install

Basic installations

```bash
sudo apt-get update 
sudo apt-get install git wget
```

```bash
# install additional libraries for python3
sudo apt install python3-dev python3-venv
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```


## Code Management

- Drag and drop code
- Clone github repository

## Data Management

### A. Manual data upload

Drag and drop using VSCode interface (not recommended for large files)

Through GCP web SSH

### B. SCP

Source: https://cloud.google.com/compute/docs/instances/transfer-files?hl=es-419#scp

Linux/Mac

scp -i ~/.ssh/my-ssh-key LOCAL_FILE_PATH USERNAME@IP_ADDRESS:~

Windows

Winscp (horrible)

### C. Download online data through Python

### D. Bucket

- Copy from bucket
- Mount the bucket

## Code Demonstration


### A. Install extensions

- Python
- Accept the installation of the ipykernel package


### B. Install Python libraries

```bash
pip install pandas scikit-learn transformers datasets
```

### B. Running Python interactively


-------

## External resources

### Key generation and SSH 

- https://www.ssh.com/academy/ssh/keygen
- https://support.stackpath.com/hc/en-us/articles/360025597511-Generate-and-Add-SSH-Keys-for-a-Virtual-Machine
- https://cloud.google.com/compute/docs/connect/add-ssh-keys?hl=es-419#console
- https://towardsdatascience.com/unleash-the-power-of-visual-studio-code-vscode-on-google-cloud-platform-virtual-machine-f75f78f49aee

