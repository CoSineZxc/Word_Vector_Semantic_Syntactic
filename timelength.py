import wave
import contextlib
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io as sio


Path = 'D:\Project\Data\stringfile\Exp2\\'

def get_length(dataPath):
    with contextlib.closing(wave.open(dataPath,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

timelist=[]
namelist=[]

for i in range(4):
    for j in range(4):
        for k in range(60):
            if i==0:
                filename =Path+"AA"+str(j+1)+"{:02d}".format(k+1)+".wav"
                namelist.append("A"+str(j+1)+"{:02d}".format(k+1))
            elif i==1:
                filename =Path+"AB"+str(j+1)+"{:02d}".format(k+1)+".wav"
                namelist.append("B" + str(j + 1) + "{:02d}".format(k + 1))
            elif i==2:
                filename = Path + "AC" + str(j+1) + "{:02d}".format(k+1) + ".wav"
                namelist.append("C" + str(j + 1) + "{:02d}".format(k + 1))
            else:
                filename = Path + "AD" + str(j+1) + "{:02d}".format(k+1) + ".wav"
                namelist.append("D" + str(j + 1) + "{:02d}".format(k + 1))
            timelist.append(get_length(filename))


# save .mat
name = 'Exp2LengthSentence1.mat'
dic={}
for i, name in enumerate(namelist):
    dic[name]=timelist[i-1]
sio.savemat(name, {'dict': dic})
# sio.savemat(name, {'FileName': namelist, 'TimeLength': timelist})

#
print("max: "+str(max(timelist)))
print("min: "+str(min(timelist)))
print("average: "+str(sum(timelist)/len(timelist)))
# mode=stats.mode(timelist)[0][0]
# print("mode: "+str(mode))
#
#
# plt.bar(range(len(timelist)), timelist)
# plt.show()
timelist.sort()
plt.bar(range(len(timelist)), timelist)
plt.show()
n_1=0
n_2=0
n_3=0
n_4=0
n_5=0
n_6=0
n_7=0
for i in timelist:
    if i<2.7:
        n_1=n_1+1
    elif i >= 2.7 and i < 2.8:
        n_7 = n_7 + 1
    elif i>=2.8 and i<2.9:
        n_2=n_2+1
    elif i >= 2.9 and i < 3.0:
        n_3 = n_3 + 1
    elif i>=3.0 and i<3.1:
        n_4=n_4+1
    elif i>=3.1 and i<3.2:
        n_5=n_5+1
    else:
        n_6=n_6+1
print("0-2.7s: ",str(n_1))
print("2.7-2.8s: ",str(n_7))
print("2.8-2.9s: ",str(n_2))
print("2.9-3.0s: ",str(n_3))
print("3.0-3.1s: ",str(n_4))
print("3.1-3.2s: ",str(n_5))
print("3.2-3.3s: ",str(n_6))
N=[n_1,n_7,n_2,n_3,n_4,n_5,n_6]
plt.xticks(range(7),['0-2.7','2.7-2.8','2.8-2.9','2.9-3.0','3.0-3.1','3.1-3.2','≥3.2'])
plt.bar(range(len(N)), N)
plt.show()