# Keyword Extraction App

This is a Streamlit app for extracting keywords from a web page and evaluating their relevance using an evaluation CSV file.

## Installation

To run this app, you need to have Python 3 installed on your system. You also need to install the following dependencies:

- requests
- beautifulsoup4
- keybert
- pandas
- streamlit

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4 keybert pandas streamlit
```

## Usage

To run the app, navigate to the directory where the app files are located and run the following command:

```bash
streamlit run app.py
```

This will launch the app in your default web browser. Enter the URL of the web page you want to extract keywords from, the number of keywords to extract, and the path to the evaluation CSV file (optional). Click the "Extract Keywords" button to extract the keywords and display them on the screen. If you have provided an evaluation CSV file, the app will also display the evaluation result.

## Files

- `keyword_model.py`: Python file containing the keyword extraction model code.
- `app.py`: Python file containing the Streamlit app code.
- `eval_dataset.csv`: Sample evaluation CSV file.
- `README.md`: This file.

## Credits

This app was created by [Anannya Mishra]. The keyword extraction model is based on the [KeyBERT](https://github.com/MaartenGr/KeyBERT) library by Maarten Grootendorst. The app was built using the [Streamlit](https://streamlit.io/) framework.

