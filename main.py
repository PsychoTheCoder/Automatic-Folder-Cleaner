# Project: Automatic Folder Cleaner
# PROGRAMMER: Psycho Coder
import os
files = os.listdir() # Return ARRAY
# ["index.html", "score.txt"]
files.remove("main.py")
def createFolder(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)


for file in files:
    print(file)
    if ".html" in file:
        print("This is HTML File")
        createFolder("HTML")
        os.replace(file, f"HTML/{file}")

    elif ".mp4" in file:
        print("This is Video File")
        createFolder("Videos")
        os.replace(file, f"Videos/{file}")

    elif ".txt" in file:
        print("This is TXT File")
        createFolder("TXT")
        os.replace(file, f"TXT/{file}")


    elif ".png" in file:
        print("This is Image File")
        createFolder("Images")
        os.replace(file, f"Images/{file}")

    elif ".py" in file:
        print("This is PYTHON File")
        createFolder("Python")
        os.replace(file, f"Python/{file}")

    elif ".docx" in file:
        print("This is Word File")
        createFolder("Word")
        os.replace(file, f"Word/{file}")
        
    elif ".zip" in file:
        print("This is ZIP File")
        createFolder("ZIP")
        os.replace(file, f"ZIP/{file}")


input()
