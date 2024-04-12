import fire
from nlplogic import corenlp
from corenlp import get_phrases

if __name__ == "__main__":
    fire.Fire(get_phrases)
