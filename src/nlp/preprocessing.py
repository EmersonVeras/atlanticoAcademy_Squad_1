import nltk
import stanza
# import src.utils.downloads

class TextPreprocessor:

    def transform(self, text):
        nlp = stanza.Pipeline(lang='pt', processors='tokenize,mwt,pos,lemma')
        tokens = []
        pos = set()
        for sent in nlp(text.lower()).sentences:
            for word in sent.words:
                if not word.pos in ['PUNCT', 'NUM', 'DET', 'SYM']:
                    pos.add(word.pos)
                    tokens.append(word.lemma)
        
        stopwords = nltk.corpus.stopwords.words('portuguese')
               
        return [token for token in tokens if not token in stopwords]


