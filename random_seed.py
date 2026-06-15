import random, string

def random_word(minlength: int, maxlength: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(random.randint(minlength, maxlength)))