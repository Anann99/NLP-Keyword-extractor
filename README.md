# Keyword Extraction App

This is a Streamlit app for extracting keywords from a web page and evaluating their relevance using an evaluation CSV file.

## Installation

To run this app, you need to have Python 3 installed on your system. You can install the dependencies using pip and the given requirements.txt file.

```bash
pip install -r requirements.txt
```
Alternatively, you also need to install the following dependencies:
- requests
- beautifulsoup4
- keybert
- pandas
- streamlit
- keyphrase-vectorizers

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4 keybert pandas streamlit keyphrase-vectorizers
```

## Usage

To run the app, navigate to the directory where the app files are located and run the following command:

```bash
streamlit run app.py
```

This will launch the app in your default web browser. Enter the URL of the web page you want to extract keywords from, the number of keywords to extract, and the path to the evaluation CSV file (optional). Click the "Extract Keywords" button to extract the keywords and display them on the screen. If you have provided an evaluation CSV file, the app will also display the evaluation result.

## Files

- `keywordmodel.py`: Python file containing the keyword extraction model code.
- `app.py`: Python file containing the Streamlit app code.
- `eval_dataset.csv`: Sample evaluation CSV file for the url https://jupiter.money/international-money-transfer/best-apps-to-send-money-abroad/(https://jupiter.money/international-money-transfer/best-apps-to-send-money-abroad/).
- `README.md`: This file.
- `requirements.txt`: Contains the dependancies that need to be installed on the system

## Credits

This app was created by [Anannya Mishra]. The keyword extraction model is based on the [KeyBERT](https://github.com/MaartenGr/KeyBERT) library by Maarten Grootendorst. The app was built using the [Streamlit](https://streamlit.io/) framework.

