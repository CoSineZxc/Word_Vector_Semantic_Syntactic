import re
name="A"
# num="1"

for k in range(4):
    for j in range(2):
        num = str(j+1)
        file_read = open("stimuli\\" + chr(ord("A")+k)+str(num) + ".txt", "r", encoding='gbk')
        for i,line in enumerate(file_read):
            line=re.sub(r"“","\"",line)
            line = re.sub(r"”", "\"", line)
            line = re.sub(r"’", "\'", line)
            line = re.sub(r"…", ".", line)
            file_write=open("rslt\\"+chr(ord("A")+k)+str(num)+f"{i+1:02}"+".txt","w")
            file_write.writelines(line)
            file_write.close()

        file_read.close()


# num="2"
# file_read=open("stimuli\\"+num+"_"+name+".txt","r",encoding='gbk')
#
# for i,line in enumerate(file_read):
#     file_write=open("rslt\\"+num+name+f"{i+1:02}"+".txt","w")
#     file_write.writelines(line)
#     file_write.close()
#
# file_read.close()