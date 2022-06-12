from stanza.server import CoreNLPClient
import os
import re
corenlp_dir = 'D:\Project\Data\stanza_model'
os.environ["CORENLP_HOME"] = corenlp_dir

# class NodeModule:
#     '''
#     convert tree string to node module
#     type:   #1: "child {\n" start of a node
#             2: Original word or syntactic tag in a node or None
#             3: "}" end of a node
#             4: merged node
#     value:  string, real word or syntactic tag (POS tag/sentence constituents)
#     ifreal: if the value of the node is real word or syntactic tag
#             1: real word(leaf node)
#             0: tag
#     '''
#     def __init__(self,type,value,ifreal):
#         self.type = type
#         self.value = value
#         self.ifreal = ifreal

# class Node:
#     '''
#     tree node
#     self.parent: parent's number in the list
#     self.childList: list of children's number in the list
#     self.value: value
#     self.ifLeafNode(): if this node is a leaf node
#     self.ifRootNode(): if this node is a root node
#     self.ifOneChildNode(): is this node only have one child (which can be simplified)
#     '''
#     def __init__(self,parent=None,childList=None,value=None):
#         self.value=value
#         self.parent=parent
#         self.childList=childList
#
#     def ifLeafNode(self):
#         if self.childList==None or self.childList==[]:
#             return True
#         else:
#             return False
#
#     def ifRootNode(self):
#         if self.parent==None:
#             return True
#         else:
#             return False
#
#     def ifOneChildNode(self):
#         if len(self.childList)==1:
#             return True
#         else:
#             return False

def Tree2Stack_n_Operations(tree,wordlist):
    return 0
#     '''
#     Every time when "}"goes into the node stack, it should be combined with the
#     nearest "child{" and the value between them, which means an additional
#     operation has been done.
#     Every time a real word goes into the node stack, the length of the stack should
#     be the number of merged modules +1.
#     the merged constituent for punctuation should be deleted
#     :param tree: tree in string version
#     :param wordlist: wordlist(without punctuation)
#     :return:
#     '''
#     stack_num_list=[]
#     operation_num_list=[]
#     tree=tree[1:-1]
#     node_str_list=re.split(r'\n\s*',tree)
#     node_stack=[]
#     for node_str in node_str_list:
#         if re.match(r'child[{]',node_str)!=None:
#             node_stack.append(NodeModule(1,None,0))#到这里了
#     if len(stack_num_list)!=len(operation_num_list):
#         print("the length of two return list doesn't match")
#         return 0
#     if len(stack_num_list)!=len(wordlist):
#         print("the length of return data doesn't match wordlist")
#         return 0
#     return stack_num_list, operation_num_list

def Creat_valuelist_n_wordlist(sentence):
    return 0
#     wordlist=[]
#     tree = sentence.parseTree.child.__str__()
#     for token in sentence.token:
#         if re.match(r'\W+',token.originalText)==None:
#             wordlist.append(token.originalText)
#     treelist=Tree2Stack_n_Operations(tree,wordlist)

def TreeSimplify():
    '''
    delete all nodes that only have one child node
    :return:
    '''
    return 0

def Tree2NumofOpenNode():
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
                Creat_valuelist_n_wordlist(sentence)



