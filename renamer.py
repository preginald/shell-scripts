import os
import argparse
import logging

# Setting up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def looper(search, replace):
    """
    This function loops through all files and directories in the current working directory
    and calls the appropriate function to rename them. If the item is a file, it calls the
    file_renamer function, if the item is a directory, it calls the dir_renamer function.
    """
    for filename in os.listdir():
        if os.path.isfile(filename):
            file_renamer(filename, search, replace)
        if os.path.isdir(filename):
            logging.info(f"{filename} is a directory")
            try:
                dir_name = dir_renamer(filename, search, replace)
                os.chdir(dir_name)
                looper(search, replace)
                os.chdir("..")
            except Exception as e:
                logging.error(f"Error occured while renaming directory {filename}: {e}")

def dir_renamer(file, _search, _replace):
    """
    This function renames a directory by replacing the search string with the replace string.
    """
    try:
        new_filename = file.replace(_search, _replace)
        os.rename(file, new_filename)
        logging.info(f"{new_filename} renamed")
    except Exception as e:
        logging.error(f"Error occured while renaming {file}: {e}")
    return new_filename

def file_renamer(file, _search, _replace):
    """
    This function renames a file by replacing the search string with the replace string.
    """
    _, file_extension = os.path.splitext(file)
    if file_extension in [".mp4", ".wmv", ".mov"]:
        try:
            new_filename = file.replace(_search, _replace)
            os.rename(file, new_filename)
            logging.info(f"{new_filename} renamed")
        except Exception as e:
            logging.error(f"Error occured while renaming {file}: {e}")

def main():
    """
    This function sets up the argparse and call the looper function to start renaming
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("search", type=str, help="the string to search for in filenames")
    parser.add_argument("replace", type=str, help="the string to replace the search string with")
    args = parser.parse_args()
    looper(args.search, args.replace)

if __name__ == "__main__":
    main()
