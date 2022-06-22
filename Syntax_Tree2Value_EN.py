from stanza.server import CoreNLPClient
import os
import re
import scipy.io as scio
corenlp_dir = 'D:\Project\Data\stanza_model'
os.environ["CORENLP_HOME"] = corenlp_dir

class BiNode(object):
    '''
    binary tree node (has either two or no children but not full binary tree)
    self.value: value
    self.lchild: left child
    self.rchild: right child
    '''
    def __init__(self,value=None,lchild=None,rchild=None):
        self.value=value
        self.lchild=lchild
        self.rchild=rchild

    def ifLeafNode(self):
        '''
        In this tree, every node will have 0/2 child nodes,but leaf node can be in
        different depth.
        :return:
        '''
        if self.lchild==None and self.rchild==None:
            return True
        elif self.lchild!=None and self.lchild!=None:
            return False
        else:
            print("ERROR: Tree structure wrong, at least one node has only one child.")
            return False

    def print_tree(self):
        print(self.value,end=" ")
        if self.lchild!=None and self.rchild!=None:
            self.lchild.print_tree()
            self.rchild.print_tree()
        elif self.lchild==None and self.lchild==None:
            print("#", end=" ")
            print("#", end=" ")
        else:
            print("\nERROR: Tree structure wrong, at least one node has only one child.")
        return

    def RChildExtension(self,childlist):
        BT = BiNode("void")
        BT.lchild = self.CreatFromParseTree(childlist[0])
        if len(childlist)==2:
            BT.rchild = self.CreatFromParseTree(childlist[1])
        elif len(childlist)>2:
            BT.rchild = self.RChildExtension(childlist[1:])
        else:
            print("ERROR: extend less than 2 children")
        return BT

    def CreatFromParseTree(self,tree):
        '''
        The binary tree is generated from real syntax parse tree. Real Syntax tree
        created by CoreNLP is a tree whose nodes have different numbers of child nodes
        rather than a binary tree. According to Nelson's strategy (Nelson et al, 2017),
        they used a binary-branching tree representing the syntax structure. So we have
        to change the original tree into binary tree without changing the syntax
        structure too much.
        There is a traditional algorithm on changing tree to binary tree in Computer
        Science, which is let the first child of the parent node be the left child and
        let all other child nodes to right child of the child node on its left. However,
        this algorithm break the syntax structure of the original tree, which make no
        sense to our research.
        So the final solution is if the node A has more than two child, we will treat the
        first child node as left child of A and create a new node B as the right child.
        let the second child of A as the left child of B, and let the third child of A be
        the right child of B or the left child of the right child of B if A has more than
        three child nodes.
        Another action we do is that we delete all of the nodes which only has one child.
        Because what we mainly focus is merging operation when listening a sentence.
        '''
        childlist=[]
        for node in tree.child:     # delete punctuation
            if node.value!="":
                childlist.append(node)
        if len(tree.child)==0:      # leaf node
            BT = BiNode(tree.value)
            return BT
        elif len(childlist)==1:    # should be deleted
            BT=self.CreatFromParseTree(childlist[0])
            return BT
        elif len(childlist)==2:    # keep it as binary tree node with two children
            BT=BiNode(tree.value)
            BT.lchild=self.CreatFromParseTree(childlist[0])
            BT.rchild=self.CreatFromParseTree(childlist[1])
        else:                       # more than 2 children
            BT = BiNode(tree.value)
            BT.lchild = self.CreatFromParseTree(childlist[0])
            BT.rchild=self.RChildExtension(childlist[1:])
        return BT

def Tree2Stack_n_Operations(tree,StackLengthList,OperationsNumList,NodeStack):
    # if re.match(r'\W+$',tree.value)!=None and tree.value!='-':
    #     return StackLengthList,OperationsNumList,NodeStack
    if len(tree.child)!=0:
        puncNum=0
        for ChildNode in tree.child:
            if ChildNode.value!="":
                StackLengthList,OperationsNumList,NodeStack=Tree2Stack_n_Operations(ChildNode,StackLengthList,OperationsNumList,NodeStack)
            else:
                puncNum+=1
        NodeStack=NodeStack[0:len(NodeStack)-len(tree.child)+puncNum]
        OperationsNumList[-1]+=1
    else:
        StackLengthList.append(len(NodeStack)+1)
        OperationsNumList.append(1)
        # print(tree.value,end="$")
    NodeStack.append(tree)
    return StackLengthList,OperationsNumList,NodeStack

def Tree2Stack_n_Operations_final(tree):
    StackLengthList, OperationsNumList, NodeStack1 = Tree2Stack_n_Operations(tree, [], [], [])
    OperationsNumList[-1] -= 1
    return StackLengthList, OperationsNumList

def Creat_wordlist(sentence):
    wordlist=[]
    for token in sentence.token:
        if re.match('\W+$',token.originalText)==None:
            wordlist.append(token.originalText)
    return wordlist

def CountStackLength_Condition_BiTree(NodeStack,tag):
    '''
    count how many nodes in the stack under some condition
    :param NodeStack:
    :param tag:
            1: individual word (leaf node)
            2: close constituent (non leaf node)
    :return:
    '''
    num=0
    if tag==1:
        Flag=True
    elif tag==2:
        Flag=False
    else:
        print("ERROR: tag input error")
        return
    for node in NodeStack:
        if node.ifLeafNode()==Flag:
            num+=1
    return num

def BiTree2NumofOpenNode(Bitree,IndividualWordNumList,CloseConstituentNumList,NodeStack):
    if Bitree.ifLeafNode()==True:
        NodeStack.append(Bitree)
        IDnum=CountStackLength_Condition_BiTree(NodeStack,1)
        CCnum=CountStackLength_Condition_BiTree(NodeStack,2)
        IndividualWordNumList.append(IDnum)
        CloseConstituentNumList.append(CCnum)
    else:
        IndividualWordNumList,CloseConstituentNumList,NodeStack=BiTree2NumofOpenNode(Bitree.lchild,IndividualWordNumList,CloseConstituentNumList,NodeStack)
        IndividualWordNumList,CloseConstituentNumList,NodeStack=BiTree2NumofOpenNode(Bitree.rchild, IndividualWordNumList, CloseConstituentNumList, NodeStack)
        NodeStack=NodeStack[0:len(NodeStack)-2]
        NodeStack.append(Bitree)
    return IndividualWordNumList,CloseConstituentNumList,NodeStack

def CountStackLength_Condition_Tree(NodeStack,tag):
    '''
    count how many nodes in the stack under some condition
    :param NodeStack:
    :param tag:
            1: individual word (leaf node)
            2: close constituent (non leaf node)
    :return:
    '''
    num=0
    if tag==1:
        for node in NodeStack:
            if len(node.child) == 0:
                num += 1
    elif tag==2:
        for node in NodeStack:
            if len(node.child) != 0:
                num += 1
    else:
        print("ERROR: tag input error")
        return
    return num

def Tree2NumofOpenNode(tree,IndividualWordNumList,CloseConstituentNumList,NodeStack):
    # if re.match(r'\W+$', tree.value) != None and tree.value!='-':
    #     return IndividualWordNumList,CloseConstituentNumList,NodeStack
    if len(tree.child)==0:
        NodeStack.append(tree)
        IDnum=CountStackLength_Condition_Tree(NodeStack,1)
        CCnum=CountStackLength_Condition_Tree(NodeStack,2)
        IndividualWordNumList.append(IDnum)
        CloseConstituentNumList.append(CCnum)
    elif len(tree.child)==1:
        if tree.child[0].value!="":
            IndividualWordNumList, CloseConstituentNumList, NodeStack = Tree2NumofOpenNode(tree.child[0],
                                                                                       IndividualWordNumList,
                                                                                       CloseConstituentNumList,
                                                                                       NodeStack)
    else:
        punc_num=0
        for childnode in tree.child:
            if childnode.value != "":
                IndividualWordNumList, CloseConstituentNumList, NodeStack = Tree2NumofOpenNode(childnode,
                                                                                             IndividualWordNumList,
                                                                                             CloseConstituentNumList,
                                                                                             NodeStack)
            else:
                punc_num+=1
        NodeStack=NodeStack[0:len(NodeStack)-len(tree.child)+punc_num]
        NodeStack.append(tree)
    return IndividualWordNumList,CloseConstituentNumList,NodeStack

def ListCombineOnebyOne(List1,List2):
    if len(List1)!=len(List2):
        print("ERROR: The length of list doesn't match")
        return
    else:
        List3=[i + j for i, j in zip(List1, List2)]
        return List3

def ClearPunctuation(tree,delete_next):
    if len(tree.child)==0:
        if delete_next==True:
            tree.Clear()
            delete_next=False
        if re.search(r'\W+',tree.value)!=None and tree.value!="Mr.":
            if tree.value=="-":
                delete_next=True
            tree.Clear()
        # else:
            # print(tree.value,end="$")
    elif len(tree.child)==1:
        tree_no_punc,delete_next=ClearPunctuation(tree.child[0],delete_next)
        tree.child[0].CopyFrom(tree_no_punc)
        if tree.child[0].value=="":
            tree.Clear()
    else:
        VoidFlag=True
        for child in tree.child:
            tree_no_punc, delete_next = ClearPunctuation(child, delete_next)
            child.CopyFrom(tree_no_punc)
            if child.value!="":
                VoidFlag=False
        if VoidFlag==True:
            tree.Clear()
    return tree,delete_next

def check_empty(word):
    if word == '\n' or word=="" or re.match('\W+$',word):
          return False
    return True

if __name__ == "__main__":
    with CoreNLPClient(
            properties='English',
            annotators=['parse'],
            timeout=30000,
            memory='6G') as client:
        # text="I will sing you a song and take you both for a jungle-ride."
        # ann = client.annotate(text)
        # sentence = ann.sentence[0]
        # tree = sentence.parseTree
        # tree = tree.child[0]
        # # print(tree)
        # tree_NoPunc,tag=ClearPunctuation(tree,False)
        # # print(tree_NoPunc)
        # #
        # StackLengthList, OperationsNumList = Tree2Stack_n_Operations_final(tree_NoPunc)
        # print(StackLengthList)
        # print(OperationsNumList)
        #
        # VOID=BiNode("fake")
        # BiTree=VOID.CreatFromParseTree(tree_NoPunc)
        # IndividualWordNumList_Bi,CloseConstituentNumList_Bi,NodeStack2=BiTree2NumofOpenNode(BiTree,[],[],[])
        # print(IndividualWordNumList_Bi)
        # print(CloseConstituentNumList_Bi)
        #
        # IndividualWordNumList_Original, CloseConstituentNumList_Original, NodeStack3 = Tree2NumofOpenNode(tree_NoPunc, [], [], [])
        # print(IndividualWordNumList_Original)
        # print(CloseConstituentNumList_Original)
        #
        # Value_bottomup=ListCombineOnebyOne(StackLengthList,OperationsNumList)
        # Value_BiOpennode=ListCombineOnebyOne(IndividualWordNumList_Bi,CloseConstituentNumList_Bi)
        # Value_OriOpennode=ListCombineOnebyOne(IndividualWordNumList_Original,CloseConstituentNumList_Original)
        # print(Value_bottomup)
        # print(Value_BiOpennode)
        # print(Value_OriOpennode)

        for i in range(4):
            for j in range(4):
                result_bottomup=[]
                result_BiOpennode=[]
                result_OriOpennode=[]
                Wordlist_all=[]
                name = chr(ord('A') + i) + str(j + 1)
                print(name)
                # if name!="B1"and name !="C4"and name!="D1":
                #     continue
                file = open("stimuli_Eng\\" + name + ".txt", "r", encoding='gbk')
                text = file.read()
                file.close()
                ann = client.annotate(text)
                # allWordFromToken=[]
                for sentence in ann.sentence:
                    # wordlist=Creat_wordlist(sentence)
                    # allWordFromToken+=Creat_wordlist(sentence)
                    # print(wordlist)
                    tree = sentence.parseTree
                    tree = tree.child[0]
                    tree_NoPunc, tag = ClearPunctuation(tree, False)
                    StackLengthList, OperationsNumList = Tree2Stack_n_Operations_final(tree_NoPunc)
                    VOID = BiNode("fake")
                    BiTree = VOID.CreatFromParseTree(tree_NoPunc)
                    IndividualWordNumList_Bi, CloseConstituentNumList_Bi, NodeStack2 = BiTree2NumofOpenNode(BiTree, [], [], [])
                    IndividualWordNumList_Original, CloseConstituentNumList_Original, NodeStack3 = Tree2NumofOpenNode(tree_NoPunc, [], [], [])
                    Value_bottomup=ListCombineOnebyOne(StackLengthList,OperationsNumList)
                    Value_BiOpennode=ListCombineOnebyOne(IndividualWordNumList_Bi,CloseConstituentNumList_Bi)
                    Value_OriOpennode=ListCombineOnebyOne(IndividualWordNumList_Original,CloseConstituentNumList_Original)
                    # if Value_BiOpennode!=Value_OriOpennode:
                    #     print("Your guess is wrong.")
                    # Wordlist_all+=wordlist
                    result_bottomup+=Value_bottomup
                    result_BiOpennode+=Value_BiOpennode
                    result_OriOpennode+=Value_OriOpennode
                file = open("stimuli_Eng\\" + name + ".txt", "r", encoding='gbk')
                wordlist_fromsplit=[]
                for line in file:
                    wordlist=line.split(' ')
                    # wordlist_fromsplit+=wordlist
                    for word in wordlist:
                        wordlist_fromsplit.append(re.sub(r'\W+','',word))
                file.close()
                # wordlist_filtered = list(filter(check_empty, wordlist))
                # if len(wordlist_filtered)!=len(result_bottomup) or len(wordlist_filtered)!=len(result_BiOpennode) or len(wordlist_filtered) != len(result_OriOpennode):
                # print("")
                # print(len(wordlist_fromsplit))
                print(len(result_bottomup))
                if len(wordlist_fromsplit) != len(result_bottomup) or len(wordlist_fromsplit) != len(result_BiOpennode) or len(wordlist_fromsplit) != len(result_OriOpennode):
                    print("ERROR:"+name)
                    # print(allWordFromToken)
                    # for word in wordlist_fromsplit:
                    #     print(word,end="$")

                mat_path_bottomup = 'D:\Project\Data\stimuli_SyntaxComplexity\Exp1\\' + name + '_bottomup.mat'
                mat_path_BiOpennode = 'D:\Project\Data\stimuli_SyntaxComplexity\Exp1\\' + name + '_BiOpennode.mat'
                mat_path_OriOpennode = 'D:\Project\Data\stimuli_SyntaxComplexity\Exp1\\' + name + '_OriOpennode.mat'
                # scio.savemat(mat_path_bottomup,
                #              {'WordVec': result_bottomup, 'wordlist': wordlist_fromsplit})
                # scio.savemat(mat_path_BiOpennode,
                #              {'WordVec': result_BiOpennode, 'wordlist': wordlist_fromsplit})
                # scio.savemat(mat_path_OriOpennode,
                #              {'WordVec': result_OriOpennode, 'wordlist': wordlist_fromsplit})