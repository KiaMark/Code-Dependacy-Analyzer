import os

fileSize = 0
hSize = 0
mSize = 0
swiftSize = 0
importSize = 0
skipFile = 0
random = 0

def folderOpen(folder):
    global fileSize
    global hSize
    global mSize
    global swiftSize
    global skipFile
    global random
    #relativePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", folder))
    for content in os.listdir(folder):
        if content[0] == '.':
            skipFile = skipFile + 1
            #print("Skipping empty file: " + content)
        else:
            fullPath = os.path.join(folder, content)
            ext = os.path.splitext(content)[-1].lower()
            if ext == ".h":
                header(fullPath)
                fileSize = fileSize + 1
                hSize = hSize + 1
            elif ext == ".m":
                header(fullPath)
                fileSize = fileSize + 1
                mSize = mSize + 1
            elif ext == ".swift":
                header(fullPath)
                fileSize = fileSize + 1
                swiftSize = swiftSize + 1
            elif os.path.isdir(fullPath):
                folderOpen(fullPath)
            else:
                fileSize = fileSize + 1
                random = random + 1

def header(folder):
    global importSize
    file = open(folder, 'r')
    read = file.readlines()
    file.close()
    for line in read:
        if str("import") in line:
            importSize = importSize + 1


print("Hello User!")
print("1-Project statistics")
print("2-Unnecessary import statements")
print("3-Unused import statements")
print("4-Redundant import statements")
print("5-Import statement counts")
choice = int(input("Select an option:"))
if choice == 1:
    folderOpen(input("Input folder name: "))
    print("Number of file(s): ", fileSize)
    print("Number of .h file(s): ", hSize)
    print("Number of .m file(s): ", mSize)
    print("Number of .swift file(s): ", swiftSize)
    print("Number of skipped empty file(s): ", skipFile)
    print("Number of random file(s): ", random)
if choice == 2:
    print("Option 2 selected")
if choice == 3:
    print("Option 3 selected")
if choice == 4:
    print("Option 4 selected")
if choice == 5:
    folderOpen(input("Input folder name: "))
    print("Total number of import(s): ", importSize)