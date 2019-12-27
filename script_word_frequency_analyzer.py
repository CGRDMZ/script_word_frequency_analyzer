import urllib.request
import nltk
from nltk.corpus import stopwords # I have used nltk just for getting stopwords, not cleaning them.
from stop_words import get_stop_words
from matplotlib import pyplot as plt
import numpy as np
from tabulate import tabulate
from wordcloud import WordCloud

FILE_NAME_1 = "word_1.txt"
FILE_NAME_2 = "word_2.txt"


def main():
    try:
        stopwords.words('english')
    except:
        nltk.download('stopwords')

    while True:
        print("1- Check word frequency from file.")
        print("2- Find the frequency of common words.")
        print("3- Exit")

        stopwords_set = list(stopwords.words('english'))

        stopwords_set.extend(get_stop_words('en'))  # both library has most of the stop words, but not all, 
                                                    # so I have extended one with the other.
        option = int(input("please choose a menu:"))

        if option == 1:
            file = open(FILE_NAME_1, "r")

            print("1- load from file")
            print("2- load from internet")
            option_2 = int(input("choose one:"))

            # get the data based on user's choice
            if option_2 == 1:
                text = file.read()
            elif option_2 == 2:
                # open a connection to a URL using urllib
                url = str(input("please enter the ful url of the film script:")) # get full url for the script
                webUrl = urllib.request.urlopen(url) # opens the page
                text = webUrl.read().decode('iso-8859-1') # this should be charset of the page
                start_loc = text.find("<pre>")            # I hardcoded it because webUrl.headers.get_content_charset()
                end_loc = text.find("</pre>")             # function didn't work
                # byte_text = bytes(text[start_loc:end_loc], 'utf-8')
                text = text[start_loc:end_loc] # cropping the text between html <pre> elements

            # replace unwanted letters or tags
            text = text.replace("<b>", "").replace("</b>", "").replace("<pre>", "").replace("</pre>", "").replace("-", "").replace(":", "").replace(".", "").replace(",", "").replace(";", "").replace("?", "")#.replace("\\r", "").replace("\\n", "")

            file.close() # closes the file

            split_text = text.split() # splits the text into an array includes words

            filtered_text = []

            for word in split_text:
                if word.lower() not in stopwords_set:
                    filtered_text.append(word) # appends the word to filtered text if the 

            word_freq = dict()

            # if word exist in the dictionary add one if not add it with value 1
            for word in filtered_text:
                word = word.lower()
                if word_freq.get(word):
                    word_freq[word] = word_freq.get(word) + 1
                else:
                    word_freq[word] = 1
                                                    # sort by second value of dictionary
            sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

            print(tabulate(sorted_freq[:20], ["words", "frequency"]))

            wordcloud = WordCloud().generate_from_frequencies({i[0]:i[1] for i in sorted_freq}) # converts list to dict and generate word cloud
            plt.imshow(wordcloud, interpolation='bilinear') # shows word cloud
            plt.figure(figsize=(10,6))
            plt.bar([i[0] for i in sorted_freq[:20]], [i[1] for i in sorted_freq[:20]],width=0.5)
            plt.xticks(fontsize=14, rotation=90)
            plt.tight_layout() # adjusts everything, in order to be able to show in screen
            plt.xlabel("Words")
            plt.ylabel("Frequency")
            plt.show()
        elif option == 2:
            file_1 = open(FILE_NAME_1, "r")
            file_2 = open(FILE_NAME_2, "r")

            print("1- load from file")
            print("2- load from internet")
            option_2 = int(input("choose one:"))

            # get the data based on user's choice
            if option_2 == 1:
                text_1 = file_1.read()
                text_2 = file_2.read() 
            elif option_2 == 2:
                # open a connection to a URL using urllib
                url_1 = str(input("please enter the full url of the first film script:")) # get full url for the script
                url_2 = str(input("please enter the full url of the second film script:")) # get full url for the script
                webUrl_1 = urllib.request.urlopen(url_1) # opens the page
                webUrl_2 = urllib.request.urlopen(url_2) # opens the page
                text_1 = webUrl_1.read().decode('iso-8859-1') # this should be charset of the page
                text_2 = webUrl_2.read().decode('iso-8859-1') # this should be charset of the page
                start_loc_1 = text_1.find("<pre>")            # I hardcoded it because webUrl.headers.get_content_charset()
                start_loc_2 = text_2.find("<pre>")            # I hardcoded it because webUrl.headers.get_content_charset()
                end_loc_1 = text_1.find("</pre>")             # function didn't work
                end_loc_2 = text_2.find("</pre>")             # function didn't work
                # byte_text = bytes(text[start_loc:end_loc], 'utf-8')
                text_1 = text_1[start_loc_1:end_loc_1] # cropping the text between html <pre> elements
                text_2 = text_2[start_loc_2:end_loc_2] # cropping the text between html <pre> elements

            text_1 = text_1.replace("<b>", "").replace("</b>", "").replace("<pre>", "").replace("</pre>", "").replace("-", "").replace(":", "").replace(".", "").replace(",", "").replace(";", "").replace("?", "")
            text_2 = text_2.replace("<b>", "").replace("</b>", "").replace("<pre>", "").replace("</pre>", "").replace("-", "").replace(":", "").replace(".", "").replace(",", "").replace(";", "").replace("?", "")

            file_1.close()
            file_2.close()

            split_text_1 = text_1.split()
            split_text_2 = text_2.split()

            filtered_text_1 = []

            for word in split_text_1:
                if word.lower() not in stopwords_set:
                    filtered_text_1.append(word) # appends the word to filtered text if the 

            filtered_text_2 = []

            for word in split_text_2:
                if word.lower() not in stopwords_set:
                    filtered_text_2.append(word) # appends the word to filtered text if the 


            word_freq_1 = dict()
            word_freq_2 = dict()
            for word in filtered_text_1:
                word = word.lower()
                if word_freq_1.get(word):
                    word_freq_1[word] = word_freq_1.get(word) + 1
                else:
                    word_freq_1[word] = 1

            for word in filtered_text_2:
                word = word.lower()
                if word_freq_2.get(word):
                    word_freq_2[word] = word_freq_2.get(word) + 1
                else:
                    word_freq_2[word] = 1

            common_words = []

            for word in word_freq_1.keys():
                if word in word_freq_2:
                    common_words.append(word)

            zipped = []
            # zips these variables so, we can sort them by any value of its members
            for word in common_words[:20]:
                zipped.append((word, word_freq_1[word], word_freq_2[word], word_freq_1[word] + word_freq_2[word])) 

            # sorts words by total frequency
            zipped.sort(key=lambda x: x[3], reverse=True)

            #prints a proper table
            print(tabulate(zipped, ["words", "frequency_1", "frequency_2", "total_frequency"]))
            

            wordcloud = WordCloud().generate_from_frequencies({i[0]:i[3] for i in zipped})
            plt.imshow(wordcloud, interpolation='bilinear') # interpolation makes the image smoother

            fig, ax = plt.subplots(figsize=(14,5))
            x = np.arange(len(zipped))

            bar_width = 0.4
            
            plt.xticks(fontsize=14, rotation=90)

            plt.bar(x, [i[1] for i in zipped[:20]], width=bar_width, label="First Movie")
            plt.bar(x + bar_width, [i[2] for i in zipped[:20]], width=bar_width, label="Second Movie")

            ax.set_xticks(x + bar_width / 2)
            ax.set_xticklabels([i[0] for i in zipped[:20]])

            ax.legend() # shows legend

            plt.tight_layout() # adjusts everything, in order to be able to show in screen

            plt.xlabel("Words")
            plt.ylabel("Frequency")
            plt.show()

        elif option == 3:
            break
    

if __name__ == "__main__":
    main()