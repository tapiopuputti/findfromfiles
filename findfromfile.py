import os
import re

class colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m' # end colors


# Function to list files and return list of filenames inside the given directory
def list_files(path:str) -> list:
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files
    except FileNotFoundError:
        pass # This error is handled inside search_text()-function
        # print("Invalid path, please try again.")
    # # Comment next except to find out details of error (TODO: print error details always, handle all errors?)
    except:
        print(f"Unhandled error: {os.error}")

# Search text inside files in the given directory
def search_text(keyword:str, path:str):
    # Make a list of all files in the directory
    files = list_files(path)
    results = []
    try:
        # Search for keyword in files
        for filename in files:
            absolutefilepath = os.path.join(path, filename)
            f = open(absolutefilepath, 'r',  encoding="utf-8") # TODO: with open
            text = f.read() 
            # print('\nINSPECTING FILE: ' + path + filename) 
            # print(text)
            matches = re.findall(keyword, text)
            # If there are matches, append them to results
            if len(matches) > 0:
                results.append([filename, len(matches)])

        # Print how many files have been searched through and what was the keyword
        print(f"\nSearched through {colors.BOLD}{colors.YELLOW}{len(files)}{colors.END} files for keyword '{colors.GREEN}{colors.UNDERLINE}{keyword}{colors.END}' in path '{colors.GREEN}{colors.UNDERLINE}{path}{colors.END}'")

        # Print which files contain the keywords and how many times and add number of hits to total_occurrences
        total_occurrences = 0
        for item in results:
            total_occurrences += item[1]
            if item[1] == 1:
                print(f"{colors.RED}{item[1]:4}{colors.END} hit  in file '{colors.BOLD}{item[0]}{colors.END}'")
            else:
                print(f"{colors.RED}{item[1]:4}{colors.END} hits in file '{colors.BOLD}{item[0]}{colors.END}'")

        # Print total occurrences
        print(f"\n{colors.MAGENTA}{total_occurrences:4}{colors.END} total occurrences in {colors.BOLD}{colors.YELLOW}{len(results)}{colors.END} file(s).")

    # Handle errors
    except IOError:
        print('\nProblem reading: ' + filename)
    except TypeError:
        print("\nInvalid path, please try again.")
    except UnicodeDecodeError:
        print("\nDecode error, file " + filename + " probably not a text file.")
    # Comment next except to find out details of error (TODO: print error details always, handle all errors?)
    except:
        print(f"Unhandled error, filename '{filename}', error: {os.error}")
    


# Function to ask user for keyword and directory
# TODO: validate proper string for directory
def user_input():
    path = input("Give the folder to search in (Enter = current directory): ")
    if path == '':
        path = "./"
    keyword = input("Give the desired string to search: ")
    search_text(keyword, path)


if __name__ == "__main__": 
    user_input()

# TODO: search subdirectories (ask it y/n?) os.walk
# TODO: detect if file is non-text and skip it