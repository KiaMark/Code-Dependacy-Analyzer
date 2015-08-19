import os
size = 0

def folderOpen(folder):
    #relativePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", folder))
    for content in os.listdir(folder):
        # Check if it is a hidden file (.foo), ignore if it is
        if content[0] == '.':
            print("Skipping empty file: " + content)
        else:
            # You need to create the full path name before checking
            fullPath = os.path.join(folder, content)
            ext = os.path.splitext(content)[-1].lower()
            #print("Processing fullpath: " + fullPath)

            if ext == ".h":
                #print(content, "is .h!")
                header(fullPath)
            elif ext == ".m":
                #print(content, "is .m!")
                header(fullPath)
            elif os.path.isdir(fullPath):
                #print(content, "is a folder!")
                folderOpen(fullPath)
            else:
                print(content, "is a file, but not .h or .m!")

def header(folder):
    print(folder, "in header!")
    file = open(folder, 'r')
    read = file.readlines()
    file.close()
    for line in read:
        if str("import") in line:
            print(line)

folder = input("Input folder name: ")
folderOpen(folder)