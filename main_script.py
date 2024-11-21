import os                                       # Import os module for operating system-related functionality
import sys                                      # Import sys to access system-specific parameters and functions
import argparse                                 # Import argparse to handle command-line arguments
from check_if_exists import check_if_exists     # Import function to check if FQDN exists in hosts file
from add_entry import add_entry                 # Import function to add entry to hosts file
from delete_entry import delete_entry           # Import function to delete entry from hosts file
from modify_entry import modify_entry           # Import function to modify existing entry in hosts file

def is_admin():
    """Check if the script is run with administrative privileges."""
    try:
        if os.name == 'nt':     # Check for Windows OS
            import ctypes     # Import ctypes for Windows API
            return ctypes.windll.shell32.IsUserAnAdmin() != 0     # Check if user is admin
        else:     # For Unix systems
            return os.geteuid() == 0     # Check if effective user ID is 0 (root)
    except AttributeError:
        return False     # Return False if issue checking admin status

def main():
    """Main function to run the FQDN blocker."""
    # Mapping actions to their functions
    actions = {
        'check': check_if_exists,
        'block': add_entry,
        'delete': delete_entry,
        'modify': modify_entry
    }

    # Check if action is valid
    if args.action in actions:
        if args.action == 'check':
            # Call function to check if the FQDN exists
            exists = actions[args.action](args.fqdn)
            if exists:
                print(f"The entry for {args.fqdn} already exists.")     # Entry exists
            else:
                print(f"The entry for {args.fqdn} does not exist.")     # Entry doesn't exist
        else:
            # If action isn't 'check', verify if the FQDN exists
            if check_if_exists(args.fqdn):
                if args.action == 'block':
                    print(f"The entry for {args.fqdn} already exists.")     # Blocking Entry already exists
                else:
                    actions[args.action](args.fqdn)     # Call delete or modify function
            else:
                if args.action == 'block':
                    actions[args.action](args.fqdn)     # Call block function if the entry doesn't exist
                else:
                    print(f"The entry for {args.fqdn} doesn't exist.")     # Entry doesn't exist for delete/modify
    else:
        print("Invalid action. Please use 'block', 'delete', 'modify', or 'check'.")     # Invalid action provided

if __name__ == "__main__":
    # Check script is run with administrative privileges
    if not is_admin():
        print("This script requires administrative privileges. Please run as an administrator.")
        sys.exit(1)  # Exit if not administrator
    
    parser = argparse.ArgumentParser(description='Block, delete, or modify a FQDN in the hosts file.')     # Set up argument parsing
    parser.add_argument('action', choices=['block', 'delete', 'modify', 'check'], help="Action to perform on FQDN.")     # Define action argument with choices
    parser.add_argument('fqdn', help="Fully Qualified Domain Name to process.")     # Define FQDN argument
    
    args = parser.parse_args()     # Parse command-line arguments
    main()     # Call main function