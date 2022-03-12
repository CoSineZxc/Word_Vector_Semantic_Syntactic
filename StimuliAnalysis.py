import re
import matplotlib.pyplot as plt

filelist=["1_coyote","2_coyote","1_pea","2_pea",
          "1_hyena","2_hyena","1_prince","2_prince",
          "1_ivan","2_ivan","1_sun","2_sun",
          "1_match","2_match","1_women","2_women"
          ]

EndPunc=['.','?','!',';']

AvoidWordList=["Mr."]
# avoid Mr. "

SentLengthList=[]


for filename in filelist:
    file=open("stimuli\\"+filename+".txt","r",encoding='gbk')
    FullTxt=file.read()
    Wordlist=re.split("\s|\n",FullTxt)
    SentLength=0
    sentence=[]
    for word in Wordlist:
        sentence.append(word)
        SentLength+=1
        if re.search("\.|\?|!|;",word)!=None:
            if word in AvoidWordList:
                continue
            for w in sentence:
                print(w,end=" ")
            print("")
            sentence=[]
            SentLengthList.append(SentLength)
            SentLength=0
        # punc=re.findall("\W", word)
        # if punc!=[]:
        #     if punc not in PuncList:
        #         PuncList.append(punc)
        #         PuncWordList.append(word)
    file.close()

# for i in PuncWordList:
#     print(i)

print(SentLengthList)
print("amount:"+str(len(SentLengthList)))
print("mean:"+str(sum(SentLengthList)/len(SentLengthList)))
print("max:"+str(max(SentLengthList)))
print("min:"+str(min(SentLengthList)))
SentLengthList.sort()
print("median:"+str(SentLengthList[len(SentLengthList)//2]))
mode=0
numnow=0
nummax=0
numcomp=0
for i,num in enumerate(SentLengthList):
    if i==0:
        mode=num
        numnow=num
        nummax+=1
        numcomp+=1
    else:
        if num==numnow:
            numcomp+=1
            if numcomp>=nummax:
                nummax=numcomp
                mode=num
        else:
            numnow=num
            numcomp=1

print("mode:"+str(mode))



# plt.bar(list(range(len(SentLengthList))),SentLengthList)
# plt.show()

# file=open("stimuli\\2_women.txt","r",encoding='gbk')
# FullTxt=file.read()
# Wordlist=re.split("\s|\n",FullTxt)
#
# label=0
#
# for word in Wordlist:
#     if re.findall("[a-z]+|[A-Z]+", word)==[]:
#         label=1
#     print(word)
#
# if label==1:
#     print("\nERROR")

# Mr.
# valley,
# "Please
# care".
# Tree",
# now!"
# big!
# “Oh
# beak!”
# couldn't
# Coyote’s
# bush;
# eyes?"
# eyes."
# “Dong,
# “Ugh!
# fifth?
# way.”
# “It’s
# happening?”
# sleep”
# Listen…”
# us,”
# much-awaited
# jungle-ride."
# friend,"
# back-fired.
# "Wonderful!
# from?!”
# “We're
# you..”
# growl…
# that!?”
# unscathed….
# so….?,
# mother?!
# burns!!!!”
# money”,
# time”.