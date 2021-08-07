import random

def main():
    '''
    Generates funny names by combining first and last names from 2 separate lists.
    '''

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
            "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
            'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
            'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet',
            'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
            'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
            'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
            'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
            'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
            'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
            'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
            'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo',
            'Scratchensniff', 'Scut', "Sid 'The Squirts'",
            'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
            'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard',
            'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston ’Jazz Hands’",
            'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson',
            'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee',
            "M’Bernbo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',
            'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler',
            'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton',
            'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal',
            'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
            'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
            'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
            'Winterkorn', 'Woolysocks')

    while True:
        firstName = random.choice(first)
        lastName = random.choice(last)

        print("\n\n")
        print(f"{firstName} {lastName}")
        print("\n\n")

        instruction = input("Do you want repeat? (Enter for continue or 'n' for exit.)")

        if instruction.lower() == "n":
            break

if __name__ == "__main__":
    main()