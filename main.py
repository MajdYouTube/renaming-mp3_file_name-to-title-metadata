import os
import win32com.client
def renamer(folderpath, musicfile):
    sh=win32com.client.gencache.EnsureDispatch('Shell.Application',0)
    ns = sh.NameSpace(folderpath)
    colnum = 0
    columns = []
    while True:
        colname=ns.GetDetailsOf(None, colnum)
        if not colname:
            break
        columns.append(colname)
        colnum += 1
    found = None
    newname = None
    for item in ns.Items():
        for colnum in range(len(columns)):
            colval=ns.GetDetailsOf(item, colnum)
            if colval:
                if(colval == musicfile):
                    found =  item.Path
                if(columns[colnum] == "Title" and found != None):
                    newname = colval
                    os.renames(item.Path, folderpath + "\\" + newname + ".mp3")
                    found = None
                    newname = None
                    print("done")

while(True):
    folderpath = r'C:\Users\DELL\Desktop\audios\osu' #place the folder path where you want to change the name of the music file inside it to it's title
    musicfile = "audio.mp3" #place the name of the music files that you want to change
    renamer(folderpath, musicfile)