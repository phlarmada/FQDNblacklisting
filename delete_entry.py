import os     # Import os module for operating system-related functionality
from hosts_file_path import get_hosts_file_path     # Import function to get path of hosts file

# Get the path to the hosts file using the imported function
HOSTS_FILE_PATH = get_hosts_file_path()

def delete_entry(fqdn):
    """Delete the specified FQDN entry from the hosts file."""
    try:
        # Open the hosts file in read mode to retrieve its contents
        with open(HOSTS_FILE_PATH, 'r') as file:
            lines = file.readlines()     # Read all lines from file into list
        
        # Open the hosts file in write mode to modify its contents
        with open(HOSTS_FILE_PATH, 'w') as file:
            for line in lines:
                # Check if the current line doesn't contain the specified FQDN
                if fqdn not in line:
                    file.write(line)     # Write back the line to the file if it doesn't contain the FQDN
        
        # Inform the user that the specified FQDN was successfully removed
        print(f"Successfully removed {fqdn} from hosts file.")
    except IOError as e:
        # Print an error message if there is an issue modifying the hosts file
        print(f"Error modifying hosts file: {e}")