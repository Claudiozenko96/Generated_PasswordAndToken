import random 
import string



def main():

    seed = 27
    random.seed(seed)
    allowed_characters = string.ascii_letters + string.digits + string.punctuation

    characters_random = ''.join(random.choice(allowed_characters) for _ in range(15))
    print(f"Password: {characters_random}")


if __name__ == '__main__':
    main()

