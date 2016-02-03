def limit_string_length():
    text = input('Insert some text: ')
    required_length = 10
    if len(text) >= required_length:
        result = text[:required_length] + "..."
    else:
        result = text
    print(result)

limit_string_length()
