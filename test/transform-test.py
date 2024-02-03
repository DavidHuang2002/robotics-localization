
import sys
import os


# set up for test - allow for import from parent directory
# so that I can import modules from the parent directory (like calc_orientation.py)
def add_parent_dir_to_path():
    """Add the parent directory of the script to sys.path."""
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
    parent_dir = os.path.dirname(script_dir)  # Parent directory
    sys.path.append(parent_dir)

add_parent_dir_to_path()
