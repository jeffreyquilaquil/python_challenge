def mad_libs_generator():
    noun = input("Give me a noun: ")
    verb = input("Give me a verb: ")
    adjective = input("Give me an adjective: ")
    place = input("Give me a place: ")

    story = f"""
    Today I went to the {adjective} {place}.
    I saw a {noun} trying to {verb}.
    It was the most unforgettable day ever!
    """

    print(story)


if __name__ == '__main__':
    mad_libs_generator()