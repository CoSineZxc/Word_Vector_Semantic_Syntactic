import re
# copy orginal sentences from .doc file to ./ori_text.txt
# The name of the output file should be A/B/C/D 1/2/3/4.txt (based on stimuli order)
file_read=open("ori_text.txt", "r+b")
file_write=open("stimuli\\D4.txt","w")
for line in file_read:
    line = line.decode()
    line = re.sub('[1-9][0-9]*.\t\s*|\r|\[.*\]', '', line)
    file_write.writelines(line)

file_read.close()
file_write.close()