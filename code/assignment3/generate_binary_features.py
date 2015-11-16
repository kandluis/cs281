
import numpy as np

words_per_joke = []
current_joke = None
with open('jester_items.clean.dat') as f:
    new_joke = False
    for line in f:
        data = line.split()
        if len(data) == 0:
            continue
        if data[ 0 ][ -1 ] == ':':
            if current_joke is not None:
                words_per_joke.append(current_joke)
            current_joke = []
            current_joke.append(int(data[-1][ : -1]))
        else:
            current_joke.append(data)
words_per_joke.append(current_joke)

# We count the workds

from collections import Counter
cnt = Counter()
for i in range(len(words_per_joke)):
    for j in range(len(words_per_joke[ i ][ 1 ])):
        cnt[ words_per_joke[ i ][ 1 ][ j ] ] += 1

n_words = 150
most_common = cnt.most_common(n_words)
most_common = [ s[ 0 ] for s in most_common ]
X = np.zeros((len(words_per_joke), n_words), dtype = np.int)
for i in range(X.shape[ 0 ]):
    for j in range(len(most_common)):
        if most_common[ j ] in words_per_joke[ i ][ 1 ]:
            X[ words_per_joke[ i ][ 0 ] - 1, j ] = 1

X = np.concatenate((X, np.ones((X.shape[ 0 ], 1))), 1)

np.savetxt("X.txt", X, fmt = "%d")
