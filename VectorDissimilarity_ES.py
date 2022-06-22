import fasttext
import numpy as np
from scipy.stats import pearsonr
import re
import scipy.io as scio
import matplotlib.pyplot as plt

# calculate semantic dissimilarity vector based on fasttext

Language = 'Spanish'
vector_dimension = 300
ft_sp = fasttext.load_model('D:\Project\Data\\fasttext\\' +Language+'_'+str(vector_dimension)+'.bin')
#%%
def SemanticDiss(target, context):
    '''
    Create semantic dissimilarity (Pearson's correlation)
    based on context words and target word
    :param target: target word
    :param context: context words
    :return: Pearson's correlation
    '''
    targetVec=ft_sp.get_word_vector(target)
    ContextVec = np.zeros(300)
    for word in context:
        ContextVec+=ft_sp.get_word_vector(word)
    ContextVec/=len(context)
    corr, _ = pearsonr(targetVec, ContextVec)
    return corr

# segment0="Mr. Coyote was getting very old and"

# long sentence: 16+20+16=52
# segment1="Mr. Coyote was getting very old and had to be more careful for his own safety. " \
#          "He had been walking for hours and hours through a beautiful valley, when he came upon a very large tree. " \
#          "Mr. Coyote was very tired and wanted to rest but he also needed to be safe."
# short sentence: 6+2+9+7+2+7+6+9+6+2=56
# segment2="“We need to call the doctor!” " \
#          "said Meg. " \
#          "Jo, will you be able to find his house?” " \
#          "“It’s the one with the tree right?” " \
#          "said Jo. " \
#          "“Yes, bring him as soon as possible. " \
#          "Hurry, before the snow gets worse!” " \
#          "Cried Meg as Jo rushed out of the house. " \
#          "“I will be back very soon!” " \
#          "said Jo."
# mix long and short: 3+7+5+3+19+13+6=56
# segment3="“This is fun! " \
#          "I can catch them in my basket!” " \
#          "“Watch out here they come!” " \
#          "said the sister. " \
#          "When they had gathered as many as they could carry, The brother and sister sat down to peel them. " \
#          "They burst open the prickly shells, And picked out the smooth chestnuts inside. " \
#          "“I can’t wait to have some!”"

def sliding_window(WindowLength,wordlist):
    '''
    Create dissimilarity list based on sliding window methods
    :param window: length of window
    :param segment: paragraph
    :return: 1-corr list
    '''
    # wordlist=segment.split(" ")
    subtract_corr_list=[]
    for i, word in enumerate(wordlist):
        wordlist[i] = re.sub("\W", "", word)
        if i==0:
            subtract_corr_list.append(1)
        elif i<WindowLength:
            corr=SemanticDiss(wordlist[i],wordlist[0:i])
            subtract_corr_list.append(1-corr)
        else:
            corr = SemanticDiss(wordlist[i], wordlist[i-WindowLength:i])
            subtract_corr_list.append(1 - corr)
    subtract_corr_list[0]=sum(subtract_corr_list[1:]) / len(subtract_corr_list[1:])
    return subtract_corr_list

def DivideBySentence(wordlist):
    '''

    :param segment: paragraph
    :return: 1-corr list
    '''
    # wordlist=segment.split(" ")
    subtract_corr_list = []
    SentenceStartFlag=False
    start=0
    for i, word in enumerate(wordlist):
        if i==0:
            if re.search("\.|\?|!|;",word)!=None and word!="Mr.":
                SentenceStartFlag=True
            wordlist[i] = re.sub("\W", "", word)
            subtract_corr_list.append(1)
            continue
        else:
            if re.search("\.|\?|!|;", word) == None or word=="Mr.":
                wordlist[i]=re.sub("\W","",word)
                corr = SemanticDiss(wordlist[i], wordlist[start:i])
                subtract_corr_list.append(1 - corr)
                if SentenceStartFlag==True:
                    start=i
                    SentenceStartFlag = False
            else:
                wordlist[i] = re.sub("\W", "", word)
                corr = SemanticDiss(wordlist[i], wordlist[start:i])
                subtract_corr_list.append(1 - corr)
                SentenceStartFlag = True
    subtract_corr_list[0] = sum(subtract_corr_list[1:]) / len(subtract_corr_list[1:])
    return subtract_corr_list

def DivideBySentence_wrong(wordlist):
    '''

    :param segment: paragraph
    :return: 1-corr list
    '''
    subtract_corr_list = []
    start=0
    for i, word in enumerate(wordlist):
        if i==0:
            wordlist[i] = re.sub("\W", "", word)
            subtract_corr_list.append(1)
        else:
            wordlist[i]=re.sub("\W","",word)
            corr = SemanticDiss(wordlist[i], wordlist[start:i])
            subtract_corr_list.append(1 - corr)
    subtract_corr_list[0] = sum(subtract_corr_list[1:]) / len(subtract_corr_list[1:])
    return subtract_corr_list

def DivideBySentence_wrong_paragraph(wordlist):
    '''

    :param segment: paragraph
    :return: 1-corr list
    '''
    subtract_corr_list = []
    for i, word in enumerate(wordlist):
        wordlist[i]=re.sub("\W","",word)
        corr = SemanticDiss(wordlist[i], wordlist)
        subtract_corr_list.append(1 - corr)
    return subtract_corr_list

def check_empty(word):
    if word == '\n' or word=="" or re.match('\W+$',word):
          return False
    return True

# segment1="maintain preserve mantain preserve!” Maintain re-establish reestablish maintan maintan maintian maintian, mantain maintan preserve, establish maintian re-establish maintian reestablish maintian maintan reestablish reestablish maintaining. re-establish maintain retain mantain maintan. maintaining"
# segment1="to vanity He He Go henchmen vanity And He not like to to to to with Go and was them. The and friendship with spread to see to make"
# segment2="misery three meanwhile henchmen make like them “I displeased. greed. much did henchmen and called brotherly was told and Go And love, called his make and Taras meanwhile love,"
# segment3="three He was and too discord. told with discord. was wanted called He greed. with friendship fight!” and told He like henchmen henchmen with them was greed. too Go"

# -------- type1 ---------
# 5 words sliding window
for i in range(4):
    for j in range(4):
        name=chr(ord('A') + i)+str(j+1)
        print(name)
        file = open("stimuli_sp\\" + name + ".txt", "r", encoding='utf-8')
        wordlist = []
        for line in file:
            # line = line.decode()
            # print(line)
            wordlist = wordlist + line.split(' ')
        file.close()
        # wordlist_new1=list(filter(check_empty, wordlist))
        # wordlist_new2=list(filter(check_empty, wordlist))
        wordlist_new3=list(filter(check_empty, wordlist))

        # result_Sliding5 = sliding_window(5, wordlist_new1)
        # result_Sliding10= sliding_window(10, wordlist_new2)
        result_sentence = DivideBySentence(wordlist_new3)
        # print(len(wordlist_new1))
        # if len(result_sentence)!=len(wordlist_new1):
        #     print("ERROR:"+name)
        # result_sentence_wrong = DivideBySentence_wrong(wordlist_new1)
        # result_sentence_wrong_paragraph = DivideBySentence_wrong_paragraph(wordlist_new1)
        mat_path_Sliding5='D:\Project\Data\stimuli_SemanticDissimilarity\Exp2\\'+name+'_Sliding_5.mat'
        mat_path_Sliding10 = 'D:\Project\Data\stimuli_SemanticDissimilarity\Exp2\\' + name + '_Sliding_10.mat'
        mat_path_sentence = 'D:\Project\Data\stimuli_SemanticDissimilarity\Exp2\\' + name + '_WholeSentence.mat'
        # mat_path_sentence_wrong = 'D:\Project\Data\stimuli_SemanticDissimilarity\Exp2\\' + name + '_WholeSentenceWrong.mat'
        # mat_path_sentence_wrong_paragraph = 'D:\Project\Data\stimuli_SemanticDissimilarity\Exp2\\' + name + '_paragraph.mat'
        # scio.savemat(mat_path_Sliding5, {'WordVec': result_Sliding5, 'wordlist': wordlist_new1})
        # scio.savemat(mat_path_Sliding10, {'WordVec': result_Sliding10, 'wordlist': wordlist_new2})
        scio.savemat(mat_path_sentence, {'WordVec': result_sentence, 'wordlist': wordlist_new3})
        # scio.savemat(mat_path_sentence_wrong, {'WordVec': result_sentence_wrong, 'wordlist': wordlist_new1})

        # scio.savemat(mat_path_sentence_wrong_paragraph, {'WordVec': result_sentence_wrong_paragraph, 'wordlist': wordlist_new1})

# rslt_1_1=sliding_window(5,segment1)
# rslt_1_2=sliding_window(5,segment2)
# rslt_1_3=sliding_window(5,segment3)


# print("-----5 words sliding window-----")
# print("Segment1:")
# print("length:"+str(len(rslt_1_1)))
# print("mean:"+str(sum(rslt_1_1)/len(rslt_1_1)))
# print([round(i,4) for i in rslt_1_1])
# print("Segment2:")
# print("length:"+str(len(rslt_1_2)))
# print("mean:"+str(sum(rslt_1_2)/len(rslt_1_2)))
# print([round(i,4) for i in rslt_1_2])
# print("Segment3:")
# print("length:"+str(len(rslt_1_3)))
# print("mean:"+str(sum(rslt_1_3)/len(rslt_1_3)))
# print([round(i,4) for i in rslt_1_3])
# a=sum(rslt_1_1)/len(rslt_1_1)
# b=sum(rslt_1_2)/len(rslt_1_2)
# c=sum(rslt_1_3)/len(rslt_1_3)
# print("mean of all:"+str((a+b+c)/3))
# # # -------- type2 ---------
# # # 10 words sliding window
# rslt_2_1=sliding_window(10,segment1)
# rslt_2_2=sliding_window(10,segment2)
# rslt_2_3=sliding_window(10,segment3)
# print("-----10 words sliding window-----")
# print("Segment1:")
# print("length:"+str(len(rslt_2_1)))
# print("mean:"+str(sum(rslt_2_1)/len(rslt_2_1)))
# print([round(i,4) for i in rslt_2_1])
# print("Segment2:")
# print("length:"+str(len(rslt_2_2)))
# print("mean:"+str(sum(rslt_2_2)/len(rslt_2_2)))
# print([round(i,4) for i in rslt_2_2])
# print("Segment3:")
# print("length:"+str(len(rslt_2_3)))
# print("mean:"+str(sum(rslt_2_3)/len(rslt_2_3)))
# print([round(i,4) for i in rslt_2_3])
# a=sum(rslt_2_1)/len(rslt_2_1)
# b=sum(rslt_2_2)/len(rslt_2_2)
# c=sum(rslt_2_3)/len(rslt_2_3)
# print("mean of all:"+str((a+b+c)/3))
# # # -------- type3 ---------
# # # particular sentence
# rslt_3_1=DivideBySentence(segment1)
# rslt_3_2=DivideBySentence(segment2)
# rslt_3_3=DivideBySentence(segment3)
# print("-----divided by Sentence-----")
# print("Segment1:")
# print("length:"+str(len(rslt_3_1)))
# print("mean:"+str(sum(rslt_3_1)/len(rslt_3_1)))
# print([round(i,4) for i in rslt_3_1])
# print("Segment2:")
# print("length:"+str(len(rslt_3_2)))
# print("mean:"+str(sum(rslt_3_2)/len(rslt_3_2)))
# print([round(i,4) for i in rslt_3_2])
# print("Segment3:")
# print("length:"+str(len(rslt_3_3)))
# print("mean:"+str(sum(rslt_3_3)/len(rslt_3_3)))
# print([round(i,4) for i in rslt_3_3])
# a=sum(rslt_3_1)/len(rslt_3_1)
# b=sum(rslt_3_2)/len(rslt_3_2)
# c=sum(rslt_3_3)/len(rslt_3_3)
# print("mean of all:"+str((a+b+c)/3))

# rslt_1_1=np.array(rslt_1_1)
# rslt_1_2=np.array(rslt_1_2)
# rslt_1_3=np.array(rslt_1_3)
# rslt_2_1=np.array(rslt_2_1)
# rslt_2_2=np.array(rslt_2_2)
# rslt_2_3=np.array(rslt_2_3)
# rslt_3_1=np.array(rslt_3_1)
# rslt_3_2=np.array(rslt_3_2)
# rslt_3_3=np.array(rslt_3_3)
#
# corr1, _ = pearsonr(rslt_1_1, rslt_2_1)
# corr2, _ = pearsonr(rslt_1_2, rslt_2_2)
# corr3, _ = pearsonr(rslt_1_3, rslt_2_3)
# corr4, _ = pearsonr(rslt_1_1, rslt_3_1)
# corr5, _ = pearsonr(rslt_1_2, rslt_3_2)
# corr6, _ = pearsonr(rslt_1_3, rslt_3_3)
# corr7, _ = pearsonr(rslt_3_1, rslt_2_1)
# corr8, _ = pearsonr(rslt_3_2, rslt_2_2)
# corr9, _ = pearsonr(rslt_3_3, rslt_2_3)
#
# print("5 words window vs 10 words window")
# print("segment1:"+str(corr1))
# print("segment2:"+str(corr2))
# print("segment3:"+str(corr3))
# print("5 words window vs sentence")
# print("segment1:"+str(corr4))
# print("segment2:"+str(corr5))
# print("segment3:"+str(corr6))
# print("sentence vs 10 words window")
# print("segment1:"+str(corr7))
# print("segment2:"+str(corr8))
# print("segment3:"+str(corr9))
#
# fig=plt.figure()
# fig.suptitle("5 words vs 10 words")
# ax1=fig.add_subplot(221)
# ax1.set_title("segment1")
# plt.xlabel("5 words window")
# plt.ylabel("10 words window")
# ax1.scatter(rslt_1_1,rslt_2_1,c='r',marker='.')
# ax2=fig.add_subplot(222)
# ax2.set_title("segment2")
# plt.xlabel("5 words window")
# plt.ylabel("10 words window")
# ax2.scatter(rslt_1_2,rslt_2_2,c='r',marker='.')
# ax3=fig.add_subplot(223)
# ax3.set_title("segment3")
# plt.xlabel("5 words window")
# plt.ylabel("10 words window")
# ax3.scatter(rslt_1_3,rslt_2_3,c='r',marker='.')
# fig.tight_layout()
# plt.show()
#
# fig=plt.figure()
# fig.suptitle("5 words vs sentence")
# ax1=fig.add_subplot(221)
# ax1.set_title("segment1")
# plt.xlabel("5 words window")
# plt.ylabel("sentence")
# ax1.scatter(rslt_1_1,rslt_3_1,c='r',marker='.')
# ax2=fig.add_subplot(222)
# ax2.set_title("segment2")
# plt.xlabel("5 words window")
# plt.ylabel("sentence")
# ax2.scatter(rslt_1_2,rslt_3_2,c='r',marker='.')
# ax3=fig.add_subplot(223)
# ax3.set_title("segment3")
# plt.xlabel("5 words window")
# plt.ylabel("sentence")
# ax3.scatter(rslt_1_3,rslt_3_3,c='r',marker='.')
# fig.tight_layout()
# plt.show()
#
# fig=plt.figure()
# fig.suptitle("10 words vs sentence")
# ax1=fig.add_subplot(221)
# ax1.set_title("segment1")
# plt.xlabel("10 words window")
# plt.ylabel("sentence")
# ax1.scatter(rslt_2_1,rslt_3_1,c='r',marker='.')
# ax2=fig.add_subplot(222)
# ax2.set_title("segment2")
# plt.xlabel("10 words window")
# plt.ylabel("sentence")
# ax2.scatter(rslt_2_2,rslt_3_2,c='r',marker='.')
# ax3=fig.add_subplot(223)
# ax3.set_title("segment3")
# plt.xlabel("10 words window")
# plt.ylabel("sentence")
# ax3.scatter(rslt_2_3,rslt_3_3,c='r',marker='.')
# fig.tight_layout()
# plt.show()

# plt.bar(list(range(len(rslt_1_1))),rslt_1_1)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_1_2))),rslt_1_2)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_1_3))),rslt_1_3)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_2_1))),rslt_2_1)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_2_2))),rslt_2_2)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_2_3))),rslt_2_3)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_3_1))),rslt_3_1)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_3_2))),rslt_3_2)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()
# plt.bar(list(range(len(rslt_3_3))),rslt_3_3)
# plt.xlabel("words")
# plt.ylabel("1-corr")
# plt.show()