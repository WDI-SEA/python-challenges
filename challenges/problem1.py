# My favorite romance movies
# title, release year, runtime, tagline, main characters
romantic_movie1 = ("The Princess Bride", 1987, 98, "The story of a man and a woman who lived happily ever after.", ["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101, "He's having the day of his lifeâ€¦ over and over again.", ["Phil Connors"])
romantic_movie3 = ("AmÃ©lie", 2001, 122, "One person can change your life forever.", ["AmÃ©lie Poulain", "Nino Quincampoix", "The Garden Gnome"])

def romantics(movies):
    print('Here are my favorite romantic moves:')
    for movie in movies:
         print(f'{movie[0]} ({movie[1]}): {movie[3]}')
romantics([romantic_movie1, romantic_movie2, romantic_movie3])
