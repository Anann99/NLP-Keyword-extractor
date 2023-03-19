#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from keybert import KeyBERT
import pandas as pd


# In[ ]:


url = input("Enter URL: ")


# In[ ]:


num_keywords = int(input("Enter the number of keywords to extract: "))


# In[ ]:


csv_path = input("Enter the path to the CSV file for evaluation: ")
eval_df = pd.read_csv(csv_path)
eval_dfs = eval_df.rename(columns={"text": "keyword"})
eval_dfs['given_score'] = eval_dfs[['relevance_x', 'relevance_y']].max(axis=1)
eval_dfs = eval_dfs.drop(columns=['relevance_x', 'relevance_y', 'dbpedia_resource', 'count'])
eval_dfs.head()


# In[ ]:


def extract_text_from_url(url):
    import requests
    from bs4 import BeautifulSoup

# Send a request to the webpage and retrieve its HTML code
    response = requests.get(url)
    html_code = response.content

# Parse the HTML code using Beautiful Soup
    soup = BeautifulSoup(html_code, "html.parser")

# Extract the text data from the webpage
    text_data = ""
    for element in soup.find_all("p"): # here we are extracting all the paragraph data
        text_data += element.get_text() + "\n"
    return text_data
# Print the text data
print (extract_text_from_url(url))


# In[ ]:


def extract_keywords(text, num_keywords):
    from keyphrase_vectorizers import KeyphraseCountVectorizer
    vectorizer = KeyphraseCountVectorizer()
    kw_model = KeyBERT(model='all-MiniLM-L6-v2')
    keywords = kw_model.extract_keywords(text, top_n= num_keywords, vectorizer=vectorizer,
                                       stop_words= 'english', use_maxsum=True, nr_candidates=40, use_mmr=True,
                                        diversity=0.2)
    return pd.DataFrame(keywords, columns=['keyword', 'extracted_score']).sort_values('extracted_score', ascending=False)


# In[ ]:


# Extract text from URL
text = extract_text_from_url(url)

# Extract keywords from text
keywords_df = extract_keywords(text, num_keywords)


# In[ ]:


print(keywords_df)


# In[ ]:


def evaluate_keywords(keywords_df, eval_dfs):
    common_keywords = pd.merge(keywords_df, eval_dfs, on='keyword')
    if len(common_keywords) == 0:
        return 0
    precision = len(common_keywords) / len(keywords_df.index)
    common_keywords['error'] = abs(common_keywords['extracted_score'] - common_keywords['given_score'])/common_keywords['given_score']
    return round(precision, 4) * 100, round(common_keywords['error'].mean(), 4) * 100, common_keywords


# In[ ]:


result = evaluate_keywords(keywords_df, eval_dfs)
print(result[2][['keyword', 'extracted_score', 'given_score', 'error']])
print('Therefore, the model results in a precision of ', result[0], '%.'' and an average error in relevant scores of  ', result[1], '%.')


# In[ ]:




