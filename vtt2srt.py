#WebVTT to SRT Converter
#Mostafa Nasiri

import os

for entry in os.scandir('.'):
    if entry.is_file():
        if os.path.splitext(entry.name)[1]==('.vtt'):   #List vtt File in directory
         fp = open(entry.name, "rb")
         data = fp.read()
         fp.close()
         times=[]
         s='' #output string variable
         for i in range(len(data)) : #Search for timelaps
             if (data[i]+data[i-1]==20):times.append(i)
         times.append(len(data))

         if (data[20]==62): #time format check
            for j in range(len(times)-1) :
             s=s+str(j+1)+"\r\n"+'00:'+((data[times[j]+1:times[j]+24].decode(encoding='UTF-8')).replace('.',',')).replace('--> ','--> 00:')+"\r\n"+(data[times[j]+25:times[j+1]-1].decode(encoding='UTF-8'))+"\r\n"+"\r\n"
         else:
             for j in range(len(times)-1) :
              s=s+str(j+1)+"\r\n"+((data[times[j]+1:times[j]+30].decode(encoding='UTF-8')).replace('.',','))+"\r\n"+(data[times[j]+31:times[j+1]-1].decode(encoding='UTF-8'))+"\r\n"+"\r\n"

         fp = open(os.path.splitext(entry.name)[0]+".srt", "wb") #Write srt file
         fp.write(s.encode('utf-8'))
         fp.close()
