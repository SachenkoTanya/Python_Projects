def get_int(message):
    while True:
        try:
            max_value = int(input(message))
            return max_value
        except ValueError:
            print('Must be number!!!')
