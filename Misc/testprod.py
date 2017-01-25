import numpy as np


def train_model(training_words, width = 1):

    model = {}

    for i in xrange(width, len(training_words)):

        input_words = tuple([s.lower() for s in training_words[i-width : i]])
        output_word = training_words[i]

        model.setdefault(input_words, {}).setdefault(output_word, 0)
        model[input_words][output_word] += 1

    # normalize all weights
    for key in model:


        freq = model[key]
        count = sum(freq.values())

        next_words = freq.keys()
        next_word_probs = [ float(freq[next_word]) / float(count)  for next_word in next_words ]

        model[key] = (next_words, next_word_probs)

    return model


def get_next(output_words, model, width = 1):

    if len(output_words) < width:
        return np.random.choice([np.random.choice(key) for key in model.keys()])

    key = tuple([s.lower() for s in output_words[-width:len(output_words)]])
    freq = model[key]

    next_word = np.random.choice(freq[0], p=freq[1])
    return next_word




def generate_crap(training_words, n, width=1):

    model = train_model(training_words, width=width)

    output = []

    for i in xrange(0, n):

        output.append(get_next(output, model, width=width))

    return output


def load_bible(file_path):

    results = []

    with open(file_path) as f:

        for line in f:
            line = line [ line.index("\t") + 1: len(line)]
            results.extend([ s.strip()   for s in line.split(" ")])

    return [r for r in results if r.strip() != ""]

if __name__ == "__main__":

    input = load_bible("C:/Users/Manas/Downloads/bible.txt/bible.txt")

    output = generate_crap(input, 100)

    print " ".join(output)