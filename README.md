# sentiment-analysis

Module Required
1. pandas
2. requets
3. bs4


Objective
The objective of this project is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below. 

Data Extraction
For each of the articles, given in the links.xlsx file, the article text is extracted and saved in a text file with URL_ID as its file name.

Data Analysis
For each of the extracted texts from the article, textual analysis is performed and variables are computed. The output is saved in “result.csv”




Text Analysis
Sentimental Analysis
Sentimental analysis is the process of determining whether a piece of writing is positive, negative, or neutral. It consists of steps:

Cleaning using Stop Words Lists
The Stop Words Lists (found in the folder words) are used to clean the text so that Sentiment Analysis can be performed by excluding the words found in Stop Words List. 

Creating a dictionary of Positive and Negative words
The Dictionary (found in the folder words) is used for creating a dictionary of Positive and Negative words. We add only those words in the dictionary if they are not found in the Stop Words Lists. 

Extracting Derived variables
Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
Negative Score: This score is calculated by assigning the value of +1 for each word if found in the Negative Dictionary and then adding up all the values.
Polarity Score: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 
Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1

Word Count
We count the total cleaned words present in the text by removing the stop words.