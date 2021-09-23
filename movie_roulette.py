import json
import random


def pick_a_light_movie():
    main_menu_ans = 0
    allowed = ["y", "n"]
    with open("movies.json", "r") as f:
        data = json.load(f)

    light_random = random.choice(data['light'])

    light_choice = light_random
    print("Your movie for tonight is  " + str(light_choice))
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        deleted = input("Do you want to delete this title from list? y/n")
        if deleted == "y":
            with open('movies.json', 'r') as fp:
                data = json.load(fp)

            data['light'].remove(light_choice)

            with open('movies.json', 'w') as fp:
                json.dump(data, fp, indent=2)
            print("""
            Movie has been deleted from list
            """)
            main_menu()
        elif deleted == "n":
            main_menu()


def check_answer(allowed, answer):
    if answer in allowed:
	    return "answer_allowed"
    else:
	    return "not_allowed"


def pick_a_dark_movie():
    main_menu_ans = 0
    allowed = ["y", "n"]
    with open("movies.json", "r") as f:
        data = json.load(f)

    dark_random = random.choice(data['dark'])

    print("Your movie for tonight is  " + str(dark_random))
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        deleted = input("Do you want to remove this title from list? y/n")
        if deleted == "y":
            with open('movies.json', 'r') as fp:
                data = json.load(fp)

            data['dark'].remove(dark_random)

            with open('movies.json', 'w') as fp:
                json.dump(data, fp, indent=2)
            print("""
            Movie has been deleted from list
            """)
            main_menu()
        elif deleted == "n":
            main_menu()


def add_a_dark_movie():
    new_movie_data = {}
    new_movie_data = input("Enter the title you want to add!")

    with open('movies.json', 'r') as fp:
        data = json.load(fp)

    data['dark'].append(new_movie_data)

    with open('movies.json', 'w') as fp:
        json.dump(data, fp, indent=2)
    print("""

    Movie has been added to gritty movie list!
    """)
    while len(new_movie_data) > 0:
        main_menu()


def add_a_light_movie():
    new_movie_data = {}
    new_movie_data = input("Enter the title you want to add!")

    with open('movies.json', 'r') as fp:
        data = json.load(fp)

    data['light'].append(new_movie_data)

    with open('movies.json', 'w') as fp:
        json.dump(data, fp, indent=2)
    print("""

        Movie has been added to light movie list!
        """)
    while len(new_movie_data) > 0:
        main_menu()


def genre_choice():
    main_menu_ans = 0
    allowed = ["1", "2", "3"]
    print("""

    How are you feeling today?

    1. I just want to have fun
    2. I'm ready for the heavy stuff
    3. Back
    """)
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        genre_ans = input("Write the number of the chosen option: ")
        if genre_ans == "1":
            pick_a_light_movie()
        elif genre_ans == "2":
            pick_a_dark_movie()
        elif genre_ans == "3":
            main_menu()


def addition_genre():
    print("""

    What kind of movie do you want to add?

    1. A light-hearted/comedy
    2. A sad/dark/gritty movie
    3. Back
    """)
    add_genre_ans = input("Write the number of the chosen option: ")
    if add_genre_ans == "1":
        add_a_light_movie()
    elif add_genre_ans == "2":
        add_a_dark_movie()
    elif add_genre_ans == "3":
        main_menu()

def quitting():
    main_menu_ans = 0
    allowed = ["y", "n"]
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        quit_ans = input("Are you sure? y or n ? ")
        while quit_ans == "n":
            main_menu()
        if quit_ans == "y":
            quit()

def main_menu():
    main_menu_ans = 0
    allowed = ["1", "2", "3"]
    print("""Movie Roulette
""")
    print("""    1. Pick a movie for me!
    2. Add a movie
    3. Quit
    """)
    while check_answer(allowed, main_menu_ans) != "answer_allowed":
        main_menu_ans = input(" Write the number of the chosen option: ")
    if main_menu_ans == "1":
        genre_choice()
    elif main_menu_ans == "2":
        addition_genre()
    elif main_menu_ans == "3":
        quitting()




main_menu()
