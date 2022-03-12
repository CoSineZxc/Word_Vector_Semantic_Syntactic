import os
import re
folder_path = "D:\Project\Data\preprocess\\1_InsertMarkers\WordAligner"
file_list = os.listdir(folder_path)
# 切换到当前文件夹路径下
os.chdir(folder_path)
for old_name in file_list:
    head=re.findall(r"(.+?)[0-9][0-9]_WordTimeAligner.mat",old_name)
    end=re.findall(r"[0-9][A-Za-z]+(.+?)_WordTimeAligner.mat",old_name)
    if head[0]=="1Apea":
        head="C1"
    elif head[0]=="2Apea":
        head="C2"
    elif head[0]=="1Aprince":
        head="C3"
    elif head[0]=="2Aprince":
        head="C4"
    elif head[0]=="1coyote":
        head="A1"
    elif head[0]=="2coyote":
        head="A2"
    elif head[0]=="1hyena":
        head="B1"
    elif head[0]=="2hyena":
        head="B2"
    elif head[0]=="1ivan":
        head="A3"
    elif head[0]=="2ivan":
        head="A4"
    elif head[0]=="1match":
        head="D3"
    elif head[0]=="2match":
        head="D4"
    elif head[0]=="1sun":
        head="D1"
    elif head[0]=="2sun":
        head="D2"
    elif head[0]=="1women":
        head="B3"
    elif head[0]=="2women":
        head="B4"
    new_name=head+end[0]+"_WordTimeAligner.mat"
    os.rename(old_name, new_name)
    pass