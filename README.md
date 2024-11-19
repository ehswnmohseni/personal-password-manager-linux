# Personal Password Manager!

This is a Python-based password manager designed to securely store and retrieve your sensitive information 
-   This is a simple **Python application** designed to securely store and manage your passwords.
-   Your passwords are **encrypted** and stored within the application.
-   To access the application, you must pass both password and **facial recognition** authentication.
-   For security reasons, the application operates entirely **offline**.
-   To enhance security, the file encryption is updated every **24 hours**.
- If the application detects a potential hacking attempt, it will **delete** all critical files.

**Personal Password Manager** uses [cryptography](https://github.com/pyca/cryptography) library for data encryption and [deep face library](https://github.com/serengil/deepface/) for facial detection.


# Install on Linux :

Here's how to install the project step by step :
1. install project from github 

    git clone https://github.com/ehswnmohseni/personal-password-manager.git
    
2. to open project file :
	
    cd personal-password-manager

3. to install requirements 
    
    python3 -m pip install -r requirements.txt

4. to run project 

    python3 main.py

5. you should get error 

6. for open the program you need skip face recognition for this Copy your desired facial image and name it 'pattern.jpg'. Save it to the following address /home/{your_os_name}/Pictures/images/pattern.jpg

7. Please also save a copy of your image key as 'key.jpg' in the same folder as the previous image.

> Please ensure that the face saved as 'pattern' is identical to the
> face saved as 'key'. Both images should be of the same person and will
> be used to unlock the program. Note that the 'key' image will be
> deleted after each successful login.

   7. for first login your password is **admin** after login you can change your password.

**now you can use personal password manager in linux!**

## add password to your password manager 

after login you can enter "add" syntax to add new password to your passwords list 
first : enter name of password for example instagram 
then : enter password you like 

## change login password 

after login you can enter "change" syntax to change your login password
first : Enter your current password
then : Enter your new password

## see list of password

after login you can enter "list" syntax to see your all passwords 
when you input the password name, the program will return the password to you

> Please note that the password will be available to you for ten seconds

## exit from program 

you can enter "exit" syntax to exit from password manager
