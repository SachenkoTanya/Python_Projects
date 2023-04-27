def get_number(message, expected_type=float):
    user_input = input(message)
    try:
        converted_input = expected_type(user_input)
        return converted_input
    except ValueError:
        print(f'The value must be of type {expected_type.__name__}')
        return get_number(message, expected_type)
