from random import choice

capital = "\nCapital: 'Topeka'"

bird = "\nBird: 'Western Meadowlark'"

flower = "\nFlower: 'Sunflower'"

song = "\nSong: 'Home on the Range'"


def randomfunfact():
    funfacts = [
        "\nKansas is considered flat, but it does have a mountain.\n",
        "\nWichita is the largest city in the state, but many would guess that it is Kansas City.\n",
        "\nA considerable portion of Kansas City is actually in Missouri.\n",
        "\nMost Kansans are annoyed by Wizard of Oz references from people outside of Kansas.\n"
    ]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()

