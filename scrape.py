"""
Iterate over the python files in the current directory, embed them with
some embedding model, store in csv.
"""
import pandas as pd


def remove_newlines(serie):
    serie = serie.str.replace("\n", " ")
    serie = serie.str.replace("\\n", " ")
    serie = serie.str.replace("  ", " ")
    serie = serie.str.replace("  ", " ")
    return serie


# texts will be a list of tuples (file name, text of the file)
texts = []
files = [
    "bench.py",
    "configurator.py",
    "model.py",
    "sample.py",
    "train.py",
]

# loop over files and read them
for file_name in files:
    # Open the file and read the text
    with open(f"./{file_name}", "r", encoding="UTF-8") as f:
        text = f.read()
        texts.append((file_name, text))

df = pd.DataFrame(texts, columns=["fname", "text"])
df["text"] = df.fname + ". " + remove_newlines(df.text)
df.to_csv("processed/scraped.csv")
print(df.head())

"""
import tiktoken

# Load the cl100k_base tokenizer which is designed to work with the ada-002 model
tokenizer = tiktoken.get_encoding("cl100k_base")

df = pd.read_csv("processed/scraped.csv", index_col=0)
df.columns = ["title", "text"]

# Tokenize the text and save the number of tokens to a new column
df["n_tokens"] = df.text.apply(lambda x: len(tokenizer.encode(x)))

# Visualize the distribution of the number of tokens per row using a histogram
df.n_tokens.hist()


max_tokens = 500


# Function to split the text into chunks of a maximum number of tokens
def split_into_many(text, max_tokens=max_tokens):
    # Split the text into sentences
    sentences = text.split(". ")

    # Get the number of tokens for each sentence
    n_tokens = [len(tokenizer.encode(" " + sentence)) for sentence in sentences]

    chunks = []
    tokens_so_far = 0
    chunk = []

    # Loop through the sentences and tokens joined together in a tuple
    for sentence, token in zip(sentences, n_tokens):
        # If the number of tokens so far plus the number of tokens in the current sentence is greater
        # than the max number of tokens, then add the chunk to the list of chunks and reset
        # the chunk and tokens so far
        if tokens_so_far + token > max_tokens:
            chunks.append(". ".join(chunk) + ".")
            chunk = []
            tokens_so_far = 0

        # If the number of tokens in the current sentence is greater than the max number of
        # tokens, go to the next sentence
        if token > max_tokens:
            continue

        # Otherwise, add the sentence to the chunk and add the number of tokens to the total
        chunk.append(sentence)
        tokens_so_far += token + 1

    return chunks


shortened = []

# Loop through the dataframe
for row in df.iterrows():
    # If the text is None, go to the next row
    if row[1]["text"] is None:
        continue

    # If the number of tokens is greater than the max number of tokens, split the text into chunks
    if row[1]["n_tokens"] > max_tokens:
        shortened += split_into_many(row[1]["text"])

    # Otherwise, add the text to the list of shortened texts
    else:
        shortened.append(row[1]["text"])
"""
