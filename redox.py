
def remove_redundant_sentences(text):
    seen = set()
    result = []
    for sentence in text.split('.'):
        sentence = sentence.strip()
        if sentence and sentence not in seen:
            seen.add(sentence)
            result.append(sentence)
    return '. '.join(result) + '.'
