import fasttext
import fasttext.util
import numpy as np
import scipy.io as scio
import re

# calculate word vector based on fasttext

# fasttext.util.download_model('en', if_exists='ignore')

# test=0
name="A2"

ft_en = fasttext.load_model('D:\Project\Data\\fasttext\English_300.bin')
# print("vector dimension: ")
# print(ft_en.get_dimension())

file=open("stimuli\\"+name+".txt","r",encoding='gbk')

# if test==1:
#     name="try"

wordlist=[]

for line in file:
    # line = line.decode()
    # print(line)
    wordlist=wordlist+line.split(' ')

file.close()
#
# sentence="Once upon a time, five little peas"
#
# wordlist=sentence.split(' ')

WordVec=np.empty(shape=(300,1))

for i, word in enumerate(wordlist):
    word=re.sub(',|\.|\?|!|;|“|”|"|…|\r|\n','',word)
    if word=='':
        continue
    print(word)
    wordvector=ft_en.get_word_vector(word)
    wordvector=np.expand_dims(wordvector,1)
    if i != 0:
        WordVec=np.concatenate((WordVec,wordvector.T),axis=0)
    else:
        WordVec=wordvector.T

print(WordVec.shape)
mat_path='D:\Project\Data\stimuli_wordvec\\'+name+'.mat'

scio.savemat(mat_path,{'WordVec':WordVec,'wordlist':wordlist})
