import re
import random

# file=open("stimuli\\1_prince.txt","r",encoding='gbk')0
# FullTxt=segment2="maintain maintaining re-establish maintian retain Maintain reestablish preserve establish mantain maintan"
FullTxt="The devil meanwhile was displeased. He did not like to see brotherly love, And wanted to spread misery and discord. He called his three henchmen to him. “I see too much friendship and happiness. Go and make them fight!” he told them. The henchmen visited Simon and Taras and cursed them with vanity and greed."

Wordlist=re.split("\s",FullTxt)
for j in range(3):
    for i in range(29):
        print(Wordlist[random.randint(0,len(Wordlist)-1)],end=" ")
    print("")

#
#cloud! slingshot. fly!” love love in second, flew feel love slingshot. and flew sight like it and the The At The fourth also fifth a “I the and air.
# file.close()