import os

<<<<<<< HEAD
def folderOpen(folder):
    relativePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", folder))
    for content in os.listdir(folder):
=======
# for fp in os.listdir(file):
#    print(fp)
#    ext = os.path.splitext(fp)[-1].lower()
#    if ext == ".framework":
#        print(fp, "is .framwork!")

def folderOpen(folder):
    relativePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", folder))
    for content in os.listdir(relativePath):
>>>>>>> origin/master
        # Check if it is a hidden file (.foo), ignore if it is
        if content[0] == '.':
            print("Skipping empty file: " + content)
        else:
            # You need to create the full path name before checking
<<<<<<< HEAD
            fullPath = os.path.join(folder, content)
            ext = os.path.splitext(content)[-1].lower()

            #print("Processing fullpath: " + fullPath)
=======
            fullPath = os.path.join(relativePath, folder, content)
            ext      = os.path.splitext(content)[-1].lower()

            print("Processing fullpath: " + fullPath)
>>>>>>> origin/master

            if ext == ".h":
                print(content, "is .h!")
                header(content)
<<<<<<< HEAD
            elif ext == ".m":
                print(content, "is .m!")
                header(content)
            elif os.path.isfile(fullPath):
                print(content, "is a file, but not .h or .m!")
            elif os.path.isdir(fullPath):
                print(content, "is a folder!")
                folderOpen(fullPath)
            else:
                print("hurr durr")
                folderOpen(fullPath)
=======
            elif os.path.isfile(fullPath):
                print(content, "is a file, but not .h!")
            elif os.path.isdir(fullPath):
                print(content, "is a folder!")
                folderOpen(content)
            else:
                print("hurr durr")
>>>>>>> origin/master

def header(folder):
    print(folder, "in header!")

folder = input("Input folder name: ")
folderOpen(folder)