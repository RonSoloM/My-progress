albums = [
    ("welcom to my Nightmare ", "Alive Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company",1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready For Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),

     ]
     ),
    ("Nightflight","budgie",1981,
     [
         (1, "Pulling the rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waktz"),
     ]
     ),
]

for name, atrist, year, songs in albums:
    print("Album: {}, Atrists: {},Year: {},Songs: {}".format(name, atrist, year, songs))
