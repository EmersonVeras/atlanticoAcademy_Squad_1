import nltk
import stanza

class TextPreprocessor:

    def transform(self, text):
        nlp = stanza.Pipeline(lang='pt', processors='tokenize,mwt,pos,lemma')
        tokens = []
        pos = set()
        for sent in nlp(text.lower()).sentences:
            for word in sent.words:
                if not word.pos in ['PUNCT', 'NUM', 'DET', 'SYM']:
                    pos.add(word.pos)
                    #print(word, word.lemma)
                    tokens.append(word.lemma)
        
        stopwords = nltk.corpus.stopwords.words('portuguese')

        print(pos)
               
        return [token for token in tokens if not token in stopwords]