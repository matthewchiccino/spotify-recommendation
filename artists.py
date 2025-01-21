# Map quiz answers to artist IDs
rap_artist_mappings = {
    # Drake, Chill
    ('drake', 'chill', 'new', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Partynextdoor'],
    ('drake', 'chill', 'new', 'no instruments', 'popular is fine', 'rap', 'group'): ['Dreamville'],
    ('drake', 'chill', 'new', 'no instruments', 'popular is bad', 'rap', 'solo'): ['J. Cole'],
    ('drake', 'chill', 'new', 'no instruments', 'popular is bad', 'rap', 'group'): ['Brockhampton'],
    ('drake', 'chill', 'new', 'instruments', 'popular is fine', 'rap', 'solo'): ['Anderson .Paak'],
    ('drake', 'chill', 'new', 'instruments', 'popular is fine', 'rap', 'group'): ['The Internet'],
    ('drake', 'chill', 'new', 'instruments', 'popular is bad', 'rap', 'solo'): ['Tyler, the Creator'],
    ('drake', 'chill', 'new', 'instruments', 'popular is bad', 'rap', 'group'): ['The Roots'],
    ('drake', 'chill', 'old', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Lauryn Hill'],
    ('drake', 'chill', 'old', 'no instruments', 'popular is fine', 'rap', 'group'): ['A Tribe Called Quest'],
    ('drake', 'chill', 'old', 'no instruments', 'popular is bad', 'rap', 'solo'): ['MF DOOM'],
    ('drake', 'chill', 'old', 'no instruments', 'popular is bad', 'rap', 'group'): ['Digable Planets'],
    ('drake', 'chill', 'old', 'instruments', 'popular is fine', 'rap', 'solo'): ['Common'],
    ('drake', 'chill', 'old', 'instruments', 'popular is fine', 'rap', 'group'): ['The Fugees'],
    ('drake', 'chill', 'old', 'instruments', 'popular is bad', 'rap', 'solo'): ['Mos Def'],
    ('drake', 'chill', 'old', 'instruments', 'popular is bad', 'rap', 'group'): ['Gang Starr'],

    # Drake, Energetic
    ('drake', 'energetic', 'new', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Lil Baby'],
    ('drake', 'energetic', 'new', 'no instruments', 'popular is fine', 'rap', 'group'): ['Migos'],
    ('drake', 'energetic', 'new', 'no instruments', 'popular is bad', 'rap', 'solo'): ['Playboi Carti'],
    ('drake', 'energetic', 'new', 'no instruments', 'popular is bad', 'rap', 'group'): ['Run the Jewels'],
    ('drake', 'energetic', 'new', 'instruments', 'popular is fine', 'rap', 'solo'): ['Kendrick Lamar'],
    ('drake', 'energetic', 'new', 'instruments', 'popular is fine', 'rap', 'group'): ['EarthGang'],
    ('drake', 'energetic', 'new', 'instruments', 'popular is bad', 'rap', 'solo'): ['Denzel Curry'],
    ('drake', 'energetic', 'new', 'instruments', 'popular is bad', 'rap', 'group'): ['Flatbush Zombies'],
    ('drake', 'energetic', 'old', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Kanye West'],
    ('drake', 'energetic', 'old', 'no instruments', 'popular is fine', 'rap', 'group'): ['N.W.A.'],
    ('drake', 'energetic', 'old', 'no instruments', 'popular is bad', 'rap', 'solo'): ['DMX'],
    ('drake', 'energetic', 'old', 'no instruments', 'popular is bad', 'rap', 'group'): ['Wu-Tang Clan'],
    ('drake', 'energetic', 'old', 'instruments', 'popular is fine', 'rap', 'solo'): ['Tupac'],
    ('drake', 'energetic', 'old', 'instruments', 'popular is fine', 'rap', 'group'): ['Outkast'],
    ('drake', 'energetic', 'old', 'instruments', 'popular is bad', 'rap', 'solo'): ['Big L'],
    ('drake', 'energetic', 'old', 'instruments', 'popular is bad', 'rap', 'group'): ['Public Enemy'],

    # Kendrick, Chill
    ('kendrick', 'chill', 'new', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Anderson .Paak'],
    ('kendrick', 'chill', 'new', 'no instruments', 'popular is fine', 'rap', 'group'): ['Dreamville'],
    ('kendrick', 'chill', 'new', 'no instruments', 'popular is bad', 'rap', 'solo'): ['J. Cole'],
    ('kendrick', 'chill', 'new', 'no instruments', 'popular is bad', 'rap', 'group'): ['Brockhampton'],
    ('kendrick', 'chill', 'new', 'instruments', 'popular is fine', 'rap', 'solo'): ['Tyler, the Creator'],
    ('kendrick', 'chill', 'new', 'instruments', 'popular is fine', 'rap', 'group'): ['The Internet'],
    ('kendrick', 'chill', 'new', 'instruments', 'popular is bad', 'rap', 'solo'): ['Saba'],
    ('kendrick', 'chill', 'new', 'instruments', 'popular is bad', 'rap', 'group'): ['The Roots'],
    ('kendrick', 'chill', 'old', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Lauryn Hill'],
    ('kendrick', 'chill', 'old', 'no instruments', 'popular is fine', 'rap', 'group'): ['A Tribe Called Quest'],
    ('kendrick', 'chill', 'old', 'no instruments', 'popular is bad', 'rap', 'solo'): ['MF DOOM'],
    ('kendrick', 'chill', 'old', 'no instruments', 'popular is bad', 'rap', 'group'): ['Digable Planets'],
    ('kendrick', 'chill', 'old', 'instruments', 'popular is fine', 'rap', 'solo'): ['Common'],
    ('kendrick', 'chill', 'old', 'instruments', 'popular is fine', 'rap', 'group'): ['The Fugees'],
    ('kendrick', 'chill', 'old', 'instruments', 'popular is bad', 'rap', 'solo'): ['Mos Def'],
    ('kendrick', 'chill', 'old', 'instruments', 'popular is bad', 'rap', 'group'): ['Gang Starr'],

    # Kendrick, Energetic
    ('kendrick', 'energetic', 'new', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Lil Baby'],
    ('kendrick', 'energetic', 'new', 'no instruments', 'popular is fine', 'rap', 'group'): ['Migos'],
    ('kendrick', 'energetic', 'new', 'no instruments', 'popular is bad', 'rap', 'solo'): ['Playboi Carti'],
    ('kendrick', 'energetic', 'new', 'no instruments', 'popular is bad', 'rap', 'group'): ['Run the Jewels'],
    ('kendrick', 'energetic', 'new', 'instruments', 'popular is fine', 'rap', 'solo'): ['Kendrick Lamar'],
    ('kendrick', 'energetic', 'new', 'instruments', 'popular is fine', 'rap', 'group'): ['EarthGang'],
    ('kendrick', 'energetic', 'new', 'instruments', 'popular is bad', 'rap', 'solo'): ['Denzel Curry'],
    ('kendrick', 'energetic', 'new', 'instruments', 'popular is bad', 'rap', 'group'): ['Flatbush Zombies'],
    ('kendrick', 'energetic', 'old', 'no instruments', 'popular is fine', 'rap', 'solo'): ['Kanye West'],
    ('kendrick', 'energetic', 'old', 'no instruments', 'popular is fine', 'rap', 'group'): ['N.W.A.'],
    ('kendrick', 'energetic', 'old', 'no instruments', 'popular is bad', 'rap', 'solo'): ['DMX'],
    ('kendrick', 'energetic', 'old', 'no instruments', 'popular is bad', 'rap', 'group'): ['Wu-Tang Clan'],
    ('kendrick', 'energetic', 'old', 'instruments', 'popular is fine', 'rap', 'solo'): ['Tupac'],
    ('kendrick', 'energetic', 'old', 'instruments', 'popular is fine', 'rap', 'group'): ['Outkast'],
    ('kendrick', 'energetic', 'old', 'instruments', 'popular is bad', 'rap', 'solo'): ['Big L'],
    ('kendrick', 'energetic', 'old', 'instruments', 'popular is bad', 'rap', 'group'): ['Public Enemy'],
}

rock_artist_mappings = {
    # Chill, New
    ('chill', 'new', 'no instruments', 'popular is fine', 'solo'): ['Hozier'],
    ('chill', 'new', 'no instruments', 'popular is fine', 'group'): ['The 1975'],
    ('chill', 'new', 'no instruments', 'popular is bad', 'solo'): ['Ben Howard'],
    ('chill', 'new', 'no instruments', 'popular is bad', 'group'): ['Phoebe Bridgers'],
    ('chill', 'new', 'instruments', 'popular is fine', 'solo'): ['Maggie Rogers'],
    ('chill', 'new', 'instruments', 'popular is fine', 'group'): ['Vampire Weekend'],
    ('chill', 'new', 'instruments', 'popular is bad', 'solo'): ['Sufjan Stevens'],
    ('chill', 'new', 'instruments', 'popular is bad', 'group'): ['Big Thief'],
    
    # Chill, Old
    ('chill', 'old', 'no instruments', 'popular is fine', 'solo'): ['Tracy Chapman'],
    ('chill', 'old', 'no instruments', 'popular is fine', 'group'): ['Simon & Garfunkel'],
    ('chill', 'old', 'no instruments', 'popular is bad', 'solo'): ['Nick Drake'],
    ('chill', 'old', 'no instruments', 'popular is bad', 'group'): ['The Velvet Underground'],
    ('chill', 'old', 'instruments', 'popular is fine', 'solo'): ['James Taylor'],
    ('chill', 'old', 'instruments', 'popular is fine', 'group'): ['Fleetwood Mac'],
    ('chill', 'old', 'instruments', 'popular is bad', 'solo'): ['Cat Stevens'],
    ('chill', 'old', 'instruments', 'popular is bad', 'group'): ['The Zombies'],

    # Energetic, New
    ('energetic', 'new', 'no instruments', 'popular is fine', 'solo'): ['Yungblud'],
    ('energetic', 'new', 'no instruments', 'popular is fine', 'group'): ['Imagine Dragons'],
    ('energetic', 'new', 'no instruments', 'popular is bad', 'solo'): ['Grandson'],
    ('energetic', 'new', 'no instruments', 'popular is bad', 'group'): ['Palaye Royale'],
    ('energetic', 'new', 'instruments', 'popular is fine', 'solo'): ['Sam Fender'],
    ('energetic', 'new', 'instruments', 'popular is fine', 'group'): ['Måneskin'],
    ('energetic', 'new', 'instruments', 'popular is bad', 'solo'): ['King Princess'],
    ('energetic', 'new', 'instruments', 'popular is bad', 'group'): ['Royal Blood'],
    
    # Energetic, Old
    ('energetic', 'old', 'no instruments', 'popular is fine', 'solo'): ['David Bowie'],
    ('energetic', 'old', 'no instruments', 'popular is fine', 'group'): ['Queen'],
    ('energetic', 'old', 'no instruments', 'popular is bad', 'solo'): ['Lou Reed'],
    ('energetic', 'old', 'no instruments', 'popular is bad', 'group'): ['Television'],
    ('energetic', 'old', 'instruments', 'popular is fine', 'solo'): ['Bruce Springsteen'],
    ('energetic', 'old', 'instruments', 'popular is fine', 'group'): ['The Rolling Stones'],
    ('energetic', 'old', 'instruments', 'popular is bad', 'solo'): ['Iggy Pop'],
    ('energetic', 'old', 'instruments', 'popular is bad', 'group'): ['The Stooges']
}

pop_artist_mappings = {
    # Chill, New
    ('chill', 'new', 'no instruments', 'popular is fine', 'solo'): ['Billie Eilish'],
    ('chill', 'new', 'no instruments', 'popular is fine', 'group'): ['LANY'],
    ('chill', 'new', 'no instruments', 'popular is bad', 'solo'): ['Clairo'],
    ('chill', 'new', 'no instruments', 'popular is bad', 'group'): ['The Japanese House'],
    ('chill', 'new', 'instruments', 'popular is fine', 'solo'): ['Harry Styles'],
    ('chill', 'new', 'instruments', 'popular is fine', 'group'): ['The Lumineers'],
    ('chill', 'new', 'instruments', 'popular is bad', 'solo'): ['Rex Orange County'],
    ('chill', 'new', 'instruments', 'popular is bad', 'group'): ['Oh Wonder'],

    # Chill, Old
    ('chill', 'old', 'no instruments', 'popular is fine', 'solo'): ['Sade'],
    ('chill', 'old', 'no instruments', 'popular is fine', 'group'): ['Air Supply'],
    ('chill', 'old', 'no instruments', 'popular is bad', 'solo'): ['Enya'],
    ('chill', 'old', 'no instruments', 'popular is bad', 'group'): ['Everything But The Girl'],
    ('chill', 'old', 'instruments', 'popular is fine', 'solo'): ['Norah Jones'],
    ('chill', 'old', 'instruments', 'popular is fine', 'group'): ['ABBA'],
    ('chill', 'old', 'instruments', 'popular is bad', 'solo'): ['Tracy Chapman'],
    ('chill', 'old', 'instruments', 'popular is bad', 'group'): ['The Carpenters'],

    # Energetic, New
    ('energetic', 'new', 'no instruments', 'popular is fine', 'solo'): ['Dua Lipa'],
    ('energetic', 'new', 'no instruments', 'popular is fine', 'group'): ['Blackpink'],
    ('energetic', 'new', 'no instruments', 'popular is bad', 'solo'): ['Charli XCX'],
    ('energetic', 'new', 'no instruments', 'popular is bad', 'group'): ['CHVRCHES'],
    ('energetic', 'new', 'instruments', 'popular is fine', 'solo'): ['Olivia Rodrigo'],
    ('energetic', 'new', 'instruments', 'popular is fine', 'group'): ['AJR'],
    ('energetic', 'new', 'instruments', 'popular is bad', 'solo'): ['Mitski'],
    ('energetic', 'new', 'instruments', 'popular is bad', 'group'): ['Foster The People'],

    # Energetic, Old
    ('energetic', 'old', 'no instruments', 'popular is fine', 'solo'): ['Madonna'],
    ('energetic', 'old', 'no instruments', 'popular is fine', 'group'): ['Depeche Mode'],
    ('energetic', 'old', 'no instruments', 'popular is bad', 'solo'): ['Kate Bush'],
    ('energetic', 'old', 'no instruments', 'popular is bad', 'group'): ['Eurythmics'],
    ('energetic', 'old', 'instruments', 'popular is fine', 'solo'): ['Michael Jackson'],
    ('energetic', 'old', 'instruments', 'popular is fine', 'group'): ['The Bangles'],
    ('energetic', 'old', 'instruments', 'popular is bad', 'solo'): ['Cyndi Lauper'],
    ('energetic', 'old', 'instruments', 'popular is bad', 'group'): ['The B-52s']
}

varied_artist_mappings = {
    # Chill, New
    ('chill', 'new', 'no instruments', 'popular is fine', 'solo'): ['Khalid'],
    ('chill', 'new', 'no instruments', 'popular is fine', 'group'): ['Lofi Fruits Music'],
    ('chill', 'new', 'no instruments', 'popular is bad', 'solo'): ['Cuco'],
    ('chill', 'new', 'no instruments', 'popular is bad', 'group'): ['Mild High Club'],
    ('chill', 'new', 'instruments', 'popular is fine', 'solo'): ['Kacey Musgraves'],  # Country
    ('chill', 'new', 'instruments', 'popular is fine', 'group'): ['Mumford & Sons'],  # Folk/Country
    ('chill', 'new', 'instruments', 'popular is bad', 'solo'): ['Leon Bridges'],  # Soul
    ('chill', 'new', 'instruments', 'popular is bad', 'group'): ['First Aid Kit'],  # Indie Folk

    # Chill, Old
    ('chill', 'old', 'no instruments', 'popular is fine', 'solo'): ['Frank Sinatra'],  # Jazz/Pop
    ('chill', 'old', 'no instruments', 'popular is fine', 'group'): ['The Andrews Sisters'],  # Jazz Harmony
    ('chill', 'old', 'no instruments', 'popular is bad', 'solo'): ['Billie Holiday'],  # Jazz/Blues
    ('chill', 'old', 'no instruments', 'popular is bad', 'group'): ['The Modern Jazz Quartet'],  # Jazz
    ('chill', 'old', 'instruments', 'popular is fine', 'solo'): ['Claude Debussy'],  # Classical
    ('chill', 'old', 'instruments', 'popular is fine', 'group'): ['The Vienna Philharmonic'],  # Classical Orchestra
    ('chill', 'old', 'instruments', 'popular is bad', 'solo'): ['Erik Satie'],  # Minimalist Classical
    ('chill', 'old', 'instruments', 'popular is bad', 'group'): ['The Academy of Ancient Music'],  # Baroque Ensemble

    # Energetic, New
    ('energetic', 'new', 'no instruments', 'popular is fine', 'solo'): ['Bad Bunny'],  # Reggaeton
    ('energetic', 'new', 'no instruments', 'popular is fine', 'group'): ['Major Lazer'],  # EDM/Reggaeton
    ('energetic', 'new', 'no instruments', 'popular is bad', 'solo'): ['Rauw Alejandro'],  # Reggaeton/Latin
    ('energetic', 'new', 'no instruments', 'popular is bad', 'group'): ['ODESZA'],  # Indie EDM
    ('energetic', 'new', 'instruments', 'popular is fine', 'solo'): ['Chris Stapleton'],  # Country
    ('energetic', 'new', 'instruments', 'popular is fine', 'group'): ['Zac Brown Band'],  # Country
    ('energetic', 'new', 'instruments', 'popular is bad', 'solo'): ['Tyler Childers'],  # Americana/Country
    ('energetic', 'new', 'instruments', 'popular is bad', 'group'): ['The Marcus King Band'],  # Blues-Rock

    # Energetic, Old
    ('energetic', 'old', 'no instruments', 'popular is fine', 'solo'): ['Elvis Presley'],  # Rock'n'Roll
    ('energetic', 'old', 'no instruments', 'popular is fine', 'group'): ['The Supremes'],  # Motown
    ('energetic', 'old', 'no instruments', 'popular is bad', 'solo'): ['Pérez Prado'],  # Latin Mambo
    ('energetic', 'old', 'no instruments', 'popular is bad', 'group'): ['Fania All-Stars'],  # Salsa
    ('energetic', 'old', 'instruments', 'popular is fine', 'solo'): ['Beethoven'],  # Classical
    ('energetic', 'old', 'instruments', 'popular is fine', 'group'): ['The Berlin Philharmonic'],  # Classical Orchestra
    ('energetic', 'old', 'instruments', 'popular is bad', 'solo'): ['Niccolò Paganini'],  # Virtuoso Classical
    ('energetic', 'old', 'instruments', 'popular is bad', 'group'): ['The Kronos Quartet']  # Avant-Garde Strings
}
