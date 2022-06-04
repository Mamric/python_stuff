from os import scandir, mkdir, path
from shutil import move


def main():
    """This function goes through a dir and organizes the files in terms of extensions. Example: list.txt goes into the TXTs dir, leads.xlsx goes into the XLSXs dir, etc


    Returns:
        Boolean: either returns 1 if successfully run or 0 if an error is thrown

    Known bugs: Program will crash if trying to copy files with same name such as "download.jpg" to JPGs dir
    """
    # DIR_TO_SCAN = "/Users/nicky/Desktop"
    INPUT_TEXT = "Enter directory to scan: \n example: \"/Users/USER/Desktop\"\nPath: "
    DIR_TO_SCAN = input(INPUT_TEXT)
    if not path.isdir(DIR_TO_SCAN):  # check if path is or isn't valid
        print("ERROR: PATH NOT FOUND! EXITING.")
        return 0
    with scandir(DIR_TO_SCAN) as entries:
        for entry in entries:
            # makes sure the file is a file and not a temp file/hidden
            if(entry.is_file() and not is_hidden_or_temp(entry.name)):
                ext = entry.name.split(".")[-1].upper()+"s"
                FILE_PATH = DIR_TO_SCAN + "/" + entry.name  # full file path of original file
                EXT_PATH = DIR_TO_SCAN + "/__" + ext  # full dir path of extension
                if(not path.isdir(EXT_PATH)):  # if the dir doesn't exist, make it
                    print(EXT_PATH + " DOES NOT EXIST! CREATING NOW!")
                    mkdir(EXT_PATH)
                move(FILE_PATH, EXT_PATH)  # make the move!
                print(entry.name + " has been moved successfully!")
    print("DONE!")
    return 1


def is_hidden_or_temp(filename):
    """ Function to check if a file is hidden or a temp file

    Args:
        filename (string): file name to check

    Returns:
        Boolean: True if the file name is hidden/temp and False if not
    """
    if filename[0] is "~":
        return True
    elif filename == "desktop.ini":
        return True
    else:
        return False


# basic python line thing
if __name__ == "__main__":
    main()
