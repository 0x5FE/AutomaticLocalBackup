- It provides a simple and automated way to protect your data by regularly creating backups.

- The script reads the configuration from the ***config.ini file***, which should be located in the same directory as the script.

- It checks the specified source and destination folders from the configuration.

- If the source folder exists, it prompts the user to enter a secure passphrase for the backup.

- If a passphrase is provided, it creates a timestamped backup folder in the destination folder.

- It recursively copies all files from the source folder to the backup folder, preserving the directory structure.

- The script logs the backup process, including successful file copies and any encountered errors.

- Once the backup process is completed, it logs a success message.
    

# Prerequisites

- Ensure that you have Python 3.x installed on your machine.


# Installation


- Clone the GitHub repository or download the script files.


- Open a terminal or command prompt and navigate to the directory containing the script files.


- Install the required dependencies by running the following command:
  

`pip install configparser`


- Create a ***config.ini file*** in the same directory as the script. The file should have the following structure:

`
[Paths]
source_folder = /path/to/source/folder
destination_folder = /path/to/destination/folder `


`[Logging]
log_file = backup.log`


- Replace ***/path/to/source/folder*** with the path to the folder you want to back up and ***/path/to/destination/folder***  with the path to the folder where you want to store the backups. You can also specify a different ***log file  name***  if desired.


- Run the script by executing the following command:


`python backup_script.py`



- Follow the prompts and enter the backup passphrase when prompted.



![275358051-c1669405-a0d3-4943-8ac3-191c5c5c010d](https://github.com/0x5FE/AutomaticLocalBackup/assets/65371336/5d479b70-342c-42eb-b55d-4d528bc903b0)






# Possible Errors and Solutions


- ***Error reading configuration file:*** If you encounter an error while reading the ***config.ini file***, ensure that the file is present in the same directory as the script and that it has the correct format and structure. Check for any syntax errors or missing sections/keys in the file.


- ***Source or destination folder not specified in the configuration:*** If you see this error, make sure that you have specified the ***source_folder*** and ***destination_folder values*** in the ***config.ini file*** under the ***[Paths] section***. Double-check the paths to ensure they are correct and accessible.


- ***Source folder does not exist:*** If the script reports that the source folder does not exist, verify that the specified source folder in the config.ini file is correct and that it exists on your system. Make sure to provide the full absolute path to the folder.


- ***Backup aborted. Passphrase not provided:*** If you receive this error message, it means that you did not enter a passphrase when prompted. To resolve this, run the script again and make sure to provide a secure passphrase when prompted.


- ***Error creating backup folder:*** If the script encounters an error while creating the backup folder, ensure that the destination folder specified in the config.ini file exists and that you have the necessary permissions to create folders in that location. Check for any file system issues or restrictions that may prevent the script from creating the backup folder.

- ***Error copying file:*** If the script encounters an error while copying a file to the backup folder, it could be due to an I/O error or a permission error. Check that the source file is accessible and that you have the necessary permissions to read from it. Also, ensure that you have write permissions to the backup folder.


- ***Error during backup process:*** If an error occurs during the backup process, the script will log the error message. Check the log file specified in the config.ini file (default: backup.log) for more details on the specific error. Troubleshoot the issue based on the logged error message.

