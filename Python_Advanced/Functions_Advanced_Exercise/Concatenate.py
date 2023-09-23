def concatenate(*words, **kwargs):
    text = ''.join(words)

    for key, value in kwargs.items():
        if key in text:
            text = text.replace(key, kwargs[key])

    return text
