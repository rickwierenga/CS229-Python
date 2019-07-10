import re
from nltk.stem import PorterStemmer
    
# Load vocabulary
vocabulary = []
with open('vocab.txt', 'r') as f:
    lines = f.readlines()
    vocabulary = [line[:-1] for line in lines]

def process_email(email_contents):
    """ preprocesses a the body of an email and returns a list of word_indices """
    global vocabulary

    # ----- Preprocess email -----

    # Lower case
    email_contents = email_contents.lower()

    # Remove all HTML
    html = re.compile(r'<[^<>]+>')
    email_contents = html.sub('', email_contents)

    # Handle numbers
    numbers = re.compile(r'[0-9]+')
    email_contents = numbers.sub('number', email_contents)

    # Handle URLs
    urls = re.compile(r'(http|https)://[^\s]*')
    email_contents = urls.sub('httpaddr', email_contents)

    # Email
    email_addresses = re.compile(r'[^\s]+@[^\s]+')
    email_contents = email_addresses.sub('emailaddr', email_contents)

    # Dollar sign
    dollar_sign = re.compile(r'[$]+')
    email_contents = dollar_sign.sub('dollar', email_contents)

    # ----- Tokenize email -----
    tokens = []
    words = re.split(r"\s|\@|\$|\/|\#|\.|\-|\:|\&|\*|\+|\=|\[|\]|\?|\!|\(|\)|\{|\}|\,|\'|\'|\"|\>|\_|\<|\;|\%", email_contents)

    stemmer = PorterStemmer()

    for word in words:
        # Remove nonalphanumeric characters
        alphanumeric = re.compile(r'[^a-zA-Z0-9]')
        word = alphanumeric.sub('', word)

        # Stem the word
        word = stemmer.stem(word)

        # Get index if it exists
        if word in vocabulary:
            tokens.append(vocabulary.index(word))
 
    return tokens

if __name__ == '__main__':
    # Run a test.
    # Note: the indexes are all 1 lower than the exercise, because Python is 0-indexed.
    with open('emailSample1.txt', 'r') as email:
        email_contents = email.read()
        tokens = process_email(email_contents)
        print(tokens)
