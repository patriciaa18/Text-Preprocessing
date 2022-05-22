# import libraries
from string import punctuation, digits
import nltk 
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

alphabet_list = list(string.ascii_lowercase)
# input text to txt
decision = input("Do you have any text? If no, we will process example text (y/n)")

if decision == "yes" or "y":
    text = str(input("Input text: "))
else:
    text = "Algorithms and data structures are central to computer science.[5] The theory of computation concerns abstract models of computation and general classes of problems that can be solved using them. The fields of cryptography and computer security involve studying the means for secure communication and for preventing security vulnerabilities. Computer graphics and computational geometry address the generation of images. Programming language theory considers approaches to the description of computational processes, and database theory concerns the management of repositories of data. Human–computer interaction investigates the interfaces through which humans and computers interact, and software engineering focuses on the design and principles behind developing software. Areas such as operating systems, networks and embedded systems investigate the principle and design behind complex systems! Computer architecture describes the construction of cmputer components and computer-operated equipment. Artificial intelligence and machine learnig aim to synthesize goal-orientated processes such as problem-solving, decision-making, environmental adaptation, planning; and learing found in humans and animals. Within artificial inteligence, computer vision aims to understand and process image and video data, while natural-language processing aims to understand and process textual, and linguistic data."

with open('file.txt', 'w') as f:
    f.write(text)

# load text, lowercase and remove -
with open('file.txt', 'r') as file:
    string_input = file.read().lower()
string_input = string_input.replace("-"," ")

# remove punctuation and numbers
string_input = string_input.translate(str.maketrans("","", punctuation))
string_input = string_input.translate(str.maketrans("","", digits))
string_input = string_input.split()
string_input = ' '.join([str(elem) for elem in string_input])
print("Punctuation removed \n{}\n".format(string_input))

# remove stop words and tokenize
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(string_input)
words = [i for i in tokens if not i in stop_words]
print("Stopwords removed \n{}\n".format(words))

# stemming
lemmatizer=WordNetLemmatizer()
words = [lemmatizer.lemmatize(word) for word in words]
words = ' '.join([str(elem) for elem in words])
print("Normalized text \n{}\n".format(words))

# unique words and processing
words = words.split()
dictionary = {}
  
for word in words:
    if (word[0] not in dictionary.keys()):
        dictionary[word[0]] = []
        dictionary[word[0]].append(word)
    else:
        if (word not in dictionary[word[0]]):
            dictionary[word[0]].append(word)

print("Unique words count: {}\n".format(len(set(words))))
print("Unique words are\n{}\n".format(set(words)))
print("List of unique words: \n")

for key in sorted(dictionary):
    if key in alphabet_list:
        dict_words = ", "
        print(key, "| count: ",len(dictionary[key]),"| ", dict_words.join(dictionary[key]))
    
