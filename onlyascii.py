def del_non_ascii(string):
    for i in range(len(string)):
        if ord(string[i]) > 128:
            string = string.replace(string[i], "")
    return string

def check_file(filename):
    removed = []
    f = open(filename, "r")
    for line in f:
        removed.append(del_non_ascii(line))
    return removed

def write_to_file(line_list, write_file):
    f = open(write_file, "w")
    for element in line_list:
        f.write(element)

def main():
    file_name = input("Enter file name: ")
    write_file = input("Enter file to write to: ")
    write_to_file(check_file(file_name), write_file)

if __name__ == "__main__":
    main()