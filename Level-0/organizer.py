import os
import shutil
import pathlib

photo=0
doc=0
video=0
audio=0
other=0

cwd = pathlib.Path.cwd()
items=os.listdir(cwd)


for item in items:
    if item.endswith((".jpg", ".png", ".jpeg")):
        if(not os.path.exists(r"Photos")):
            os.makedirs(r"Photos")
        shutil.move(item, r"Photos")
        print("Photo Moved")
        photo+=1

    elif item.endswith(".pdf") or item.endswith(".docx"):
        if(not os.path.exists(r"Documents")):
            os.makedirs(r"Documents")
        shutil.move(item, r"Documents")
        print("Document File Moved")
        doc+=1

    elif item.endswith(".mp4"):
        if(not os.path.exists(r"Videos")):
            os.makedirs(r"Videos")
        shutil.move(item, r"Videos")
        print("Video Moved")
        video+=1

    elif item.endswith(".mp3"):
        if(not os.path.exists(r"Audios")):
            os.makedirs(r"Audios")
        shutil.move(item, r"Audios")
        print("Audio file Moved")
        audio+=1

    elif item.endswith((".py", ".cpp", ".html", ".json", ".css", ".js", ".md")):
        if(not os.path.exists(r"Audios")):
            os.makedirs(r"Audios")
        shutil.move(item, r"Audios")
        print("Audio file Moved")
        audio+=1
    

    else:
        if(not os.path.exists(r"Others")):
            os.makedirs(r"Others")
        shutil.move(item, r"Others")
        print("Other file Moved")
        other+=1

print("==========================================")
print("               Final Report               ")
print("------------------------------------------")
print("Total File moved ", photo+doc+video+audio+other)
print("Total Photos moved", photo)
print("Total Documents moved",doc)
print("Total Videos moved",video)
print("Total Audios moved",audio)
print("Other files moved",other)
print("==========================================")



    