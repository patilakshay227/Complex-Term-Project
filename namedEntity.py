import sqlite3
from polyglot.text import Text
import nltk
from nltk.tag.stanford import StanfordNERTagger
from itertools import groupby
import warnings
import string
import re

warnings.filterwarnings("ignore")

db = sqlite3.connect('/home/akshay/IIT KGP/SEM 2/Complex Network/Github/commentsData.db')
c = db.cursor()

tagConvert = {
    'I-LOC':'LOCATION',
    'I-ORG': 'ORGANIZATION',
    'I-PER': 'PERSON',
    'GPE'  : 'LOCATION',
    'GSP'  : 'LOCATION',
    'PERSON':  'PERSON',
    'ORGANIZATION': 'ORGANIZATION',
    'LOCATION': 'LOCATION',
    'FACILITY' : 'FACILITY'
    
}



c.execute("create table if not exists namedEntities(entity text, entityType text, userID int,gender text)")


# **** Change maleComments to femaleComments for adding female data
gender = 'male'

c.execute("select userID, comment from maleComments LIMIT 500")

sqlstat="insert into namedEntities values(?,?,?,?)"

# Stanford NER
stanford_classifier  = "/home/akshay/Stanford/stanford-ner-2018-02-27/classifiers/english.all.3class.distsim.crf.ser.gz"
stanford_ner_path = '/home/akshay/Stanford/stanford-ner-2018-02-27/stanford-ner.jar'

# Creating Tagger Object
st = StanfordNERTagger(stanford_classifier, stanford_ner_path,  encoding='utf-8' )

punctuations = string.punctuation

recProc = 0

for res in c.fetchall():
    recProc += 1
    try:
    
        ne = set()
        userID, comment = res

        # polyglot NE extraction
        blob = comment
        text = Text(blob)
        #print text.entities
        try:
            for e in text.entities:
                #print e.tag
                ne.add((tagConvert[e.tag] , ' '.join(e)))
        except:
            print 'error'



#           # Standford NER
#         tokenized_text = nltk.word_tokenize(comment)
#         classified_text = st.tag(tokenized_text)

#         for tag, chunk in groupby(classified_text, lambda x:x[1]):
#             if tag != "O":
#                 ne.add((tag, " ".join(w for w,t in chunk)))


        # nltk NE Extraction
        for sent in nltk.sent_tokenize(comment):
            try:
                for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                      if hasattr(chunk, 'label'):
                        ne.add((tagConvert[chunk.label()], ' '.join(c[0] for c in chunk)))
            except UnicodeEncodeError:
                pass


        for e in ne:
            escape = False
            if len(re.sub(r'[^a-zA-Z0-9]',"",e[1])) == 0:
                continue

            for w in nltk.word_tokenize(e[1]):
                #print nltk.pos_tag([w], tagset='universal')
                if nltk.pos_tag([w], tagset='universal')[0][1] == 'PRON' :
                    escape = True
            if escape:
                continue

            c.execute(sqlstat, (e[1], e[0], userID, gender))
            #print e[1], e[0], userID, 'male'
    
    except e:
        print 'error',e
        pass
    
    if (recProc % 10 ) == 0:
        print recProc, ' records processed.'

db.commit()



















# import sqlite3
# from polyglot.text import Text
# import nltk

# db = sqlite3.connect('../commentsData.db')
# c = db.cursor()

# # c.execute("create table if not exists commenterGender(userID int,username text,gender text,\
# # PRIMARY KEY(userID,username))")

# c.execute("select cg.userID, c.commentBody from comments c, commenterGender cg where c.userID = cg.userID and cg.gender = 'male' LIMIT 5")


# tagConvert = {
	
# }


# for res in c.fetchall():
# 	ne = []
# 	userID, comment = res

# 	# polyglot NE extraction
# 	blob = comment
#     	text = Text(blob)
#     	#print text.entities
#     	try:
#         	for e in text.entities:
# 			#print e.tag
#             		ne.append((e.tag , ' '.join(e)))
#     	except:
# 		print 'error'
#         	pass


#     	# nltk NE Extraction
#     	#for sent in nltk.sent_tokenize(comment):
#    	#	for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#       	#		if hasattr(chunk, 'label'):
#         #			ne.append((chunk.label(), ' '.join(c[0] for c in chunk)))

#     	for e in ne:
#     		print userID , e



