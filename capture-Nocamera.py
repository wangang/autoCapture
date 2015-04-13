# -*- coding: utf-8 -*-
#from VideoCapture import Device 
import os
import time
import Tkinter,tkFileDialog
root = Tkinter.Tk()

#cam = Device(devnum=0, showVideoWindow=0) 
print 'I am checking files...'

timeSpan = 1 #Frequency to check the file

## this is for the camera setting
timestamp = 3 #the time stamp on the photo
boldfont = 1 #the bold font of the stamp
quality = 1000 #quality of the photo



#cam.saveSnapshot('image.jpg', timestamp=timestamp, boldfont=boldfont, quality=quality)  
path = tkFileDialog.askdirectory(initialdir = 'C:/')
root.destroy()
print path
#print 'C:/Users/wangang/Desktop/新建文件夹'
#path = 'C:/Users/wangang/Desktop/新建文件夹'
newPath = path + '/' + 'CaptureData'
if not os.path.isdir(newPath):
    os.mkdir(newPath)    

fileDictionary = os.listdir(path)
newFilename = []


def isdirExist(fileDir):
    if os.apth.isdir(fileDir):
        return True
    else:
        return False
    
def isnewFile(files):
    global newFilename
    a = False
    for i in files:
        if os.path.isfile(path+'/'+i):
            if i not in fileDictionary:
                fileDictionary.append(i)
                #fileDictionary = files
                #newFilename = i.split('.')
                newFilename = i
                a = True
                break
    return a
            
    
def findFiles(path):
    if os.path.exists(path):
        files = os.listdir(path)
        if isnewFile(files):
            print "It's a new file."
            #print 'newFile:%s'%newFile.name
            #os.mkdir(path + '/' + newFile )
            #print 'fileDictionary:%s'%fileDictionary
            #folderPath = path + '/' + newFilename[0]
            #print folderPath
            #os.mkdir(folderPath)
            #filePath = folderPath + '/' + '%s.txt'%newFilename[0]
            #photoPath = folderPath + '/' + '%s.jpg'%newFilename[0]
            # filePath = path + '/' + newFile + '/' + '%s.txt'%newFile
            # photoPath = path + '/' + newFile + '/' + '%s.jpg'%newFile
            #print 'filePath:%s'%filePath
            filePath = newPath + '/' + '%s.txt'%newFilename
            photoPath = newPath + '/' + '%s.jpg'%newFilename
            f = open(filePath,'w')
            f.write('Test')
            #f.write("保存路径：" + photoPath + "\n")
            #f.write("时间戳大小：" + str(timestamp) + '\n' )
            #f.write("字体大小" + str(boldfont) + '\n' )
            f.close()
            #cam.saveSnapshot(photoPath, timestamp=timestamp, boldfont=boldfont)  
    else:
        print "Can't find the file directory..."

    
while True:
    findFiles(path)
    time.sleep(timeSpan)
    


