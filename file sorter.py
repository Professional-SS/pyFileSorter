
import os,shutil

path  = "/Users/path"
folder_names = ['pdf files','video files','image files','js files',"text files"]
file_name = os.listdir(path)

for loop in range(0,5):
    if not os.path.exists(path + folder_names[loop]):
        print(path +folder_names[loop])
        os.mkdir(path +folder_names[loop])

for file in file_name:
    if ".pdf" in file and not os.path.exists(path +"pdf files/"+ file):
        shutil.move(path+file, path+"pdf files/"+file)
    elif ".png" in file and not os.path.exists(path+"image files/"+file):
       shutil.move(path+file, path+"image files/"+file)
    elif ".jpeg" in file and not os.path.exists(path+"image files/"+file):
       shutil.move(path+file, path+"image files/"+file)
    elif ".mov" in file and not os.path.exists(path+"video files/"+file):
       shutil.move(path+file, path+"video files/"+file)
    elif ".txt" in file and not os.path.exists(path+"text files/"+file):
       shutil.move(path+file, path+"text files/"+file)
    elif ".js" in file and not os.path.exists(path+"js files/"+file):
       shutil.move(path+file, path+"js files/"+file)