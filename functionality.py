# Map quiz answers to artist IDs
artist_mappings = {
    ('upbeat', 'pop', 'workout'): ['2CIMQHirSU0MQqyYHq0eOx'],  # Example: Dua Lipa
    ('calm', 'classical', 'relax'): ['57dN52uHvrHOxijzpIgu3E'],  # Example: Ludovico Einaudi
    ('happy', 'indie', 'driving'): ['1vCWHaC5f2uS3yhpwWbIA6'],  # Example: Tame Impala
    # You can expand this list based on more combinations
}

def get_artist_ids(answers):
    # Get the tuple of answers
    key = (answers['mood'], answers['genre'], answers['activity'])
    # Return the artist IDs corresponding to this key
    return artist_mappings.get(key, ['3TVXtAsR1Inumwj272M2M0'])  # Default: Drake's ID if no match

def get_artist(answers):
    if answers['genre'] == "pop":
        artist_info = get_pop_artist(answers)
    elif answers['genre'] == "rap":
        artist_info = get_rap_artist(answers)
    elif answers['genre'] == "rock":
        artist_info = get_rock_artist(answers)
    else:
        artist_info = get_else_artist(answers)
    return artist_info

def get_pop_artist(answers):
    # Question 2: Do you prefer chill or energetic?
    if answers["mood"] == 'energetic':
        # Question 4: Real instruments or electronic?
        if answers["instruments"] == 'electronic':
            # Question 5: Popular or not?
            if answers["popularity"] == 'popular':
                # Question 7: Group or solo?
                if answers["artist_type"] == 'group':
                    return ['6lS7iIOJjqKYFQonOHtW3z']  # The Chainsmokers
                else:
                    return ['1vCWHaC5f2uS3yhpwWbIA6']  # Tame Impala (solo, energetic, electronic)
            else:
                return ['4RwfXNmWJdGOMNSr1d9qOd']  # Example: A more niche, electronic artist Aphex Twin
        else:
            return ['2CIMQHirSU0MQqyYHq0eOx']  # Example: Dua Lipa (pop, upbeat, real instruments)
    else:
        # If calm or chill
        return ['57dN52uHvrHOxijzpIgu3E']  # Example: Ludovico Einaudi (classical, calm)

def get_rap_artist(answers):
    # Handle rap choices (you can expand on this further)
    if answers["mood"] == "chill":
        if answers["popularity"] == "popular":
            return ['6lS7iIOJjqKYFQonOHtW3z']  # Example: Travis Scott
        else:
            return ['5K4W6rqBFWDnAN6FQUk6lM']  # Example: A niche rap artist
    else:
        return ['4RwfXNmWJdGOMNSr1d9qOd']  # Example: Tupac (old-school rap)

def get_rock_artist(answers):
    # Handle rock choices (you can expand on this further)
    if answers["instruments"] == "real":
        if answers["popularity"] == "popular":
            return ['2V3tXr9pja2Bjo7Zf9GBM0']  # Led Zeppelin (classic, real instruments, popular)
        else:
            return ['7dq6Vmf6RxvQ4NEkBDiwDq']  # Foo Fighters (rock, real instruments, not so popular)
    else:
        return ['7dq6Vmf6RxvQ4NEkBDiwDq']  # Foo Fighters (rock, electronic)

def get_else_artist(answers):
    # Handle other genres or defaults
    return ['2CIMQHirSU0MQqyYHq0eOx']  # Default artist ID (e.g., Dua Lipa)