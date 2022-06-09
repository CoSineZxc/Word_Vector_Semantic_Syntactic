import stanza

# nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')
# doc = nlp('This is a test')
# for sentence in doc.sentences:
#     print(sentence.constituency)

# nlp = stanza.Pipeline(lang='es', processors='tokenize,pos,constituency')
# doc = nlp('Vivían un leñador y sus dos hijos.')
# for sentence in doc.sentences:
#     print(sentence.constituency)

from stanza.server import CoreNLPClient
import os
corenlp_dir = 'D:\Project\Data\stanza_model'
os.environ["CORENLP_HOME"] = corenlp_dir
# text = "Dijo la madrastra con desprecio"
text = "Cerca de un bosque espeso y oscuro, Vivían un leñador y sus dos hijos. Los hijos se llamaban Hansel y Gretel. Su mamá había muerto hace muchos años."
with CoreNLPClient(
        # properties='English',
        properties={
            'annotators': 'tokenize,ssplit,pos,parse',
            'tokenize.language': 'es',
            # 'mwt.mappingFile':'edu/stanford/nlp/models/mwt/spanish/spanish-mwt.tsv',
            'pos.model':'edu/stanford/nlp/models/pos-tagger/spanish-ud.tagger',
            'parse.model': 'edu/stanford/nlp/models/srparser/spanishSR.beam.ser.gz',
        },
        # annotators=['tokenize','ssplit','pos','lemma','ner', 'parse', 'depparse','coref'],
        # annotators=['tokenize','ssplit','pos','parse'],
        timeout=30000,
        memory='6G') as client:
    ann = client.annotate(text)
    for sentence in ann.sentence:
        constituency_parse = sentence.parseTree
        print(constituency_parse)
    # print(sentence.basicDependencies)
    # token = sentence.token[0]
    # print(token.value, token.pos, token.ner)
    # constituency_parse = sentence.parseTree
    # print(constituency_parse)

# from stanza.server import CoreNLPClient
# import os
# corenlp_dir = 'D:\Project\Data\stanza_model'
# os.environ["CORENLP_HOME"] = corenlp_dir
# text = "Mr. Coyote was getting very old"
# with CoreNLPClient(
#         properties='English',
#         # properties={
#         #     'parse.model': 'edu/stanford/nlp/models/srparser/spanishSR.beam.ser.gz',
#         # },
#         # annotators=['tokenize','ssplit','pos','lemma','ner', 'parse', 'depparse','coref'],
#         annotators=['parse'],
#         timeout=30000,
#         memory='6G') as client:
#     ann = client.annotate(text)
#     sentence = ann.sentence[0]
#     constituency_parse = sentence.parseTree
#     print(constituency_parse)