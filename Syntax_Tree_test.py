import stanza

# nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')
# doc = nlp('This is a test')
# for sentence in doc.sentences:
#     print(sentence.constituency)

# 目前 constituency 不能用 for Spanish
# nlp = stanza.Pipeline(lang='es', processors='tokenize,pos,constituency')
# doc = nlp('Vivían un leñador y sus dos hijos.')
# for sentence in doc.sentences:
#     print(sentence.constituency)

# from stanza.server import CoreNLPClient
# import os
# corenlp_dir = 'D:\Project\Data\stanza_model'
# os.environ["CORENLP_HOME"] = corenlp_dir
# text = "Dijo la madrastra con desprecio"
# # text = "Mr. Coyote was getting very old\nand had to be more careful for his own safety."
# with CoreNLPClient(
#         # properties='English',
#         properties={
#             'annotators': 'tokenize,ssplit,pos,parse',
#             'tokenize.language': 'es',
#             'pos.model':'edu/stanford/nlp/models/pos-tagger/spanish-ud.tagger',
#             'parse.model': 'edu/stanford/nlp/models/srparser/spanishSR.beam.ser.gz',
#         },
#         timeout=30000,
#         memory='6G') as client:
#     ann = client.annotate(text)
#     for sentence in ann.sentence:
#         constituency_parse = sentence.parseTree
#         print(constituency_parse)

from stanza.server import CoreNLPClient
import os
corenlp_dir = 'D:\Project\Data\stanza_model'
os.environ["CORENLP_HOME"] = corenlp_dir
text = "Tom loves Amy"
with CoreNLPClient(
        properties='English',
        annotators=['parse'],
        timeout=30000,
        memory='6G') as client:
    ann = client.annotate(text)
    sentence = ann.sentence[0]
    constituency_parse = sentence.parseTree
    print(constituency_parse)