from nltk.tokenize import RegexpTokenizer

def tokenize_without_punctuation(content): 

    content = str.casefold(content)
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(content)
