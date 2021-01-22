from textblob import TextBlob
words = ["mahine" , "engne"]
corrected_words = []
for i in words:
    corrected_words.append(str(TextBlob(i).correct()))
for i in range(len(words)):
    print("Word before correction : "+words[i]+" ; After Correction: "+corrected_words[i])