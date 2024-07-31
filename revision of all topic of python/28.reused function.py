def emojis_converter(messages):
    words = message.split(' ')
    emojis = {
        ":)" : "smile",
        ":(" : "Sad" 
    }
    output = ""
    for word in words:
        output +=  emojis.get(word,word)
    return output
message = input("=")
print(emojis_converter(message))