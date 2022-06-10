from stanza.server import CoreNLPClient
import os
corenlp_dir = 'D:\Project\Data\stanza_model'
os.environ["CORENLP_HOME"] = corenlp_dir

def Tree2Stack_n_Operations(sentence):
    return 0

with CoreNLPClient(
        properties='English',
        annotators=['parse'],
        timeout=30000,
        memory='6G') as client:
    for i in range(4):
        for j in range(4):
            name = chr(ord('A') + i) + str(j + 1)
            print(name)
            file = open("stimuli_Eng\\" + name + ".txt", "r", encoding='gbk')
            text = file.read()
            ann = client.annotate(text)
            for sentence in ann.sentence:
                tree=sentence.parseTree.child.__str__()



