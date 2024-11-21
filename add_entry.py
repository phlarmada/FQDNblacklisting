import os     # Import os module for operating system-related functionality
from hosts_file_path import get_hosts_file_path     # Import function to get path of hosts file

# Get the path to the hosts file using the imported function
HOSTS_FILE_PATH = get_hosts_file_path()

def add_entry(fqdn):
    """Add a new entry to the hosts file to block the specified FQDN."""
    try:
        # Open the hosts file in append mode to add a new entry
        with open(HOSTS_FILE_PATH, 'a') as file:
            # Write entry to hosts file with format "0.0.0.0 FQDN"
            file.write(f"0.0.0.0 {fqdn}\n")  
        
        # Inform the user that the specified FQDN has been successfully blocked
        print(f"Successfully blocked {fqdn}.")
    except IOError as e:
        # Print an error message if there is an issue writing to the hosts file
        print(f"Error writing to hosts file: {e}")