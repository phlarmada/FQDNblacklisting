import os     # Import the os module for operating system-related functionality

def get_hosts_file_path():
    """Return the file path of the hosts file based on the operating system."""
    if os.name == 'nt':     # Check for Windows OS
        return "C:\\Windows\\System32\\drivers\\etc\\hosts"  # Return path for Windows hosts file
    else:     # For Linux and macOS
        return "/etc/hosts"     # Return path for Linux/macOS hosts file