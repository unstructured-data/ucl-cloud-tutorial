# ucl-cloud-tutorial

Some intro

-------
## Creating and connecting to a VM

### A. Create a public/private key

Open the PowerShell, cd to the location where you want to store the Key: 

ssh-keygen -t rsa -f [KEY_FILENAME] -C [USERNAME]
ssh-keygen -t rsa -f test_key -C test-user


### B. Create a VM in GCP

### C. Connect to the VM via the terminal

ssh -i [PATH-TO-PRIVATE-KEY] [USERNAME]@[VM-IP-ADDRESS]
ssh -i C:\\Users\\yabra\\.ssh\\test_key test-user@34.171.141.200
ssh -i test_key test-user@34.30.159.216


### D. Connect to the VM through VSCode

1. Download the remote explore extension

2. Edit the config file to add the information of the VM and the keys

        ```yaml
        Host 34.30.159.216
            IdentityFile C:\Users\yabra\.ssh\test_key
            User test-user
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


### SSH Resources

- https://www.ssh.com/academy/ssh/keygen
- https://support.stackpath.com/hc/en-us/articles/360025597511-Generate-and-Add-SSH-Keys-for-a-Virtual-Machine
- https://cloud.google.com/compute/docs/connect/add-ssh-keys?hl=es-419#console
- https://towardsdatascience.com/unleash-the-power-of-visual-studio-code-vscode-on-google-cloud-platform-virtual-machine-f75f78f49aee

