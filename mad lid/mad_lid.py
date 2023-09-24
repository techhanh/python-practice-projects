def get_input(word_type):
    user_input = input(f'Enter {word_type}')
    return user_input

animal1 = get_input("animal")
verb1 = get_input("verb")
animal2 = get_input("different animal")
verb2 = get_input("different verb")
verb3 = get_input("another verb")

story = f"""
There once was a {animal1} who likes to {verb1}. 
The {animal1} met a {animal2} who likes to {verb2}.
The {animal1} said to the {animal2}: Do you want to {verb3} instead?
They both agreed and decided to {verb3} together.
"""

print(story)