
# data from https://archive.ics.uci.edu/ml/datasets/sms+spam+collection

import string

items = []

print('reading SMSSpamCollection')
with open('SMSSpamCollection') as datafile: #, encoding='latin-1') as datafile:
    for line in datafile:
        row = line.rstrip().split('\t')
        # store first two fields as (label, message)
        items.append((row[0], row[1]))
print('read', len(items), 'items')
print()

print('first five items:')
for item in items[:5]:
    print(item)
print()

# very simple tokenizer that first strips punctuation
punct_stripper = str.maketrans(dict.fromkeys(string.punctuation))
def tokenize(s):
    return s.translate(punct_stripper).split()

print('tokenizing')
items = [(item[0], tokenize(item[1])) for item in items]
print()

print('first five tokenized items:')
for item in items[:5]:
    print(item)
print()

print('making 80/20 train/test split')
train_size = int(0.8 * len(items))
train_items, test_items = items[:train_size], items[train_size:]
print('train set size:', len(train_items))
print('test set size:', len(test_items))
print()

