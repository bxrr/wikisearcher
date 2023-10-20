import random

def read_indexes(filename):
    print(f"Reading {filename}")
    f = open(filename, "r")
    terms = []
    for line in f:
        if(line != "\n"):
            temp = line.replace("'", "").replace("\"", "")
            terms.append(temp)
    return terms

def write_indexes(filename, list):
    print(f"Writing to {filename}")
    f = open(filename, "w")
    for item in list:
        f.write(item)
    f.close()
    print("Finished writing.")

def trim(filename):
    print("Removing whitespace.")
    try:
        content = read_indexes(filename)
    except Exception as e:
        print(e)
        return

    write_indexes(filename, content)

if __name__ == "__main__":
    trim(input("filename: "))