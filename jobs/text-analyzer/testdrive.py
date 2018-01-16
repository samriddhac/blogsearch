import os
import csv
import re
import nltk
from nltk.corpus import stopwords

location='D://Samriddha/personal/projects/sample_data/'
data = list(csv.reader(open(location+'output_2.csv', encoding="utf8")))
text_1 = data[4][3]+data[4][4]
tokens = nltk.word_tokenize(text_1)
nlp_text = nltk.Text(tokens)
f_dist_nlp_text = nltk.FreqDist(nlp_text)
keywords = sorted(w for w in set(nlp_text) if len(w)>=2 and f_dist_nlp_text[w]>1) 
english_stopwords = [w for w in stopwords.words('english')]
keywords = [w.lower() for w in keywords if w.lower() not in english_stopwords]
keywords = set([w for w in keywords if re.findall(r'^[a-z]+$',w)])
special_chars = [w for w in keywords if re.findall(r'[\.\+\,\;\*\(\)\{\}\[\]\$\&\%\^\#@0-9]', w)]
keyword_pos_tags = nltk.pos_tag(keywords)
[ tags[0] for tags in keyword_pos_tags]
keyword_nn = [ tags[0] for tags in keyword_pos_tags if tags[1]=='NN']
keywords_nn = set([w for w in keywords if re.findall(r'^[a-z]+$',w)])


raw_tags = nltk.pos_tag(nlp_text)
raw_nn = sorted(set([ tag[0] for tag in raw_tags if tag[1]=='NN' or tag[1]=='NNP']))
english_stopwords = [w for w in stopwords.words('english')]
keywords_nn = [w.lower() for w in keywords if w.lower() not in english_stopwords]

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/home/ubuntu/shared/opt/jobs/scrape/output/'
wordlists = PlaintextCorpusReader(corpus_root, '.csv')
wordlists.words('output_2.csv')



f_dist_nlp_text.most_common(50)

V = set(nlp_text)
long_words = [w for w in V if len(w) > 10]
sorted(long_words)

Fine gained selection of words

sorted(w for w in set(nlp_text) if len(w)>=4 and f_dist_nlp_text[w]>2) 

list(bigrams(nlp_text))
nlp_text.collocations()

fdist = FreqDist(len(w) for w in nlp_text)
fdist.max()
fdist.freq(3)
fdist[3]


Accessing text corpora.

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)

                  can could   may might  must  will
           news    93    86    66    38    50   389
       religion    82    59    78    12    54    71
        hobbies   268    58   131    22    83   264
science_fiction    16    49     4    12     8    16
        romance    74   193    11    51    45    43
          humor    16    30     8     8     9    13

genre_word = [ (genre, word) for genre in ['news', 'romance'] for word in brown.words(categories=genre)]
cfd = nltk.ConditionalFreqDist(genre_word)
genre_word[:4]
genre_word[-4:]
cfd.conditions()
['news', 'romance']
cfd['romance'].most_common()
cfd['romance']['could']

from nltk.corpus import inaugural
inaugural.fileids()
inaugural.fileids()[:4]
['1789-Washington.txt', '1793-Washington.txt', '1797-Adams.txt', '1801-Jefferson.txt']


Conditional Frequency.

file_genre = [(target,fileid[:4])
			for fileid in inaugural.fileids()
			for w in inaugural.words(fileid)
			for target in ['america', 'citizen']
			if w.lower().startswith(target)]
file_genre[:4]
[('citizen', '1789'), ('citizen', '1789'), ('citizen', '1789'), ('citizen', '1789')]
file_genre[-3:]
[('america', '2009'), ('america', '2009'), ('america', '2009')]
cfd = nltk.ConditionalFreqDist(file_genre)
cfd['america']
FreqDist({'1993': 33, '1997': 31, '2005': 30, '1921': 24, '1973': 23, '1985': 21, '2001': 20, '1981': 16, '2009': 15, '1909': 12, ...})
cfd.tabulate(conditions=['citizen'])
cfd.tabulate(conditions=['citizen'], samples=range(30))
         0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
citizen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
cfd.tabulate(conditions=['citizen'], samples=range(30), cumulative=True)
         0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
citizen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0

WordList Corpora + wordnet

Lemma :- Dictionary hearers.
Gloss :- Definitions.
Synsets :- Collection of synonymus words.
Lemma : Pairing of synset with word is called lemma.
From each synset we can get collection of lemmas.
Hyponyms navigate down --is-a lexical relation.
Hypernyms naviage up is-a lexical relation.
Meronyms :- navigate items to their components.
Part meronyms :- Components of the item .
Substance meronyms :- What the item is made of.
Holonyms :- Where the items are contained in.

from nltk.corpus import wordnet as wn
wn.synsets('breeze')
[Synset('breeze.n.01'), Synset('cinch.n.01'), Synset('breeze.v.01'), Synset('breeze.v.02')]
wn.synset('cinch.n.01').lemma_names()
['cinch', 'breeze', 'picnic', 'snap', 'duck_soup', "child's_play", 'pushover', 'walkover', 'piece_of_cake']
wn.synset('breeze.n.01').lemma_names()
['breeze', 'zephyr', 'gentle_wind', 'air']
wn.synset('breeze.n.01').definition()
'a slight wind (usually refreshing)'
wn.synset('breeze.n.01').lemmas()
[Lemma('breeze.n.01.breeze'), Lemma('breeze.n.01.zephyr'), Lemma('breeze.n.01.gentle_wind'), Lemma('breeze.n.01.air')]
wn.lemma('breeze.n.01.breeze')
Lemma('breeze.n.01.breeze')
wn.lemma('breeze.n.01.breeze').synset()
Synset('breeze.n.01')
wn.lemma('breeze.n.01.breeze').name()
wn.lemmas('breeze')
[Lemma('breeze.n.01.breeze'), Lemma('cinch.n.01.breeze'), Lemma('breeze.v.01.breeze'), Lemma('breeze.v.02.breeze')]

breeze=wn.synset('breeze.n.01')
types_of_breeze=breeze.hyponyms()
sorted(lemma.name() for synset in types_of_breeze for lemma in synset.lemmas())
['breath', 'fresh_breeze', 'gentle_breeze', 'light_air', 'light_breeze', 'moderate_breeze', 'sea_breeze', 'strong_breeze']

path = breeze.hypernym_paths()
path
[[Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('process.n.06'), Synset('phenomenon.n.01'), Synset('natural_phenomenon.n.01'), Synset('physical_phenomenon.n.01'), Synset('atmospheric_phenomenon.n.01'), Synset('weather.n.01'), Synset('wind.n.01'), Synset('breeze.n.01')]]
 wn.synset('wind.n.01').root_hypernyms()
[Synset('entity.n.01')]

Hyponyms --> More specifiic.
Hypernyms -> More generic. 

wn.synset('tree.n.01').part_meronyms()
[Synset('burl.n.02'), Synset('crown.n.07'), Synset('limb.n.02'), Synset('stump.n.01'), Synset('trunk.n.01')]
wn.synset('tree.n.01').substance_meronyms()
[Synset('heartwood.n.01'), Synset('sapwood.n.01')]
wn.synset('tree.n.01').member_holonyms()
[Synset('forest.n.01')]
for synset in wn.synsets('mint', wn.NOUN):
...     print(synset.name()+' : ',synset.definition()+' : ',synset.lemma_names())
...
batch.n.02 :  (often followed by `of') a large number or amount or extent :  ['batch', 'deal', 'flock', 'good_deal', 'great_deal', 'hatful', 'heap', 'lot', 'mass', 'mess', 'mickle', 'mint', 'mountain', 'muckle', 'passel', 'peck', 'pile', 'plenty', 'pot', 'quite_a_little', 'raft', 'sight', 'slew', 'spate', 'stack', 'tidy_sum', 'wad']
mint.n.02 :  any north temperate plant of the genus Mentha with aromatic leaves and small mauve flowers :  ['mint']
mint.n.03 :  any member of the mint family of plants :  ['mint']
mint.n.04 :  the leaves of a mint plant used fresh or candied :  ['mint']
mint.n.05 :  a candy that is flavored with a mint oil :  ['mint', 'mint_candy']
mint.n.06 :  a plant where money is coined by authority of the government :  ['mint']

Entailments rlexical relations :- 

wn.synsets('walk')
[Synset('walk.n.01'), Synset('base_on_balls.n.01'), Synset('walk.n.03'), Synset('walk.n.04'), Synset('walk.n.05'), Synset('walk.n.06'), Synset('walk_of_life.n.01'), Synset('walk.v.01'), Synset('walk.v.02'), Synset('walk.v.03'), Synset('walk.v.04'), Synset('walk.v.05'), Synset('walk.v.06'), Synset('walk.v.07'), Synset('walk.v.08'), Synset('walk.v.09'), Synset('walk.v.10')]
wn.synset('walk.v.01').entailments()
[Synset('step.v.01')]

Antonomy Lexical relation (between lemmas)

wn.synset('walk.v.01').lemmas()
[Lemma('walk.v.01.walk')]
wn.lemma('walk.v.01.walk').antonyms()
[Lemma('ride.v.02.ride')]

Find depth in Wordnet sysnsets :-

wn.synset('baggage.n.01').min_depth()
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
right.lowest_common_hypernyms(minke)
[Synset('baleen_whale.n.01')]

path_similarity :- gives the shortest path measurement.


#####
Process raw Text.
Unicode character processing :- To be followed later.

Regular expression.

# .	Wildcard, matches any character
# ^abc	Matches some pattern abc at the start of a string
# abc$	Matches some pattern abc at the end of a string
# [abc]	Matches one of a set of characters
# [A-Z0-9]	Matches one of a range of characters
# ed|ing|s	Matches one of the specified strings (disjunction)
# *	Zero or more of previous item, e.g. a*, [a-z]* (also known as Kleene Closure)
# # +	One or more of previous item, e.g. a+, [a-z]+
# ?	Zero or one of the previous item (i.e. optional), e.g. a?, [a-z]?
# {n}	Exactly n repeats where n is a non-negative integer
# {n,}	At least n repeats
# {,n}	No more than n repeats
# {m,n}	At least m and no more than n repeats
# a(b|c)+	Parentheses that indicate the scope of the operators
# \b	Word boundary (zero width)
# \d	Any decimal digit (equivalent to [0-9])
# \D	Any non-digit character (equivalent to [^0-9])
# \s	Any whitespace character (equivalent to [ \t\n\r\f\v])
# \S	Any non-whitespace character (equivalent to [^ \t\n\r\f\v])
# \w	Any alphanumeric character (equivalent to [a-zA-Z0-9_])
# \W	Any non-alphanumeric character (equivalent to [^a-zA-Z0-9_])
# \t	The tab character
# \n	The newline character

re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
['ing']
re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
['processing']
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
[('process', 'ing')]
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
[('process', 'es')]
re.findall(r"<a> (<.*>) <man>", text)

Text Normalization.
Stemming
porter = nltk.PorterStemmer()
[porter.stem(w) for w in keywords]
['air', 'airport', 'app', 'asia', 'bali', 'beach', 'big', 'chicken', 'comment', 'day', 'driver', 'email', 'facebook', 'final', 'french', 'fri', 'ganguli', 'get', 'grand', 'husband', 'idr', 'inr', 'inna', 'intern', 'kolkata', 'kuala', 'kuta', 'look', 'lumpur', 'malaysian', 'mr', 'pinterest', 'post', 'post', 'rice', 'ringgit', 'tamali', 'trip', 'twitter', 'age', 'airport', 'also', 'alway', 'anyth', 'area', 'around', 'ask', 'back', 'bag', 'baggag', 'balconi', 'bathroom', 'best', 'big', 'blue', 'bottl', 'breez', 'bright', 'broken', 'buy', 'came', 'chang', 'chicken', 'clean', 'clearli', 'come', 'constantli', 'convers', 'convers', 'counter', 'day', 'decid', 'desper', 'earli', 'enter', 'etc', 'everyon', 'everyth', 'exchang', 'experi', 'eye', 'fight', 'first', 'flight', 'food', 'full', 'get', 'go', 'golden', 'got', 'guest', 'guid', 'guy', 'hard', 'head', 'hotel', 'housekeep', 'huge', 'insid', 'item', 'journey', 'kg', 'know', 'ladi', 'last', 'light', 'light', 'like', 'link', 'long', 'look', 'look', 'loud', 'luggag', 'mani', 'meal', 'menu', 'minut', 'much', 'must', 'number', 'one', 'option', 'order', 'outsid', 'packag', 'pack', 'parti', 'peopl', 'pm', 'pool', 'price', 'provid', 'reach', 'reach', 'realli', 'recept', 'ribbon', 'room', 'saw', 'sea', 'section', 'see', 'servic', 'set', 'shoe', 'slowli', 'small', 'smile', 'someon', 'start', 'still', 'stood', 'tie', 'time', 'told', 'took', 'tour', 'toward', 'tri', 'trip', 'tri', 'two', 'type', 'us', 'use', 'view', 'water', 'way', 'weight', 'went', 'window', 'year']

lancaster = nltk.LancasterStemmer()
[lancaster.stem(w) for w in keywords]
['air', 'airport', 'ap', 'as', 'bal', 'beach', 'big', 'chick', 'com', 'day', 'driv', 'email', 'facebook', 'fin', 'french', 'fri', 'gangu', 'get', 'grand', 'husband', 'idr', 'inr', 'inn', 'intern', 'kolkat', 'kual', 'kut', 'look', 'lump', 'malays', 'mr', 'pinterest', 'post', 'post', 'ric', 'ringgit', 'tamal', 'trip', 'twit', 'ag', 'airport', 'also', 'alway', 'anyth', 'are', 'around', 'ask', 'back', 'bag', 'bag', 'balcony', 'bathroom', 'best', 'big', 'blu', 'bottl', 'breez', 'bright', 'brok', 'buy', 'cam', 'chang', 'chick', 'cle', 'clear', 'com', 'const', 'convers', 'convert', 'count', 'day', 'decid', 'desp', 'ear', 'ent', 'etc', 'everyon', 'everyth', 'exchang', 'expery', 'ey', 'fight', 'first', 'flight', 'food', 'ful', 'get', 'go', 'gold', 'got', 'guest', 'guid', 'guy', 'hard', 'head', 'hotel', 'housekeep', 'hug', 'insid', 'item', 'journey', 'kg', 'know', 'lady', 'last', 'light', 'light', 'lik', 'link', 'long', 'look', 'look', 'loud', 'lug', 'many', 'meal', 'menu', 'minut', 'much', 'must', 'numb', 'on', 'opt', 'ord', 'outsid', 'pack', 'pack', 'party', 'peopl', 'pm', 'pool', 'pric', 'provid', 'reach', 'reach', 'real', 'receiv', 'ribbon', 'room', 'saw', 'sea', 'sect', 'see', 'serv', 'set', 'sho', 'slow', 'smal', 'smil', 'someon', 'start', 'stil', 'stood', 'tied', 'tim', 'told', 'took', 'tour', 'toward', 'tri', 'trip', 'try', 'two', 'typ', 'us', 'us', 'view', 'wat', 'way', 'weight', 'went', 'window', 'year']

wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]
['air', 'airport', 'apps', 'asia', 'bali', 'beach', 'big', 'chicken', 'comment', 'day', 'driver', 'email', 'facebook', 'finally', 'french', 'fried', 'ganguly', 'get', 'grand', 'husband', 'idr', 'inr', 'inna', 'international', 'kolkata', 'kuala', 'kuta', 'looked', 'lumpur', 'malaysian', 'mr', 'pinterest', 'posted', 'post', 'rice', 'ringgit', 'tamali', 'trip', 'twitter', 'age', 'airport', 'also', 'always', 'anything', 'area', 'around', 'asked', 'back', 'bag', 'baggage', 'balcony', 'bathroom', 'best', 'big', 'blue', 'bottle', 'breeze', 'bright', 'broken', 'buy', 'came', 'change', 'chicken', 'clean', 'clearly', 'coming', 'constantly', 'conversation', 'conversion', 'counter', 'day', 'decided', 'desperately', 'early', 'entered', 'etc', 'everyone', 'everything', 'exchange', 'experience', 'eye', 'fight', 'first', 'flight', 'food', 'full', 'get', 'go', 'golden', 'got', 'guest', 'guided', 'guy', 'hard', 'headed', 'hotel', 'housekeeping', 'huge', 'inside', 'item', 'journey', 'kg', 'know', 'lady', 'last', 'light', 'light', 'like', 'link', 'long', 'look', 'looked', 'loud', 'luggage', 'many', 'meal', 'menu', 'minute', 'much', 'must', 'number', 'one', 'option', 'ordered', 'outside', 'package', 'packing', 'party', 'people', 'pm', 'pool', 'price', 'provide', 'reach', 'reaching', 'really', 'reception', 'ribbon', 'room', 'saw', 'sea', 'section', 'see', 'service', 'set', 'shoe', 'slowly', 'small', 'smile', 'someone', 'started', 'still', 'stood', 'tied', 'time', 'told', 'took', 'tour', 'towards', 'tried', 'trip', 'trying', 'two', 'type', 'u', 'used', 'view', 'water', 'way', 'weight', 'went', 'window', 'year']

text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)    # set flag to allow verbose regexps
...     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
...   | \w+(-\w+)*        # words with optional internal hyphens
...   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
...   | \.\.\.            # ellipsis
...   | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
... '''
nltk.regexp_tokenize(text, pattern)
['That', 'U.S.A.', 'poster-print', 'costs', '$12.40', '...']

nltk.corpus.indian.tagged_words()
Sentence Segmentation :-
sents = nltk.sent_tokenize(text_1)
print(str(len(words)), file=output_file)

count, total = 3205, 9375
"accuracy for {} words: {:.4%}".format(total, count / total)
'accuracy for 9375 words: 34.1867%'


Tagging

raw_tags = nltk.pos_tag(nlp_text)
raw_nn = sorted(set([ tag[0] for tag in raw_tags if tag[1]=='NN' or tag[1]=='NNP']))
english_stopwords = [w for w in stopwords.words('english')]
keywords_nn = [w.lower() for w in keywords if w.lower() not in english_stopwords]

nltk.corpus.brown.tagged_words()
[('The', 'AT'), ('Fulton', 'NP-TL'), ...]
nltk.corpus.indian.tagged_words()

Tag	Meaning	English Examples
ADJ	adjective	new, good, high, special, big, local
ADP	adposition	on, of, at, with, by, into, under
ADV	adverb	really, already, still, early, now
CONJ	conjunction	and, or, but, if, while, although
DET	determiner, article	the, a, some, most, every, no, which
NOUN	noun	year, home, costs, time, Africa
NUM	numeral	twenty-four, fourth, 1991, 14:24
PRT	particle	at, on, out, over per, that, up, with
PRON	pronoun	he, their, her, its, my, I, us
VERB	verb	is, say, told, given, playing, would
.	punctuation marks	. , ; !
X	other	ersatz, esprit, dunno, gr8, univeristy

>>> tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
>>> nltk.FreqDist(tags)
FreqDist({'NN': 13162, 'IN': 10616, 'AT': 8893, 'NP': 6866, ',': 5133, 'NNS': 5066, '.': 4452, 'JJ': 4392, 'CC': 2664, 'VBD': 2524, ...})

Default Taggers
>>> raw = 'My name is Sam'
>>> tokens = nltk.word_tokenize(raw)
>>> tokens
['My', 'name', 'is', 'Sam']
>>> defaulttagger = nltk.DefaultTagger('NN')
>>> defaulttagger.tag(tokens)
[('My', 'NN'), ('name', 'NN'), ('is', 'NN'), ('Sam', 'NN')]

Regular Expression Tagger.
>>> patterns = [
...     (r'.*ing$', 'VBG'),
...     (r'.*ed$', 'VBD'),
...     (r'.*es$', 'VBZ'),
...     (r'.*ould$', 'MD'),
...     (r'.*\'s$', 'NN$'),
...     (r'.*s$', 'NNS'),
...     (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
...     (r'.*', 'NN')
... ]
>>> regexp_tagger = nltk.RegexpTagger(patterns)
>>> regexp_tagger.tag(tokens)
[('My', 'NN'), ('name', 'NN'), ('is', 'NNS'), ('Sam', 'NN')]

Lookup Taggger.
>>> from nltk.corpus import brown
>>> fd = nltk.FreqDist(brown.words(categories='news'))
>>> cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
>>> most_freq_words = fd.most_common(100)
>>> cfd.conditions()
>>> cfd['The']
FreqDist({'AT': 775, 'AT-TL': 28, 'AT-HL': 3})
>>> likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
>>> baseline_tagger = nltk.UnigramTagger(model=likely_tags)
>>> brown_tagged_sents = brown.tagged_sents()
>>> baseline_tagger.evaluate(brown_tagged_sents)
0.4696708210184018

Unigram Tagger :-
For each token assign the tag which is most likely applicable for that token. Unigram tagger is set up via training.
>>> brown.categories()
['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
>>> tag_sents=brown.tagged_sents(categories='hobbies')
>>> sents = brown.sents(categories='hobbies')
>>> unigram_tagger=nltk.UnigramTagger(tag_sents)
>>> unigram_tagger.tag(sents[0])
[('Too', 'QL'), ('often', 'RB'), ('a', 'AT'), ('beginning', 'VBG'), ('bodybuilder', 'NN'), ('has', 'HVZ'), ('to', 'TO'), ('do', 'DO'), ('his', 'PP$'), ('training', 'NN'), ('secretly', 'RB'), ('either', 'CC'), ('because', 'CS'), ('his', 'PP$'), ('parents', 'NNS'), ("don't", 'DO*'), ('want', 'VB'), ('sonny-boy', 'NN'), ('to', 'TO'), ('``', '``'), ('lift', 'VB'), ('all', 'ABN'), ('those', 'DTS'), ('old', 'JJ'), ('barbell', 'NN'), ('things', 'NNS'), ("''", "''"), ('because', 'CS'), ('``', '``'), ("you'll", 'PPSS+MD'), ('stunt', 'VB'), ('your', 'PP$'), ('growth', 'NN'), ("''", "''"), ('or', 'CC'), ('because', 'CS'), ('childish', 'JJ'), ('taunts', 'NNS'), ('from', 'IN'), ('his', 'PP$'), ('schoolmates', 'NNS'), (',', ','), ('like', 'CS'), ('``', '``'), ('Hey', 'UH'), ('lookit', 'VB+IN'), ('Mr.', 'NP'), ('America', 'NP'), (';', '.'), (';', '.')]
>>> unigram_tagger.evaluate(tag_sents)
0.9327463719715829
>>> size = int(len(tag_sents)*0.9)
>>> train_sets = tag_sents[:size]
>>> test_sets = tag_sents[size:]
>>> u_tagger = nltk.UnigramTagger(train_sets)
>>> u_tagger.evaluate(test_sets)
0.7931999139229611
#N-gram Tagger :-Assign the tag to a token which is most likely applicable to current token and n-1 preceeding token.
>>> b_tagger = nltk.BigramTagger(train_sets)
>>> b_tagger.tag(test_sets[0])
[(('This', 'DT'), None), (('function', 'NN'), None), (('is', 'BEZ'), None), (('staffed', 'VBN'), None), (('by', 'IN'), None), (('engineers', 'NNS'), None), (('chosen', 'VBN'), None), (('for', 'IN'), None), (('their', 'PP$'), None), (('technical', 'JJ'), None), (('competence', 'NN'), None), (('and', 'CC'), None), (('who', 'WPS'), None), (('have', 'HV'), None), (('the', 'AT'), None), (('title', 'NN'), None), ((',', ','), None), (('member', 'NN'), None), (('of', 'IN'), None), (('the', 'AT'), None), (('technical', 'JJ'), None), (('staff', 'NN'), None), (('.', '.'), None)]
>>> b_tagger.evaluate(test_sets)
0.10038734667527437
sparse data problem :- As n gets larger, the specificity of the contexts increases, as does the chance 
 that the data we wish to tag contains contexts that were not present in the training data. 
This is known as the sparse data problem, and is quite pervasive in NLP. As a consequence, there is a trade-off between 
the accuracy and the coverage of our results (and this is related to the precision/recall trade-off in information retrieval).

#Combining Taggers :-
>>> t0 = nltk.DefaultTagger('NN')
>>> t1 = nltk.UnigramTagger(test_sets, backoff=t0)
>>> t2 = nltk.BigramTagger(test_sets, backoff=t1)
>>> t2.evaluate(test_sets)
0.9794491069507208
>>> t2.tag(test_sets[10])
[(('Fundamental', 'JJ'), 'NN'), (('to', 'IN'), 'NN'), (('the', 'AT'), 'NN'), (('difficulty', 'NN'), 'NN'), (('of', 'IN'), 'NN'), (('creating', 'VBG'), 'NN'), (('the', 'AT'), 'NN'), (('desired', 'VBN'), 'NN'), (('prestige', 'NN'), 'NN'), (('is', 'BEZ'), 'NN'), (('the', 'AT'), 'NN'), (('fact', 'NN'), 'NN'), (('that', 'CS'), 'NN'), ((',', ','), 'NN'), (('in', 'IN'), 'NN'), (('the', 'AT'), 'NN'), (('business', 'NN'), 'NN'), (('community', 'NN'), 'NN'), ((',', ','), 'NN'), (('prestige', 'NN'), 'NN'), (('and', 'CC'), 'NN'), (('status', 'NN'), 'NN'), (('are', 'BER'), 'NN'), (('conferred', 'VBN'), 'NN'), (('in', 'IN'), 'NN'), (('proportion', 'NN'), 'NN'), (('to', 'IN'), 'NN'), (('the', 'AT'), 'NN'), (('authority', 'NN'), 'NN'), (('that', 'WPO'), 'NN'), (('one', 'CD'), 'NN'), (('man', 'NN'), 'NN'), (('has', 'HVZ'), 'NN'), (('over', 'IN'), 'NN'), (('others', 'NNS'), 'NN'), (('and', 'CC'), 'NN'), (('the', 'AT'), 'NN'), (('extent', 'NN'), 'NN'), (('of', 'IN'), 'NN'), (('which', 'WDT'), 'NN'), (('he', 'PPS'), 'NN'), (('participates', 'VBZ'), 'NN'), (('in', 'IN'), 'NN'), (('the', 'AT'), 'NN'), (('management', 'NN'), 'NN'), (('functions', 'NNS'), 'NN'), (("''", "''"), 'NN'), (('.', '.'), 'NN')]

>>> from pickle import dump
>>> output = open('t2.pkl', 'wb')
>>> dump(t2, output, -1)
>>> output.close()
>>> output = open('D://Samriddha/personal/projects/sample_data/t2.pkl', 'wb')
>>> dump(t2, output, -1)
>>> output.close()
>>> from pickle import load
>>> input = open('D://Samriddha/personal/projects/sample_data/t2.pkl', 'rb')
>>> tagger = load(input)
>>> text = """The board's action shows what free enterprise
... is up against in our complex maze of regulatory laws ."""
>>> tokens = text.split()
>>> tokens
['The', "board's", 'action', 'shows', 'what', 'free', 'enterprise', 'is', 'up', 'against', 'in', 'our', 'complex', 'maze', 'of', 'regulatory', 'laws', '.']
>>> tagger.tag(tokens)
[('The', 'AT'), ("board's", 'NN'), ('action', 'NN'), ('shows', 'VBZ'), ('what', 'WDT'), ('free', 'JJ'), ('enterprise', 'NN'), ('is', 'BEZ'), ('up', 'RP'), ('against', 'IN'), ('in', 'IN'), ('our', 'PP$'), ('complex', 'JJ'), ('maze', 'NN'), ('of', 'IN'), ('regulatory', 'NN'), ('laws', 'NN'), ('.', '.')]

#Performance Limitations.

#Brills Taggin Transformation based learning :
The general idea is very simple: guess the tag of each word, then go back and fix the mistakes. 
In this way, a Brill tagger successively transforms a bad tagging of a text into a better one.

As with n-gram tagging, this is a supervised learning method, since we need annotated training data to figure out whether 
the taggers guess is a mistake or not. 
However, unlike n-gram tagging, it does not count observations but compiles a list of transformational correction rules

In general, linguists use morphological, syntactic, and semantic clues to determine the category of a word

Morphological Clues:
 The internal structure of a word may give useful clues as to the words category. 
For example, -ness is a suffix that combines with an adjective to produce a noun, e.g. happy → happiness, ill → illness. 
So if we encounter a word that ends in -ness, this is very likely to be a noun. Similarly, -ment is a suffix that 
combines with some verbs to produce a noun, e.g. govern → government and establish → establishment.
English verbs can also be morphologically complex. For instance, the present participle of a verb ends in -ing, and 
expresses the idea of ongoing, incomplete action (e.g. falling, eating). The -ing suffix also appears on nouns 
derived from verbs, e.g. the falling of the leaves (this is known as the gerund).

Syntactic Clues:
 Then we might say that a syntactic criterion for an adjective in English is 
 that it can occur immediately before a noun, or immediately following the words be or very

Semantic Clues:
 Finally, the meaning of a word is a useful clue as to its lexical category. 
 For example, the best-known definition of a noun is semantic: "the name of a person, place or thing". Within 
 modern linguistics, semantic criteria for word classes are treated with suspicion, mainly because they are hard to 
 formalize. Nevertheless, semantic criteria underpin many of our intuitions about word classes, and enable us to make a 
 good guess about the categorization of words in languages that we are unfamiliar with

New words
 All languages acquire new lexical items. A list of words recently added to the Oxford Dictionary of English 
 includes cyberslacker, fatoush, blamestorm, SARS, cantopop, bupkis, noughties, muggle, and robata. Notice that all 
 these new words are nouns, and this is reflected in calling nouns an open class. By contrast, prepositions are regarded as 
 a closed class.

Text Classifications :-



def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab
    word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()




def lexical_diversity(text):
	return len(set(text))/len(text)

def unusualwords(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = [val for val in text_vocab if val not in english_vocab]
	return unusual

def usualwords(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	usual=[val for val in text_vocab if val in english_vocab]

