
def read_messages_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def filter_spam_messages(messages, spam_words):
    filtered_messages = []
    nonspam_count = 0
    spam_count = 0
    
    for message in messages:
        if not any(word.lower() in message.lower() for word in spam_words):
            filtered_messages.append(message)
            nonspam_count += 1
        else:
            spam_count += 1
    
    return filtered_messages, nonspam_count, spam_count

spam_words = ["y?urs?lf", "??autiful"]

# Read messages from file
filename = "spam_nichtspam_datensatz.csv"
messages = read_messages_from_file(filename)

filtered, nonspam, spam = filter_spam_messages(messages, spam_words)

print(f"\nNonspam Messages : {nonspam}")
print(f"Spam messages: {spam}")
