from scipy.io import loadmat

EEGdataPath="D:\Project\Data\preprocess\EEGFinalMat"

for i in range(24):
    EEG = loadmat(EEGdataPath+'\EEG_'+str(i+1)+'.mat')
    print(type(EEG.event))