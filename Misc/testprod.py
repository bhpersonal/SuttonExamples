import numpy as np


def train_model(training_words, max_width = 3):

    models = []

    for width in xrange(0, max_width+1):


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

        models.append(model)

    return models



def get_next(output_words, models):


    for width in xrange(len(models)-1, -1, -1):

        if len(output_words) < width:
            #            return np.random.choice([np.random.choice(key) for key in models.keys()])
            continue

        key = tuple([s.lower() for s in output_words[-width:len(output_words)]])

        if not key in models[width]:
            continue

        freq = models[width][key]

        next_word = np.random.choice(freq[0], p=freq[1])
        return next_word




def generate_crap(training_words, n, max_width=3):

    models = train_model(training_words, max_width=max_width)

    output = []

    for i in xrange(0, n):

        output.append(get_next(output, models))

    return output


def load_bible(file_path):

    results = []

    with open(file_path) as f:

        for line in f:
            line = line [ line.index("\t") + 1: len(line)]
            results.extend([ s.strip()   for s in line.split(" ")])

    return [r for r in results if r.strip() != ""]

def load_20000_leagues(file_path):

    results = []

    with open(file_path) as f:

        for line in f:
            #line = line [ line.index("\t") + 1: len(line)]
            results.extend([ s.strip()   for s in line.split(" ")])

    return [r for r in results if r.strip() != ""]


if __name__ == "__main__":

    input = load_bible("C:/Users/Manas/Downloads/bible.txt/bible.txt")
    #input.extend(load_20000_leagues("C:/Users/Manas/Downloads/bible.txt/2000010.txt"))
    #input.extend(load_20000_leagues("C:/Users/Manas/Downloads/bible.txt/2000010.txt"))
    #input.extend(load_20000_leagues("C:/Users/Manas/Downloads/bible.txt/2000010.txt"))
    #input.extend(load_20000_leagues("C:/Users/Manas/Downloads/bible.txt/2000010.txt"))

    output = generate_crap(input, 2000, max_width=4)

    print " ".join(output)