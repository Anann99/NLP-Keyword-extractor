import streamlit as st
import pandas as pd
from keywordmodel import extract_text_from_url, extract_keywords, evaluate_keywords

# Set app title
st.title("Keyword Extraction App")

# Get user input
url = st.text_input("Enter URL:")
num_keywords = st.number_input("Enter the number of keywords to extract:", min_value=1, step=1, value=10)
csv_path = st.text_input("Enter the path to the CSV file for evaluation:")

# Extract text from URL
text = extract_text_from_url(url)

# Extract keywords from text
keywords_df = extract_keywords(text, num_keywords)

# Evaluate keywords
if csv_path:
    eval_df = pd.read_csv(csv_path)
    eval_dfs = eval_df.rename(columns={"text": "keyword"})
    eval_dfs['given_score'] = eval_dfs[['relevance_x', 'relevance_y']].max(axis=1)
    eval_dfs = eval_dfs.drop(columns=['relevance_x', 'relevance_y', 'dbpedia_resource', 'count'])
    result = evaluate_keywords(keywords_df, eval_dfs)
    st.write("Evaluation Result:")
    st.write(result[2][['keyword', 'extracted_score', 'given_score', 'error']])
    st.write(f"Therefore, the model results in a precision of {result[0]}% and an average error in relevant scores of {result[1]}%.")