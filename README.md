# FQDN Blacklisting

FQDN Blacklisting is a simple Python utility for managing entries in the system's hosts file. This tool allows you to block specific Fully Qualified Domain Names (FQDNs) by adding, modifying, or deleting entries in the hosts file.

## Features

- **Add entries** to block FQDNs.
- **Check** if an FQDN already exists in the hosts file.
- **Modify** existing entries in the hosts file.
- **Delete** entries from the hosts file.
- Automatically determine the correct path to the hosts file based on the operating system (Windows, Linux, macOS).

## Modules

### 1. `hosts_file_path.py`
This module contains a function to retrieve the path to the hosts file based on the operating system.
- **Functions**:
  - `get_hosts_file_path()`: Returns the file path of the hosts file.
    - **Returns**:
      - For Windows: `C:\Windows\System32\drivers\etc\hosts`
      - For Linux/macOS: `/etc/hosts`

### 2. `add_entry.py`
This module provides functionality to add a new entry to the hosts file to block a specified FQDN.
- **Functions**:
  - `add_entry(fqdn)`: Adds a new entry to the hosts file.
    - **Parameters**:
      - `fqdn`: The Fully Qualified Domain Name to be blocked.
    - **Returns**:
      - Prints a success message if the entry is added successfully.
      - Prints an error message if there is an issue writing to the hosts file.

### 3. `check_if_exists.py`
This module allows you to check if a specific FQDN already exists in the hosts file.
- **Functions**:
  - `check_if_exists(fqdn)`: Checks if the given FQDN is already present in the hosts file.
    - **Parameters**:
      - `fqdn`: The Fully Qualified Domain Name to check.
    - **Returns**:
      - `True` if the FQDN exists in the hosts file.
      - `False` if it does not exist.
      - Prints an error message if there is an issue reading the hosts file.

### 4. `delete_entry.py`
This module provides functionality to remove an existing entry from the hosts file.
- **Functions**:
  - `delete_entry(fqdn)`: Deletes an entry for the specified FQDN from the hosts file.
    - **Parameters**:
      - `fqdn`: The Fully Qualified Domain Name to be removed.
    - **Returns**:
      - Prints a success message if the entry is deleted successfully.
      - Prints an error message if there is an issue writing to the hosts file.

### 5. `modify_entry.py`
This module allows you to modify an existing entry in the hosts file.
- **Functions**:
  - `modify_entry(old_fqdn, new_fqdn)`: Modifies an existing entry in the hosts file.
    - **Parameters**:
      - `old_fqdn`: The Fully Qualified Domain Name to be modified.
      - `new_fqdn`: The new Fully Qualified Domain Name to replace the old one.
    - **Returns**:
      - Prints a success message if the entry is modified successfully.
      - Prints an error message if there is an issue writing to the hosts file.

### 6. `main_script.py`
This module serves as the entry point for the application, allowing users to interact with the hosts file through a command-line interface.
- **Functions**:
  - `is_admin()`: Checks if the script is run with administrative privileges.
    - **Returns**:
      - `True` if the user has administrative privileges.
      - `False` if the user does not have administrative privileges.
  - `main()`: The main function that handles user input and calls the appropriate functions to manage the hosts file.
    - **Behavior**:
      - Maps user-specified actions (block, delete, modify, check) to their corresponding functions.
      - Validates the provided action and checks if the specified FQDN exists in the hosts file before proceeding with the requested action.
      - Prints appropriate messages based on the outcome of the actions.

## Command-Line Usage

The script requires administrative privileges to modify the hosts file. To run the script, use the following command:

```bash
python main_script.py <action> <fqdn>
```

## Requirements
- Python 3.x

## Author
Adam Ralph
