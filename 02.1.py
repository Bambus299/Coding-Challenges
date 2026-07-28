def world(w0, w1, w2, w3) :
    print(w0)
    print(w1)
    print(w2)
    print(w3)


c: str = "+"
t: str = "#"
w: str = "°"
e: str = "!"
# c = character ,t = tile ,w = way ,e = end


w0 =[t,c,t]
w1 =[t,w,t]
w2 =[t,w,e]
w3 =[t,t,t]

world(w0, w1, w2, w3)

# Erster Abteil

while c in w0:
    move1= input("wohin soll sich Santa bewegen? ")


    if move1== "r" and w0.index(c) == 2:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move1== "r" and w0.index(c) == 1:
        w0 =[t,t,c]
        w1 =[t,t,w]
        w2 =[t,t,e]

        world(w0, w1, w2, w3)

    if move1== "r" and w0.index(c) == 0:
        w0 =[t,c,t]
        w1 =[t,w,t]
        w2 =[t,w,e]

        world(w0, w1, w2, w3)

    if move1== "l" and w0.index(c) == 0:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move1== "l" and w0.index(c) == 1:
        w0 =[c,t,t]
        w1 =[w,t,t]
        w2 =[w,w,e]

        world(w0, w1, w2, w3)

    if move1== "l" and w0.index(c) == 2:
        w0 =[t,c,t]
        w1 =[t,w,t]
        w2 =[t,w,e]

        world(w0, w1, w2, w3)

    if move1== "u"and w0.index(c) == 2:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move1== "u"and w0.index(c) == 1:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move1== "u"and w0.index(c) == 0:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move1== "d"and w0.index(c) == 2:
        w0 =[t,t,t]
        w1 =[t,t,c]
        w2 =[t,t,e]

        world(w0, w1, w2, w3)
        break

    if move1== "d"and w0.index(c) == 1:
        w0 =[t,t,t]
        w1 =[t,c,t]
        w2 =[t,w,e]

        world(w0, w1, w2, w3)
        break

    if move1== "d"and w0.index(c) == 0:
        w0 =[t,t,t]
        w1 =[c,t,t]
        w2 =[w,w,e]

        world(w0, w1, w2, w3)
        break

# Zweiter Abteil

while c in w1:
    move2= input("wohin nun? ")


    if move2== "r" and w1.index(c) == 2:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move2== "r" and w1.index(c) == 1:
        w0 =[t,t,t]
        w1 =[t,t,c]
        w2 =[t,t,e]

        world(w0, w1, w2, w3)

    if move2== "r" and w1.index(c) == 0:
        w0 =[t,t,t]
        w1 =[t,c,t]
        w2 =[t,w,e]

        world(w0, w1, w2, w3)

    if move2== "l" and w1.index(c) == 0:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move2== "l" and w1.index(c) == 1:
        w0 =[t,t,t]
        w1 =[c,t,t]
        w2 =[w,w,e]

        world(w0, w1, w2, w3)

    if move2== "l" and w1.index(c) == 2:
        w0 =[t,t,t]
        w1 =[t,c,t]
        w2 =[t,w,e]

        world(w0, w1, w2, w3)

    if move2== "u"and w1.index(c) == 2:
        w0 =[t,t,c]
        w1 =[t,t,w]
        w2 =[t,t,e] 

        world(w0, w1, w2, w3)
        while c in w0:
            move1 = input("wohin nun?")
            if move1== "r" and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 1:
                w0 =[t,t,c]
                w1 =[t,t,w]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 0:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 1:
                w0 =[c,t,t]
                w1 =[w,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 2:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 1:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "d"and w0.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,t,c]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 0:
                w0 =[t,t,t]
                w1 =[c,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)
                break




    if move2 == "u" and w1.index(c) == 1:
        w0 = [t,c,t]
        w1 = [t,w,t]
        w2 = [t,w,e]

        world(w0,w1,w2,w3)
        while c in w0:
            move1 = input("wohin nun?")
            if move1== "r" and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 1:
                w0 =[t,t,c]
                w1 =[t,t,w]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 0:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 1:
                w0 =[c,t,t]
                w1 =[w,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 2:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 1:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "d"and w0.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,t,c]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 0:
                w0 =[t,t,t]
                w1 =[c,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)
                break

    

    if move2== "u"and w1.index(c) == 0:
        w0 =[c,t,t]
        w1 =[w,t,t]
        w2 =[w,w,e]

        world(w0, w1, w2, w3)
        while c in w0:
            move1 = input("wohin nun?")
            if move1== "r" and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 1:
                w0 =[t,t,c]
                w1 =[t,t,w]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 0:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 1:
                w0 =[c,t,t]
                w1 =[w,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 2:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 1:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "d"and w0.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,t,c]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 0:
                w0 =[t,t,t]
                w1 =[c,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)
                break

    if move2== "d"and w1.index(c) == 2:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[t,t,c]
        print("Du hast es geschafft!")
        world(w0, w1, w2, w3)
        break

    if move2== "d"and w1.index(c) == 1:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[t,c,e]

        world(w0, w1, w2, w3)
        break

    if move2== "d"and w1.index(c) == 0:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[c,w,e]

        world(w0, w1, w2, w3)
        break

# Dritter Abteil

while c in w2:
    move3= input("wohin nun? ")


    if move3== "r" and w2.index(c) == 2:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move3== "r" and w2.index(c) == 1:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[t,t,c]

        print("Du hast es geschafft!")

        world(w0, w1, w2, w3)
        break

    if move3== "r" and w2.index(c) == 0:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[t,c,e]

        world(w0, w1, w2, w3)

    if move3== "l" and w2.index(c) == 0:
        print("das ist nicht möglich")

        world(w0, w1, w2, w3)

    if move3== "l" and w2.index(c) == 1:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[c,w,e]

        world(w0, w1, w2, w3)

    if move3== "l" and w2.index(c) == 2:
       break

    if move3== "u"and w2.index(c) == 2:
        break


    if move3 == "u" and w2.index(c) == 1:
        w0 = [t,t,t]
        w1 = [t,c,t]
        w2 = [t,w,e]

        world(w0,w1,w2,w3)
        while c in w1:
            move2= input("wohin nun? ")


            if move2== "r" and w1.index(c) == 2:
                print("das ist nicht möglich")

            world(w0, w1, w2, w3)

            if move2== "r" and w1.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,t,c]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)

            if move2== "r" and w1.index(c) == 0:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move2== "l" and w1.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move2== "l" and w1.index(c) == 1:
                w0 =[t,t,t]
                w1 =[c,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)

            if move2== "l" and w1.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move2== "u"and w1.index(c) == 2:
                w0 =[t,t,c]
                w1 =[t,t,w]
                w2 =[t,t,e] 

                world(w0, w1, w2, w3)
                while c in w0:
                    move1 = input("wohin nun?")
                    if move1== "r" and w0.index(c) == 2:
                        print("das ist nicht möglich")

                        world(w0, w1, w2, w3)

                    if move1== "r" and w0.index(c) == 1:
                        w0 =[t,t,c]
                        w1 =[t,t,w]
                        w2 =[t,t,e]

                        world(w0, w1, w2, w3)

                    if move1== "r" and w0.index(c) == 0:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]

                        world(w0, w1, w2, w3)

                    if move1== "l" and w0.index(c) == 0:
                        print("das ist nicht möglich")

                        world(w0, w1, w2, w3)

                    if move1== "l" and w0.index(c) == 1:
                        w0 =[c,t,t]
                        w1 =[w,t,t]
                        w2 =[w,w,e]

                        world(w0, w1, w2, w3)

                    if move1== "l" and w0.index(c) == 2:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]

                        world(w0, w1, w2, w3)

                    if move1== "u"and w0.index(c) == 2:
                        print("das ist nicht möglich")

                        world(w0, w1, w2, w3)

                    if move1== "u"and w0.index(c) == 1:
                        print("das ist nicht möglich")

                        world(w0, w1, w2, w3)

                    if move1== "u"and w0.index(c) == 0:
                        print("das ist nicht möglich")

                        world(w0, w1, w2, w3)

                    if move1== "d"and w0.index(c) == 2:
                        w0 =[t,t,t]
                        w1 =[t,t,c]
                        w2 =[t,t,e]

                        world(w0, w1, w2, w3)
                        break

                    if move1== "d"and w0.index(c) == 1:
                        w0 =[t,t,t]
                        w1 =[t,c,t]
                        w2 =[t,w,e]

                        world(w0, w1, w2, w3)
                        break

                    if move1== "d"and w0.index(c) == 0:
                        w0 =[t,t,t]
                        w1 =[c,t,t]
                        w2 =[w,w,e]

                        world(w0, w1, w2, w3)
                        break




    if move2 == "u" and w1.index(c) == 1:
        w0 = [t,c,t]
        w1 = [t,w,t]
        w2 = [t,w,e]

        world(w0,w1,w2,w3)
        while c in w0:
            move1 = input("wohin nun?")
            if move1== "r" and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 1:
                w0 =[t,t,c]
                w1 =[t,t,w]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 0:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 1:
                w0 =[c,t,t]
                w1 =[w,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 2:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 1:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "d"and w0.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,t,c]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 0:
                w0 =[t,t,t]
                w1 =[c,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)
                break

    

    if move2== "u"and w1.index(c) == 0:
        w0 =[c,t,t]
        w1 =[w,t,t]
        w2 =[w,w,e]

        world(w0, w1, w2, w3)
        while c in w0:
            move1 = input("wohin nun?")
            if move1== "r" and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 1:
                w0 =[t,t,c]
                w1 =[t,t,w]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)

            if move1== "r" and w0.index(c) == 0:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 1:
                w0 =[c,t,t]
                w1 =[w,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)

            if move1== "l" and w0.index(c) == 2:
                w0 =[t,c,t]
                w1 =[t,w,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 2:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 1:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "u"and w0.index(c) == 0:
                print("das ist nicht möglich")

                world(w0, w1, w2, w3)

            if move1== "d"and w0.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,t,c]
                w2 =[t,t,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]

                world(w0, w1, w2, w3)
                break

            if move1== "d"and w0.index(c) == 0:
                w0 =[t,t,t]
                w1 =[c,t,t]
                w2 =[w,w,e]

                world(w0, w1, w2, w3)
                break

            if move2== "d"and w1.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,t,t]
                w2 =[t,t,c]
                print("Du hast es geschafft!")
                world(w0, w1, w2, w3)
                break

            if move2== "d"and w1.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,t,t]
                w2 =[t,c,e]

                world(w0, w1, w2, w3)
                break

            if move2== "d"and w1.index(c) == 0:
                w0 =[t,t,t]
                w1 =[t,t,t]
                w2 =[c,w,e]

                world(w0, w1, w2, w3)
                break


    

    if move3== "u"and w2.index(c) == 0:
        w0 =[t,t,t]
        w1 =[c,t,t]
        w2 =[w,w,e]

        world(w0,w1,w2,w3)
        while c in w1:
            move2= input("wohin nun? ")


            if move2== "r" and w1.index(c) == 2:
                print("das ist nicht möglich")
        
                world(w0, w1, w2, w3)
        
            if move2== "r" and w1.index(c) == 1:
                w0 =[t,t,t]
                w1 =[t,t,c]
                w2 =[t,t,e]
        
                world(w0, w1, w2, w3)
        
            if move2== "r" and w1.index(c) == 0:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]
        
                world(w0, w1, w2, w3)
        
            if move2== "l" and w1.index(c) == 0:
                print("das ist nicht möglich")
        
                world(w0, w1, w2, w3)
        
            if move2== "l" and w1.index(c) == 1:
                w0 =[t,t,t]
                w1 =[c,t,t]
                w2 =[w,w,e]
        
                world(w0, w1, w2, w3)
        
            if move2== "l" and w1.index(c) == 2:
                w0 =[t,t,t]
                w1 =[t,c,t]
                w2 =[t,w,e]
        
                world(w0, w1, w2, w3)
        
            if move2== "u"and w1.index(c) == 2:
                w0 =[t,t,c]
                w1 =[t,t,w]
                w2 =[t,t,e] 
        
                world(w0, w1, w2, w3)
                while c in w0:
                    move1 = input("wohin nun?")
                    if move1== "r" and w0.index(c) == 2:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "r" and w0.index(c) == 1:
                        w0 =[t,t,c]
                        w1 =[t,t,w]
                        w2 =[t,t,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "r" and w0.index(c) == 0:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 0:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 1:
                        w0 =[c,t,t]
                        w1 =[w,t,t]
                        w2 =[w,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 2:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 2:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 1:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 0:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "d"and w0.index(c) == 2:
                        w0 =[t,t,t]
                        w1 =[t,t,c]
                        w2 =[t,t,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move1== "d"and w0.index(c) == 1:
                        w0 =[t,t,t]
                        w1 =[t,c,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move1== "d"and w0.index(c) == 0:
                        w0 =[t,t,t]
                        w1 =[c,t,t]
                        w2 =[w,w,e]
        
                        world(w0, w1, w2, w3)
                        break
        
        
        
        
            if move2 == "u" and w1.index(c) == 1:
                w0 = [t,c,t]
                w1 = [t,w,t]
                w2 = [t,w,e]
        
                world(w0,w1,w2,w3)
                while c in w0:
                    move1 = input("wohin nun?")
                    if move1== "r" and w0.index(c) == 2:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "r" and w0.index(c) == 1:
                        w0 =[t,t,c]
                        w1 =[t,t,w]
                        w2 =[t,t,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "r" and w0.index(c) == 0:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 0:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 1:
                        w0 =[c,t,t]
                        w1 =[w,t,t]
                        w2 =[w,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 2:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 2:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 1:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 0:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "d"and w0.index(c) == 2:
                        w0 =[t,t,t]
                        w1 =[t,t,c]
                        w2 =[t,t,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move1== "d"and w0.index(c) == 1:
                        w0 =[t,t,t]
                        w1 =[t,c,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move1== "d"and w0.index(c) == 0:
                        w0 =[t,t,t]
                        w1 =[c,t,t]
                        w2 =[w,w,e]
        
                        world(w0, w1, w2, w3)
                        break
        
            
        
            if move2== "u"and w1.index(c) == 0:
                w0 =[c,t,t]
                w1 =[w,t,t]
                w2 =[w,w,e]
        
                world(w0, w1, w2, w3)
                while c in w0:
                    move1 = input("wohin nun?")
                    if move1== "r" and w0.index(c) == 2:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "r" and w0.index(c) == 1:
                        w0 =[t,t,c]
                        w1 =[t,t,w]
                        w2 =[t,t,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "r" and w0.index(c) == 0:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 0:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 1:
                        w0 =[c,t,t]
                        w1 =[w,t,t]
                        w2 =[w,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "l" and w0.index(c) == 2:
                        w0 =[t,c,t]
                        w1 =[t,w,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 2:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 1:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "u"and w0.index(c) == 0:
                        print("das ist nicht möglich")
        
                        world(w0, w1, w2, w3)
        
                    if move1== "d"and w0.index(c) == 2:
                        w0 =[t,t,t]
                        w1 =[t,t,c]
                        w2 =[t,t,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move1== "d"and w0.index(c) == 1:
                        w0 =[t,t,t]
                        w1 =[t,c,t]
                        w2 =[t,w,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move1== "d"and w0.index(c) == 0:
                        w0 =[t,t,t]
                        w1 =[c,t,t]
                        w2 =[w,w,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move2== "d"and w1.index(c) == 2:
                        w0 =[t,t,t]
                        w1 =[t,t,t]
                        w2 =[t,t,c]
                        print("Du hast es geschafft!")
                        world(w0, w1, w2, w3)
                        break
        
                    if move2== "d"and w1.index(c) == 1:
                        w0 =[t,t,t]
                        w1 =[t,t,t]
                        w2 =[t,c,e]
        
                        world(w0, w1, w2, w3)
                        break
        
                    if move2== "d"and w1.index(c) == 0:
                        w0 =[t,t,t]
                        w1 =[t,t,t]
                        w2 =[c,w,e]
        
                        world(w0, w1, w2, w3)
                        break
       

        

    if move3== "d"and w2.index(c) == 2:
        break

    if move3== "d"and w2.index(c) == 1:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[t,w,e]
        w3 =[t,c,t]

        world(w0, w1, w2, w3)
        break

    if move3== "d"and w2.index(c) == 0:
        w0 =[t,t,t]
        w1 =[t,t,t]
        w2 =[w,w,e]
        w3 =[c,t,t]

        world(w0, w1, w2, w3)
        break
            










