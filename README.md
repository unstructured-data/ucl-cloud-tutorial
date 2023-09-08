# ucl-cloud-tutorial

This tutorial will demonstrate how to create a virtual machine (VM) in Google Cloud Platform (GCP), connect to it, deploy code and data on it, and execute a computationally intensive task.

-------

## 1. Creating and connecting to a VM

### A. Create a public/private key pair

- Open the PowerShell (Windows) Terminal (Mac) 
- Go to the location where you want to store the keys (using the ```cd``` command) 
- Execute the following command replacing *[KEY_FILENAME]* and *[USERNAME]* for appropriate values


```bash
ssh-keygen -t rsa -f [KEY_FILENAME] -C [USERNAME]
```

- Use the file navigation system to locate the files created

### B. Create a VM in GCP

- Create a GCP account and set up a billing method
- Choose a project to work in (as a starting point Google creates for you a project called *My First Project*)
- Enable *Compute Engine API* in GCP project
- Manually create a virtual machine. Make sure to:
    - Select an appropriate machine configuration
    - Select an appropriate boot disk
    - Allow full access to all Cloud APIs
    - Allow HTTP and HTTPS traffic
    - Unclik the "Control VM access through IAM permissions" option and "Block project-wide SSH keys"
    - Add your public key to the security information of the VM
- Make sure the VM is running

### C. Connect to the VM via the terminal

- Locate the IP address of your VM (e.g. 34.30.159.216)
- Open your PowerShell/Terminal and navigate to the folder with your private key
- Run the following command with the appropriate values

```bash
ssh -i [PATH-TO-PRIVATE-KEY] [USERNAME]@[VM-IP-ADDRESS]
```
- Explore your VM

### D. Connect to the VM through VSCode

- Download the *Remote Explorer* extension
- Locate the *.ssh* folder in your computer
- Create a file with no extension called *config*
- Edit the config file to add the information of the VM and the keys. Add the following block to the file:

    ```python
    Host [VM-IP-ADDRESS]
        IdentityFile [FULL-PATH-TO-PRIVATE-KEY]  # e.g. C:\Users\yabra\.ssh\test_key
        User [USERNAME]
        IdentitiesOnly=yes
        CheckHostIP=no
    ```

- Connect by clicking on the IP address of the VM

## 2. VSCode tour and Linux installations

### A. Tour

- File explorer
- Terminal
- Extensions

### B. Linux installations

We are not going to learn Linux. However, here are some very basic commands that are important to remember:

- Change Directory (cd)
- List (ls)
- sudo apt install

As a demonstration we will install to basic additional Linux libraries (i.e. *git* and *wget*). We just need to run the commands below

```bash
sudo apt-get update 
sudo apt-get install git wget
```

Lastly, we will also install the *pip* library that allows us to easily install Python libraries:

```bash
sudo apt install python3-dev python3-venv
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```


## 3. Code and data management

In order to download the data files we will use in this tutorial go to the following two links:
- [Document-term matrix](https://drive.google.com/file/d/1Ru4p2I3C-3rPBAnU3D8WGlGfBhoHAAVb/view?usp=sharing)
- [Covariates data](https://drive.google.com/file/d/1WUVFrJWD1xpUOy9_dHEuWM3CyaMZSvLa/view?usp=drive_link)


Files can be moved to the VM by simply dragging and dropping them in VSCode. However, for large files this might not be the best solution.

### A. Bucket creation

Buckets are another product from the GCP family of products. Buckets are basic data containers that can hold large amounts of data for a good price. They can easily connect to VMs.

We will create a bucket by following the steps below:

- Go to *Cloud Storage*
- Select *Buckets*
- Click on *Create*
- Give your bucket a name
- Choose a region (be mindful of GDPR regulation)
- Select appropriate options

### B. Bucket to VM data transfer

In order to transfer files from a Bucket to a VM they should both be in the same GCP project. We will transfer files by running the following command:

```bash
# option 1
gcloud storage cp gs://[BUCKET-NAME]/[FILE-PATH] [DESTINATION-PATH]
# option 2
gsutil cp gs://[BUCKET-NAME]/[FILE-PATH] [DESTINATION-PATH]
```

## 4. Code demonstration

Now that we have data and code on the VM we can execute our task.

### A. Install  VSCode extensions and Python libraries on the VM

Before actually executing our code we need to install a couple of Python libraries. We do this by simply running the command below on the Terminal:

```bash
pip install pandas scikit-learn
```

We also need to install the *Python VSCode extension*. This extension will allow us to interactive run any Python script. Once we have this extension we can go to the *demonstration.py* script (or any Python script) and run it interactively. To do this we just need to add ```#%%``` add the start and the end of the chunk of code we want to execute. After running the first chunk of code we will be asked if we want to accept the installation of the *ipykernel* package. Accept the installation.

## 5. GPU drivers

For a complete guide on how to setup all the necessary software to use a GPU on a VM follow [this](./gpu_setup.md) guide.

-------

## External resources

### Basic GCP commands

- [Here](./gcp_commands.md) is a list of some basic commands from GCP.

### Key generation and SSH 

- https://www.ssh.com/academy/ssh/keygen
- https://support.stackpath.com/hc/en-us/articles/360025597511-Generate-and-Add-SSH-Keys-for-a-Virtual-Machine
- https://cloud.google.com/compute/docs/connect/add-ssh-keys?hl=es-419#console
- https://towardsdatascience.com/unleash-the-power-of-visual-studio-code-vscode-on-google-cloud-platform-virtual-machine-f75f78f49aee

