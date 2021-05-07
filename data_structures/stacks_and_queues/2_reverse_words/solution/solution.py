
def reverse_words(sentence):
    # sentence_list = sentence.split(' ')
    # result =[]
    # for sentence in sentence_list:
    #     result.insert(0,sentence)
    # return " ".join(result)


    if sentence == '':
        return 
    sentence_list = sentence.split(' ')
    stack = []
    result = []
    for sentence in sentence_list:
        stack.append(sentence)
    while stack:
        result.append(stack.pop())
    return " ".join(result)




sentence = "hello bonjour aloha"
print(reverse_words(sentence)) #== "aloha bonjour hello"