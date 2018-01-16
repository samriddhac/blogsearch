location='D://Samriddha/personal/projects/sample_data/'
data = list(csv.reader(open(location+'output_2.csv', encoding="utf8")))
text_1 = data[4][3]+data[4][4]

special_chars = [w for w in keywords if re.findall(r'[\.\+\,\;\*\(\)\{\}\[\]\$\&\%\^\#@0-9]', w)]
re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
['ing']
re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
['processing']
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
[('process', 'ing')]
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
[('process', 'es')]
re.findall(r"<a> (<.*>) <man>", text)

>>> pos = {}
>>> pos['1']='NN'
>>> pos['2']='NLP'
>>> pos
{'1': 'NN', '2': 'NLP'}
>>> list(pos)
['1', '2']
>>> sorted(list(pos))
['1', '2']
>>> pos.keys()
dict_keys(['1', '2'])
>>> pos.values()
dict_values(['NN', 'NLP'])
>>> pos.items()
dict_items([('1', 'NN'), ('2', 'NLP')])
>>> [w for w in pos]
['1', '2']
>>> [w for w in pos]
['1', '2']
>>> list(pos.keys())
['1', '2']
>>> list(pos.values())
['NN', 'NLP']
>>> list(pos.items())
[('1', 'NN'), ('2', 'NLP')]

>>> pos={'3':'ADV', '4':'ADJ'}
>>> pos
{'3': 'ADV', '4': 'ADJ'}

>>> from collections import defaultdict
>>> test = defaultdict(int)
>>> test['a']
0
>>> pos = defaultdict(lambda: 'NN')
>>> pos
defaultdict(<function <lambda> at 0x000001E440023048>, {})
>>> pos['1']
'NN'
>>> from nltk.corpus import brown
>>> count = defaultdict(int)
>>> for(word, tag) in brown.tagged_words(categories='news', tagset='universal'):
...     count[tag]+=1
...
>>> sorted(list(count))
['.', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'VERB', 'X']
>>> from operator import itemgetter
>>> sorted(count.items(), key=itemgetter(1), reverse=False)
[('X', 92), ('NUM', 2166), ('PRT', 2264), ('PRON', 2535), ('CONJ', 2717), ('ADV', 3349), ('ADJ', 6706), ('DET', 11389), ('.', 11928), ('ADP', 12355), ('VERB', 14399), ('NOUN', 30654)]

>>> pair = ('1','a')
>>> itemgetter(0)(pair)
'1'
>>> itemgetter(1)(pair)
'a'>>> for key, value in pos.items():
...     pos_reverse_2[value].append(key)
...
>>> pos_reverse_2
defaultdict(<class 'list'>, {'ADJ': ['colorless', 'old'], 'N': ['ideas', 'cats'], 'V': ['sleep', 'scratch'], 'ADV': ['furiously', 'peacefully']})
>>> list(pos_reverse_2.items())
[('ADJ', ['colorless', 'old']), ('N', ['ideas', 'cats']), ('V', ['sleep', 'scratch']), ('ADV', ['furiously', 'peacefully'])]
