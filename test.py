# import os
# import re
# folder_path = "D:\Project\Data\preprocess\Exp2\\1_InsertMarkers\WordAligner"
# file_list = os.listdir(folder_path)
# # 切换到当前文件夹路径下
# os.chdir(folder_path)
# for old_name in file_list:
#     # head=re.findall(r"(.+?)[0-9][0-9]_WordTimeAligner.mat",old_name)
#     # end=re.findall(r"[0-9][A-Za-z]+(.+?)_WordTimeAligner.mat",old_name)
#     # if head[0]=="1Apea":
#     #     head="C1"
#     # elif head[0]=="2Apea":
#     #     head="C2"
#     # elif head[0]=="1Aprince":
#     #     head="C3"
#     # elif head[0]=="2Aprince":
#     #     head="C4"
#     # elif head[0]=="1coyote":
#     #     head="A1"
#     # elif head[0]=="2coyote":
#     #     head="A2"
#     # elif head[0]=="1hyena":
#     #     head="B1"
#     # elif head[0]=="2hyena":
#     #     head="B2"
#     # elif head[0]=="1ivan":
#     #     head="A3"
#     # elif head[0]=="2ivan":
#     #     head="A4"
#     # elif head[0]=="1match":
#     #     head="D3"
#     # elif head[0]=="2match":
#     #     head="D4"
#     # elif head[0]=="1sun":
#     #     head="D1"
#     # elif head[0]=="2sun":
#     #     head="D2"
#     # elif head[0]=="1women":
#     #     head="B3"
#     # elif head[0]=="2women":
#     #     head="B4"
#     new_name=old_name[1:]
#     os.rename(old_name, new_name)
#     pass

import numpy as np
import matplotlib.pyplot as plt

# x=['A','B','C','D']
# y1=[0.022498929,0.027746446,0.011387516,0.022150027]
# y2=[0.034160242,0.043760729,0.015001292,0.028285321]
# y3=[0.037452252,0.037345784,0.018515306,0.030609791]
# y4=[0.014539056,0.009105512,0.009058676,0.007905777]
# y5=[0.016346758,0.014021706,0.007708962,0.013267458]
# y6=[0.014397489,0.016575614,0.007641274,0.006834851]
# l1=plt.plot(x,y1,'ro-',label='5 words sliding window (Exp1)')
# l2=plt.plot(x,y2,'b+-',label='10 words sliding window (Exp1)')
# l3=plt.plot(x,y3,'r^-',label='Whole Sentence (Exp1)')
# l4=plt.plot(x,y4,'bo-',label='5 words sliding window (Exp2)')
# l5=plt.plot(x,y5,'b+-',label='10 words sliding window (Exp2)')
# l6=plt.plot(x,y6,'b^-',label='Whole Sentence (Exp2)')
# plt.plot(x,y1,'ro-',x,y2,'r+-',x,y3,'r^-',x,y4,'bo-',x,y5,'b+-',x,y6,'b^-')
# plt.title('Cross Correlation')
# plt.xlabel('condition')
# plt.legend()
# plt.ylim(0,0.06)
# plt.show()

x=['A','B','C','D']
# y1=[0.022498929,0.027746446,0.011387516,0.022150027]
# y2=[0.014539056,0.009105512,0.009058676,0.007905777]
# y1=[0.034160242,0.043760729,0.015001292,0.028285321]
# y2=[0.016346758,0.014021706,0.007708962,0.013267458]
y1=[0.037452252,0.037345784,0.018515306,0.030609791]
y2=[0.014397489,0.016575614,0.007641274,0.006834851]
# y1=[0.060728728,0.052004599,0.034285766,0.043375861]
# y2=[0.054316461,0.045734861,0.012628838,0.02212558]
l1=plt.plot(x,y1,'ro-',label='Exp1')
l2=plt.plot(x,y2,'b+-',label='Exp2')
# l3=plt.plot(x,y3,'bx-',label='whole sentence')
# l4=plt.plot(x,y4,'c*-',label='whole passage')
plt.title('Cross Correlation (whole sentence)')
plt.xlabel('condition')
plt.legend()
plt.ylim(0,0.05)
plt.show()