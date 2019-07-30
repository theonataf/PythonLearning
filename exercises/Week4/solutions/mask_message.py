import random

with open('sowpods.txt', 'r') as f:
    words = [word.strip().lower() for word in f]


def get_random_words(length):
    random_words = random.choices(words, k=length)
    return random_words

def mask_message(message):
    message = message.split()
    random_words = get_random_words(len(message))
    masked_message = []
    for i in range(len(message)):
        masked_message.append(message[i])
        masked_message.append(random_words[i])

    return ' '.join(masked_message)

def unmask_message(message):
    message = message.split()
    unmasked = []
    length = len(message)
    for i in range(int(len(message)/2)):
        unmasked.append(message[i*2])

    return ' '.join(unmasked)

