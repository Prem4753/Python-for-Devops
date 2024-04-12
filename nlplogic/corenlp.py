from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """searching name in wikipedia"""
    print(f"searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """summarizing the name"""
    print(f"finding the wikipedia summary of the name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """getting text objects and returns"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """gets wikipedia name and returns phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
