import os,shutil

folders = ["Text","Music","Image"]
directory = "C:/Users/popr2/Desktop"



for i in folders:
    try:
        os.mkdir(f"C:/Users/popr2/Desktop/{i}")
    except FileExistsError:
        continue

for file in os.listdir(directory):
    _ , extension = os.path.splitext(file)
    if extension == '.txt':
        source_path = f"C:/Users/popr2/Desktop/{file}"
        dest_path = f"C:/Users/popr2/Desktop/Text/{file}"
        try:
            os.rename(source_path,dest_path)
        except FileExistsError:
            print(f"{file} already exists in Text folder.")
            ans = input("Do you want to delete the duplicate?Y/N\n")
            if ans.lower() == 'y':
                os.remove(source_path)
    elif extension == '.mp3':
        source_path = f"C:/Users/popr2/Desktop/{file}"
        dest_path = f"C:/Users/popr2/Desktop/Music/{file}"
        try:
            os.rename(source_path,dest_path)
        except FileExistsError:
            print(f"{file} already exists in Music folder")
            ans = input("Do you want to delete the duplicate?Y/N\n")
            if ans.lower() == 'y':
                os.remove(source_path)
    elif extension == '.jpg' or extension == '.png':
        source_path = f"C:/Users/popr2/Desktop/{file}"
        dest_path = f"C:/Users/popr2/Desktop/Image/{file}"
        try:
            os.rename(source_path,dest_path)
        except FileExistsError:
            print(f"{file} already exists in Image folder")
            ans = input("Do you want to delete the duplicate?Y/N\n")
            if ans.lower() == 'y':
                os.remove(source_path)