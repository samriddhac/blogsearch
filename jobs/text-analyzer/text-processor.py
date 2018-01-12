import csv
import nltk
data = list(csv.reader(open('/home/ubuntu/shared/opt/jobs/scrape/output/output_2.csv')))
text_1 = data[4][3]+data[4][4]
tokens = nltk.word_tokenize(text_1)
nlp_text = nltk.Text(tokens)
keywords = sorted(w for w in set(nlp_text) if len(w)>=4 and f_dist_nlp_text[w]>2) 

f_dist_nlp_text = FreqDist(nlp_text)
f_dist_nlp_text.most_common(50)

V = set(nlp_text)
long_words = [w for w in V if len(w) > 10]
sorted(long_words)

/*Fine gained selection of words */
sorted(w for w in set(nlp_text) if len(w)>=4 and f_dist_nlp_text[w]>2) 

list(bigrams(nlp_text))
nlp_text.collocations()

fdist = FreqDist(len(w) for w in nlp_text)
fdist.max()
fdist.freq(3)
fdist[3]



def lexical_diversity(text):
	return len(set(text))/len(text)

