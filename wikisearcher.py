import wikipedia
import random
import os
from datetime import datetime


PARENT_DIR = os.getcwd()

ERR_DIR = "Not Found"
ERR_PATH = os.path.join(PARENT_DIR, ERR_DIR)

LOAD_DIR = "Load Files"
LOAD_PATH = os.path.join(PARENT_DIR, LOAD_DIR)

OUTPUT_DIR = "Output"
OUTPUT_PATH = os.path.join(PARENT_DIR, OUTPUT_DIR)

try:
    os.makedirs(ERR_PATH)
except:
    pass

try:
    os.makedirs(LOAD_PATH)
except:
    pass

try:
    os.makedirs(OUTPUT_PATH)
except:
    pass

 
def get_indexes(filename):
    print()
    count = 1
    f = open(os.path.join(LOAD_PATH, filename), "w")
    terms = []
    print("Enter all terms to search.\n"
        + "Type 'exit' or 'x' to exit the file.")
    while True:
        user_input = input(f"{count}. ")
        if user_input.lower() == "exit" or user_input.lower() == "x":
            break
        else:
            count += 1
            terms.append(user_input)
            f.write(user_input + "\n")
    f.close()
    return terms

def read_indexes(filename):
    print()
    print(f"Reading {filename}")
    f = open(filename, "r")
    terms = []
    for line in f:
        line = line.encode("ascii", "ignore")
        line = line.decode()
        terms.append(line.replace("\n", ""))
    return terms
 

def give_definition(term_name):
    try:        
        print(f"\nFinding info for {term_name}" + ("." * (65 - len(term_name))), end="", flush=True)
        definition = ""
        definition = wikipedia.summary(term_name, sentences=3)
        start_paren = ""
        end_paren = ""
        while(start_paren != -1):
            start_paren = definition.find("(")
            end_paren = definition.find(")")
            definition = definition.replace(definition[start_paren:end_paren+1], "") 
            definition = definition [:start_paren] + " " + definition[start_paren:]
        print("Found", end=" | ")
        definition = definition.replace("  ", "").replace(" ,", ",").replace(" .", ". ").replace(".", ". ").replace(".  ", ". ").replace("\n", "")
        return definition
    except:
        print("Not Found", end=" | ")
        return -1
 

def list_definition(term_list, savefile):
    vocab_dict = {}
    missing = []
    for term in term_list:
        definition = give_definition(term)
        if definition != -1:
            vocab_dict.update({term: definition})
        else:
            missing.append(term)

    if len(missing) > 0:
        print(f"\n\n{len(missing)} terms could not be found.")
        filename = savefile.replace(savefile[savefile.rfind("."):], "") + "{:05d}".format(random.randint(0, 99999)) + "-" + datetime.now().strftime("%m%d") + ".txt"
        f = open(os.path.join(ERR_PATH, filename), "w")
        for term in missing:
            f.write(term + "\n")
        f.close()
        print(f"Missing terms have been written to: {os.path.join(ERR_DIR, filename)}")
    return vocab_dict
 

def write_to_file(filename, dictionary):
    print(f"Writing {len(dictionary.keys())} items to file: {os.path.join(LOAD_DIR, filename)}")
    terms = list(dictionary.keys())
    definitions = list(dictionary.values())
    
    f = open(os.path.join(OUTPUT_PATH, filename), "w") 
    for i in range(len(dictionary)):
        f.write(terms[i] + ": " + definitions[i] + "\n\n")
    f.close()
    print(f"Finished writing.")
 

def read_file(filename):
    terms = []
    f = open(os.path.join(LOAD_PATH, filename), "r")
    for line in f:
        if line != " " and line != "\n":
            terms.append(line.replace("\n", "").replace("  ", ""))
    return terms


def print_file_error(more_text=""):
    print("File name can not include special characters. " + more_text + "\n")
 

def main():
    while(True):
        while(True):
            print("\n" * 50)
            print("WIKI SEARCHER. Files with terms must be formatted with one term per line.")
            print("load files by typing 'l'. Type 'w' to write to a new file.\n"
                + "Type 'x' to quit the program at any time.")
            load = input("$ ")
            print()
            if load.lower() == "l":
                while True:
                    try:
                        user_input = input("Enter a file name to read.\n$ ")
                        if user_input.lower() == "x":
                            quit()
                        terms = read_file(user_input)
                        break
                    except SystemExit:
                        quit()
                    except:
                        print_file_error("Possibly no existing file with that name.")
                break
            elif load.lower() == "w":
                while True:
                    try:
                        user_input = input("Enter a file name to write to.\n$ ")
                        if user_input.lower() == "x":
                            quit()
                        terms = get_indexes(user_input)
                        break
                    except SystemExit:
                        quit()
                    except:
                        print_file_error()
                break
            elif load.lower() == "x":
                exit()
            else:
                print("Invalid input.")
                continue

        print()
        while True:
            try:
                savefile = input("Enter a file to save definitions to.\n$ ")
                if savefile.lower() == "x":
                    quit()
                f = open(os.path.join(OUTPUT_PATH, savefile), "w")
                f.close()
                break
            except SystemExit:
                quit()
            except:
                print_file_error()
        terms_and_def = list_definition(terms, savefile)
        print()
        write_to_file(savefile, terms_and_def)
        print()
        user_input = input("Press enter to continue. ")
        if user_input.lower() == "x":
            quit()
 

if __name__ == "__main__":
    main()