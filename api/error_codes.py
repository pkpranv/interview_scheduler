# initialize error codes
error_codes = {
    '1': "Enter a valid email address.",
    '2': "user with this email already exists.",
    '3': "User name or password incorrect",
    '4': "Role doesnt exist",
    '5': "Invalid time format",
    '6': "Avilablity to should be greater than availablity from"
}


def get_error_code(messages):
    try:
        message = list(messages)[0][0]
    except TypeError:
        return
    if not message:
        return
    for error_code, msg in error_codes.items():
        if msg == message:
            return error_code
