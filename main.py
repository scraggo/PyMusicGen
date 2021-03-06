from structs \
    import makescale, \
    intelligentplay, \
    review
import pickle
import sys

def __main():
    print("Welcome to Colin Burke's music program\n")
    print("Please donate to the ESU Computer Science Organization if you liked this program.\n")
    print("Main Menu")
    demo = 0
    inmenu = 1
    oursong = []
    while inmenu:
        menuoption = input(" [1]Start new random song\n [2]Load exising song from file\n [3]Demo mode\n [0]Quit\n" \
                           "Choice? ")
        if menuoption == 1:
            break
        elif menuoption == 2:
            filepath = "./songs/" + raw_input("./songs/")
            ourpickle = open(filepath, "rb")
            songparts = pickle.load(ourpickle)
            keyinfodict = songparts[0]
            oursong = songparts[1]
            review(keyinfodict, oursong)
            continue
        elif menuoption == 3:
            demo = 1
            israndom = 1
            break
        elif menuoption == 0:
            inmenu = 0
            quit()

    if demo:
        ourmeasures = 4
        ourkey = 'Eb'
        ouroption = 1
        beatspermeasure = 8
        ourscale = []
        ourseeds = []
        keyinfodict = {"ourmeasures": ourmeasures, "ourkey": ourkey, "ouroption": ouroption,
                       "beatspermeasure": beatspermeasure, "ourscale": ourscale, "ourseeds": ourseeds}
    else:
        ourkey = raw_input("\nWhat Key Root? Acceptable values: C,Db,D,Eb,E,F,F#,G,Ab,A,Bb,B \n")
        ouroption = input(
            "\nplease choose:\n--------------\n1. major scale\n2. natural minor scale\n3. harmonic minor scale\n" \
            "4. melodic minor scale\n5. dorian mode\n6. mixolydian mode\n7. ahava raba mode\n \
            8. minor pentatonic\n9. pentatonic scale\nyourchoice: ")
        beatspermeasure = input("\nhow many beats per measure?")
        ourmeasures = input("\nhow many measures?")
        ourscale = []
        ourseeds = []
        keyinfodict = {"ourmeasures": ourmeasures, "ourkey": ourkey, "ouroption": ouroption,
                       "beatspermeasure": beatspermeasure, "ourscale": ourscale, "ourseeds": ourseeds}
    # make our scale with our information
    keyinfodict["ourscale"] = makescale(ourkey, ouroption)
    intelligentplay(keyinfodict, oursong)


__main()
