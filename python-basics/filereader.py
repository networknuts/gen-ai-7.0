file_path = input("Enter the file name or path to read: ")

f = open(file_path,"r")

for line in f.readlines():
    print(line.strip())

f.close()