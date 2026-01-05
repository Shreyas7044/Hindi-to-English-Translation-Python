import pandas as pd
from googletrans import Translator

# Read Hindi words from CSV
data = pd.read_csv("hindi.csv")
print("Original Data:")
print(data)

# Initialize translator
translator = Translator()
translations = {}

# Translate each unique word
for column in data.columns:
    unique_values = data[column].unique()
    for element in unique_values:
        translations[element] = translator.translate(element).text

print("\nTranslations:")
for item in translations.items():
    print(item)

# Replace Hindi words with English translations
data.replace(translations, inplace=True)

print("\nTranslated Data:")
print(data)