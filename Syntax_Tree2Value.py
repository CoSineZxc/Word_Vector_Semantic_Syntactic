from stanza.server import CoreNLPClient
import os
import re
corenlp_dir = 'D:\Project\Data\stanza_model'
os.environ["CORENLP_HOME"] = corenlp_dir

class NodeModule:
    '''
    convert tree string to node module
    type:   1: "child {\n" start of a node
            2: Original word or syntactic tag in a node or None
            3: "}" end of a node
            4: merged node
    value:  string, real word or syntactic tag (POS tag/sentence constituents)
    ifreal: if the value of the node is real word or syntactic tag
            1: real word(leaf node)
            0: tag
    ifOneChild: if the node is a node with one child node, which can be simplified
            1: only one child
            0: more than one child
    '''
    def __init__(self,type,value,ifreal,ifOneChild):
        self.type = type
        self.value = value
        self.ifreal = ifreal
        self.ifOneChild = ifOneChild



def Tree2Stack_n_Operations(tree,wordlist):
    '''
    Every time when "}"goes into the node stack, it should be combined with the
    nearest "child{" and the value between them, which means an additional
    operation has been done.
    Every time a real word goes into the node stack, the length of the stack should
    be the number of merged modules +1.
    the merged constituent for punctuation should be deleted
    :param tree: tree in string version
    :param wordlist: wordlist(without punctuation)
    :return:
    '''
    stack_num_list=[]
    operation_num_list=[]
    tree=tree[1:-1]
    node_str_list=re.split(r'\n\s*',tree)
    node_stack=[]
    for node_str in node_str_list:
        if re.match(r'child[{]',node_str)!=None:
            node_stack.append(NodeModule(1,None,0,))# ifonechild怎么办
    if len(stack_num_list)!=len(operation_num_list):
        print("the length of two return list doesn't match")
        return 0
    if len(stack_num_list)!=len(wordlist):
        print("the length of return data doesn't match wordlist")
        return 0
    return stack_num_list, operation_num_list
def Creat_valuelist_n_wordlist(sentence):
    wordlist=[]
    tree = sentence.parseTree.child.__str__()
    for token in sentence.token:
        if re.match(r'\W+',token.originalText)==None:
            wordlist.append(token.originalText)
    treelist=Tree2Stack_n_Operations(tree,wordlist)




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
                Creat_valuelist_n_wordlist(sentence)



