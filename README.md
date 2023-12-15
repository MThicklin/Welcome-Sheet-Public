
# Welcome Sheet Maker

This Python script generates Welcome Sheets for new users.

### How does it work?

Make sure you have at least python 3.8 and the PyPDF package installed.

Download this Repo
Unzip it where you want
Open a command prompt in the directory where you unzipped the repo

Basic use: python main.py -n firstName lastName 

When you first try out the script, it will make a PDF filled with '<Company X here>' statements.  Of course, there's a little work to be done to make this script fit your situation.   Most adjustments will be made in the person class.


## Options:

### -n, --name

Name of user.  Needs at least a first and last name, but can accept any number of middle names.  However if the name is too long, it wil run off the page.

### -nn, --uNameNum

Number added to the end of username. Use 'none' to omit this number.  Default: 01.

### -en, --emailNum

Number added to the end of the email address. In the rare case that you have a username ending in 01 and need a number at the end of the email to be different. Default: blank.

### -o, --o365

Adds a Office 365 password section to the welcome sheet.  Use "pass" if the Office365 password needs to match the login password.  Use "gen" to generate a random password.

### -p, --passw

Option to add a specfic password to the welcome sheet. Use 'gen' to have a random password generated.  This password is a 6 letter word (Created from 2 - 3 letter words).  If the option isn't used, it will use the default password in script.

### -c, --compname

Adjusts the company name in the title in case you make welcome sheets for multiple companies.

### -d, --deskPhoneExt

This adds a section for phone extensions to the welcome sheet.  You can change the phone's area code and prefix at the self.phonePrefix variable in the Person class (main.py, Line 35).

### -v, -voicemail

If your company uses a phone system with voicemail, you can adjust the password to access it here.  Default: 0000

### -pa, --phone

This is an example section if you what to expand this script to include different sections.


## Examples:

***First & Last name, random PC login password:***
python main.py -n firstName lastName -p gen

***First & Last name, random login and office 365 password:*** 
python main.py -n firstName lastName -p gen -o gen

***First, Middle & Last name, random login password,  office 365 password same as login:*** 
python main.py -n firstName middleName lastName -p gen -o pass

