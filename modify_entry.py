from delete_entry import delete_entry     # Import function to delete entry from hosts file
from add_entry import add_entry     # Import function to modify existing entry in hosts file

def modify_entry(fqdn):
    """Modify the specified FQDN entry in the hosts file."""
    delete_entry(fqdn)     # Delete the old entry
    add_entry(fqdn)        # Add the new entry