#this is was for my practice, pls do check organizer.py for actual code 
import os
import shutil

photo=0
doc=0
video=0
audio=0
other=0

main=r"D:\Trash"
items=os.listdir(main)

for item in items:
    if item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg"):
        if(not os.path.exists(r"D:\Trash\Photos")):
            os.makedirs(r"D:\Trash\Photos")
        item_path="D:/Trash/"+item
        shutil.move(item_path, r"D:\Trash\Photos")
        print("Photo Moved")
        photo+=1

    elif item.endswith(".pdf") or item.endswith(".docx"):
        if(not os.path.exists(r"D:\Trash\Documents")):
            os.makedirs(r"D:\Trash\Documents")
        item_path="D:/Trash/"+item
        shutil.move(item_path, r"D:\Trash\Documents")
        print("Document File Moved")
        doc+=1

    elif item.endswith(".mp4"):
        if(not os.path.exists(r"D:\Trash\Videos")):
            os.makedirs(r"D:\Trash\Videos")
        item_path="D:/Trash/"+item
        shutil.move(item_path, r"D:\Trash\Videos")
        print("Video Moved")
        video+=1

    elif item.endswith(".mp3"):
        if(not os.path.exists(r"D:\Trash\Audios")):
            os.makedirs(r"D:\Trash\Audios")
        item_path="D:/Trash/"+item
        shutil.move(item_path, r"D:\Trash\Audios")
        print("Audio file Moved")
        audio+=1

    else:
        if(not os.path.exists(r"D:\Trash\Others")):
            os.makedirs(r"D:\Trash\Others")
        item_path="D:/Trash/"+item
        shutil.move(item_path, r"D:\Trash\Others")
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


    

    
