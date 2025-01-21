from artists import *

def get_artist(answers):
    if answers['6'] == "rap":
        artist_id = rap_artist_mappings[tuple(answers.values())]
    elif answers['6'] == "pop":
        del answers["1"]
        del answers["6"]
        artist_id = pop_artist_mappings[tuple(answers.values())]
    elif answers['6'] == "rock":
        del answers["1"]
        del answers["6"]
        artist_id = rock_artist_mappings[tuple(answers.values())]
    else:
        del answers["1"]
        del answers["6"]
        artist_id = varied_artist_mappings[tuple(answers.values())]

    print("IM SEARCHING FOR", artist_id)

    return artist_id