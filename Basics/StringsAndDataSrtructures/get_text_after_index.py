def get_text_after_another_text():
    text1 = input("Insert some text: ")
    included_text = input('Insert text that is included in the above text: ')
    print(text1.split(included_text, 1)[-1])
    # index = text1.find(included_text)
    # if index > 0:
    #     print(text1[index + len(included_text):], end='')
    # else:
    #     print('Second text is not included in the first text.')

get_text_after_another_text()
