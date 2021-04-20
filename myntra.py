class myntra:
    def __init__(self):
        print("Welcome to myntra")

    class Mens:
        def __init__(self):
            print("welcome to mens section")

        class footware:
            def __init__(self):
                print("welcome to mens footware")

            def woodland(self):
                print("Thanks for searching woodland")

            def crocs(self):
                print("thanks for searching crocs")

        class clothing:
            def __init__(self):
                print("welcome to clothing")

            def Gstar(self):
                print("thanks fot searching Gstar")


    class womens:
        def __init__(self):
            print("welcome to women section")

        class footware:
            def __init__(self):
                print("welcome to  women footware")

            def woodland(self):
                print("Thanks for searching woodland")

            def crocs(self):
                print("thanks for searching crocs")

        class clothing:
            def __init__(self):
                print("welcome to clothing")

            def Gstar(self):
                print("thanks fot searching Gstar")


shoping = myntra()
men = shoping.Mens()
foot = men.footware()
foot.woodland()


women = shoping.womens()
foot1 = women.footware()
foot1.woodland()