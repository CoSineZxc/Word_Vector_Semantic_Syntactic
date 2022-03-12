import scipy.io as sio
import re

name="women"
AlignerPath="D:\Project\Data\\aligner\output\\"
for i in range(2):
    StrI=str(i+1)
    for j in range(60):
        StrJ=f"{j+1:02}"
        file_read=open(AlignerPath+name+"\\"+StrI+"\\"+StrI+name+StrJ+".TextGrid")
        wordlist=[]
        timelist=[]
        for line in file_read:
            if line.find("item [2]")!=-1:
                    break
            elif line.find("intervals [")!=-1:
                xmin=file_read.readline()
                xmax=file_read.readline()
                text=file_read.readline()
                reg=re.compile(r'\s*text\s=\s"(.*)"\s')
                text=reg.findall(text)
                if text[0]=="":
                    continue
                else:
                    wordlist.append(text[0])
                    reg = re.compile(r'\s*xmin\s=\s([0-9|\.]*)\s')
                    xmin=reg.findall(xmin)
                    reg = re.compile(r'\s*xmax\s=\s([0-9|\.]*)\s')
                    xmax=reg.findall(xmax)
                    timelist.append([float(xmin[0]),float(xmax[0])])
            else:
                continue
        file_read.close()
        matdic={"wordlist":wordlist,"timelist":timelist}
        if name=="pea" or name=="prince":
            sio.savemat("./rslt/"+StrI+"A"+name+StrJ+"_WordTimeAligner.mat",matdic)
        else:
            sio.savemat("./rslt/"+StrI+name+StrJ+"_WordTimeAligner.mat",matdic)
