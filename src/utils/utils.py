import string


def filter_message(msg):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = msg.translate(translator)
    lowercased_text = cleaned_text.lower()

    return lowercased_text
