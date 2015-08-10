import os

folder = input("Input folder name: ")

# for fp in os.listdir(file):
#    print(fp)
#    ext = os.path.splitext(fp)[-1].lower()
#    if ext == ".framework":
#        print(fp, "is .framwork!")

def folderOpen(folder):
    for content in os.listdir(folder):
        ext = os.path.splitext(content)[-1].lower()
        if ext == ".h":
            print(content, "is .h!")
            header(content)
        elif os.path.isfile(content):
            print(content, "is a file, but not .h!")
        else:
            print(content, "is a folder!")
            folderOpen(content)


def header(folder):
    print(folder, "in header!")

folderOpen(folder)