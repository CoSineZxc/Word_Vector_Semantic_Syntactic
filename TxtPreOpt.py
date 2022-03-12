import re

file_read=open("ori_text.txt", "r+b")
file_write=open("stimuli\\1_prince.txt","w")
for line in file_read:
    line = line.decode()
    line = re.sub('[1-9][0-9]*.\t\s*|\r|\[.*\]', '', line)
    file_write.writelines(line)

file_read.close()
file_write.close()