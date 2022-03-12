# Pearson's correlation
import fasttext
import numpy as np
from scipy.stats import pearsonr
ft_en = fasttext.load_model('D:\Project\Data\\fasttext\English_300.bin')

def SemanticDiss(target, context):
    '''

    :param target: target word
    :param context: context words
    :return: Pearson's correlation
    '''
    targetVec=ft_en.get_word_vector(target)
    ContextVec = np.zeros(300)
    for word in context:
        ContextVec+=ft_en.get_word_vector(word)
    ContextVec/=len(context)
    corr, _ = pearsonr(targetVec, ContextVec)
    return corr

corr=SemanticDiss("hello",["hello","hello","hello"])
print(corr)