import shutil
import os
import datetime
import logging
import configparser
import getpass  

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Error reading configuration file: {str(e)}")
    exit(1)

def backup_files(source, destination, log_file):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(destination, f"backup_{timestamp}")

    try:
        os.makedirs(backup_folder, mode=0o700)  
    except OSError as e:
        logging.error(f"Error creating backup folder: {str(e)}")
        return

    try:
        for root, dirs, files in os.walk(source):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(backup_folder, os.path.relpath(source_path, source))

                try:
                    shutil.copy2(source_path, destination_path)
                    logging.info(f"File '{source_path}' copied to '{destination_path}'")
                except (IOError, PermissionError) as e:
                    logging.error(f"Error copying file '{source_path}' to '{destination_path}': {str(e)}")
    except Exception as e:
        logging.error(f"Error during backup process: {str(e)}")

    logging.info("Backup completed successfully!")

if __name__ == "__main__":
    source_folder = config.get('Paths', 'source_folder', fallback=None)
    destination_folder = config.get('Paths', 'destination_folder', fallback=None)
    log_file = config.get('Logging', 'log_file', fallback='backup.log')

    if not source_folder or not destination_folder:
        logging.error("Source or destination folder not specified in the configuration.")
    else:
        # Set up logging
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        if os.path.exists(source_folder):
            # Prompt for a secure passphrase before initiating the backup
            passphrase = getpass.getpass(prompt="Enter backup passphrase: ")
            if passphrase:  # Check if a passphrase was provided
                # Perform the backup
                backup_files(source_folder, destination_folder, log_file)
            else:
                logging.error("Backup aborted. Passphrase not provided.")
        else:
            logging.error(f"Source folder '{source_folder}' does not exist. Backup aborted.")
