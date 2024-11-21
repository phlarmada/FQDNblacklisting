import os     # Import os module for operating system-related functionality
from hosts_file_path import get_hosts_file_path     # Import function to get path of hosts file

# Get the path to the hosts file using the imported function
HOSTS_FILE_PATH = get_hosts_file_path()

def check_if_exists(fqdn):
    """Check if the given FQDN already exists in the hosts file."""
    try:
        # Open the hosts file in read mode to check for the FQDN
        with open(HOSTS_FILE_PATH, 'r') as file:
            # Iterate through each line in the hosts file
            for line in file:
                if fqdn in line:     # Check if the FQDN is present in the current line
                    return True     # Return True if the FQDN is found in the file
    except IOError as e:
        # Print an error message if there is an issue reading the hosts file
        print(f"Error reading hosts file: {e}")
    
    return False     # Return False if the FQDN isn't found in the file