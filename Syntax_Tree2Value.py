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

class Node(object):
#     '''
#     full binary tree node (has either two or no children)
#     self.parent: parent's number in the list
#     self.childList: list of children's number in the list
#     self.value: value
#     self.ifLeafNode(): if this node is a leaf node
#     self.ifRootNode(): if this node is a root node
#     self.ifOneChildNode(): is this node only have one child (which can be simplified)
#     '''
    def __init__(self,value=None,parent=None,lchild=None,rchild=None):
        self.value=value
        self.parent=parent
        self.lchild=lchild
        self.rchild=rchild
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

class FullBiTree(object):
    

def Tree2Stack_n_Operations(tree,StackLengthList,OperationsNumList,NodeStack):
    if re.match(r'\W+',tree.value)!=None:
        return StackLengthList,OperationsNumList,NodeStack
    if len(tree.child)!=0:
        for ChildNode in tree.child:
            StackLengthList,OperationsNumList,NodeStack=Tree2Stack_n_Operations(ChildNode,StackLengthList,OperationsNumList,NodeStack)
        NodeStack=NodeStack[0:len(NodeStack)-len(tree.child)]
        OperationsNumList[-1]+=1
    else:
        StackLengthList.append(len(NodeStack)+1)
        OperationsNumList.append(1)
    NodeStack.append(tree)
    return StackLengthList,OperationsNumList,NodeStack

def Creat_wordlist(sentence):
    wordlist=[]
    for token in sentence.token:
        if re.match(r'\W+',token.originalText)==None:
            wordlist.append(token.originalText)
    return wordlist

def TreeSimplify(sentence):
    '''
    delete all nodes that only have one child node
    :return:
    '''
    Node=sentence.parseTree
    return 0

def Tree2NumofOpenNode():
    return 0

if __name__ == "__main__":
    with CoreNLPClient(
            properties='English',
            annotators=['parse'],
            timeout=30000,
            memory='6G') as client:
        text="Bill Gates met two very tired dancers in Cambridge"
        ann = client.annotate(text)
        sentence = ann.sentence[0]
        tree = sentence.parseTree
        print(tree)
        # tree = tree.child[0]
        # StackLengthList, OperationsNumList, NodeStack = Tree2Stack_n_Operations(tree, [], [], [])
        # for i in range(4):
        #     for j in range(4):
        #         name = chr(ord('A') + i) + str(j + 1)
        #         print(name)
        #         file = open("stimuli_Eng\\" + name + ".txt", "r", encoding='gbk')
        #         text = file.read()
        #         ann = client.annotate(text)
        #         for sentence in ann.sentence:
        #             wordlist=Creat_wordlist(sentence)
        #             tree = sentence.parseTree
        #             tree = tree.child[0]
        #             StackLengthList, OperationsNumList, NodeStack = Tree2Stack_n_Operations(tree, [], [], [])
        #             OperationsNumList[-1]-=1


