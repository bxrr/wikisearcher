import random

def read_indexes(filename):
    print()
    print(f"Reading {filename}")
    f = open(filename, "r")
    terms = []
    for line in f:
       terms.append(line.replace("\n", ""))
    return terms

def write_indexes(filename, list):
    print()
    print(f"Writing to {filename}")
    f = open(filename, "w")
    for item in list:
        f.write(item + "\n")
    f.close()
    print("Finished writing.")

def main():
    while True:
        try:
            filename = input("Enter file name.\n$ ")
            content = read_indexes(filename)
            break
        except:
            print("Invalid file name.")
    print(f"Total number of lines: {len(content)}")

    while True:
        try:
            trim_to = int(input("Enter number of lines to trim file to.\n$ "))
            if trim_to > len(content) or trim_to < 0:
                print(f"Number must be between 0 and highest line number {len(content)}")
            else:
                break
        except:
            print("Must enter a number. ")

    while True:
        mode = input("Enter 's' to remove from start, 'e' to remove from end, and 'r' to remove randomly\n$ ")
        mode = mode.lower()
        if mode == "s" or mode == "r" or mode == "e":
            break
        else:
            print("Invalid letter.")

    print(abs(trim_to - len(content)))
    for i in range(abs(trim_to - len(content))):
        if mode == "s":
            content.pop(i)
        if mode == "e":
            content.pop(len(content)-1)
        if mode == "r":
            content.pop(random.randint(0, len(content)-1))

    write_indexes(filename, content)

if __name__ == "__main__":
    main()