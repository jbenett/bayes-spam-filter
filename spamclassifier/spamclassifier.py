from spamreader import train_items, test_items

# Count of how many spam/ham emails in training set
spam_email_count = 0
ham_email_count = 0

# Total number of words observed in each category
spam_word_count = 0
ham_word_count = 0

# Dictionaies that record the occurences of words in both spam/ham emails
spam_wc_dict = {}
ham_wc_dict = {}

# loop over training set, counting the number of spam/ham emails and the number of occurences of words in them
for email in train_items:
    if email[0] == 'spam':
        spam_email_count = spam_email_count + 1
        for word in email[1]:
            spam_word_count += 1
            try:
                spam_wc_dict[word] += 1
            except KeyError:
                 spam_wc_dict[word] = 1
    else:
        ham_email_count += 1
        for word in email[1]:
            ham_word_count = ham_word_count + 1
            try:
                ham_wc_dict[word] += 1
            except KeyError:
                 ham_wc_dict[word] = 1

# Probability of spam/ham based on generated distribution
percent_spam = spam_email_count / (spam_email_count + ham_email_count)
percent_ham = ham_email_count / (spam_email_count + ham_email_count)

# Dictionaies that record the probabllity of (word | spam) and (word | ham)
spam_p_dict = {}
ham_p_dict = {}

# Fill in probabilities of word occuring in spam/ham emails.  TODO: Apply Laplace smoothing.
for word in spam_wc_dict:
    probability = (spam_wc_dict[word]) / (spam_word_count)
    spam_p_dict[word] = probability

for word in ham_wc_dict:
    probability = (ham_wc_dict[word]) / (ham_word_count)
    ham_p_dict[word] = probability

# Go through test_items and classify them
correct_guess = 0
incorrect_guess = 0
current_guess = 0
for email in test_items:
    p_spam = 1.0
    p_ham = 1.0
    # Calculate spam probablity
    for word in email[1]:
        try:
            p_spam = p_spam * spam_p_dict[word]
        except KeyError:
             continue
    # Calculate ham probability
    for word in email[1]:
        try:
            p_ham = p_ham * ham_p_dict[word]
        except KeyError:
            continue
    if current_guess < 50:
        print('Current Test Number: ' + str(current_guess))
        print('Spam Probability: ' + str(p_spam))
        print('Ham Probability: ' + str(p_ham))
        current_guess += 1

    if p_spam * percent_spam < p_ham * percent_ham:
        if email[0] == 'spam':
            correct_guess += 1
            if current_guess < 50:
                print('Classified as spam correctly')
        else:
            incorrect_guess += 1
    else:
        if email[0] == 'ham':
            correct_guess += 1
            if current_guess < 50:
                print('Classified as ham correctly')
        else:
            incorrect_guess += 1

print('Percentage of correct guesses: ')
print(correct_guess / (incorrect_guess + correct_guess) * 100)