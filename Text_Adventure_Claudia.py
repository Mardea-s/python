start = '''
You are coming home from an extended day at your Girls Who Code club at Accenture. It is well into the evening and the sun is beginning to set.
You reach the subway and have a choice betweent the F and E train.
The F line is traveling locally at a painfully slow pace, but will take you straight home.
The E line is traveling express but is unreliable and may skip your stop. Which will you take?
'''

F_Line = '''
You see a man sitting on a bench in casual attire.
He eyes you up and down before you take a seat next to him.
You both shift awkwardly. He attempts light conversation.
'''
E_Line = '''
Right before the doors close, a man in casual attire hops on, assesses the car
crowd, and locks eyes with you before taking a seat beside you.
'''

F_Stranger = '''
The ride is long. He complains about the local service, asking if you are frustrated
as well. Entertain or ignore his conversation? Type entertain or ignore
'''

E_Transfer= '''
You hear an announcement. The E train may skip your stop, but you can transfer
to the F line. Do you transfer or stay seated?
'''
F_ignorecommon='''
He smiles at your ignoring him. He doesn't ask anymore questions.
'''

F_name= '''
He asks your name. Do you respond?
'''
F_namecont= '''
He keeps talking. You are uncomfortable.
'''
E_Transferwyou='''
He transfers as well and takes a seat next to you once again
'''

E_stay='''
Both of you remain seated as the transfering crowd disperses.
'''

E_shutdown= '''
The E line is unreliable. After two stops it is shut down, leaving you to transfer back to the F anyway.
'''




print(start)
done = False
while not done:
    user_input = input("Type 'F' to take the F train or 'E' to take the E: ")
    if user_input == "F":
        print(F_Line)
        print(F_Stranger)
        done = True

        choice1F= False
        while not choice1F:
            user_input= input("Type 'entertain' to entertain or 'ignore' to ignore'")
            if user_input== "entertain":
                print(F_name)
                choice1F= True

                choice2F= False
                while not choice2F:
                        user_input= input("Type 'yes' or 'no'")
                        if user_input== 'yes':
                            print(F_namecont)
                            choice2F= True
                        elif user_input== 'no':
                            print(F_ignorecommon)
                            choice2F= True
            elif user_input=="ignore":
                print (F_ignorecommon)
                choice1F= True
            else:
                print("Type 'entertain' or 'ignore'")
    elif user_input == "E":
        print(E_Line)
        print(E_Transfer)
        done = True

        choice1E= False
        while not choice1E:
            user_input=input("Type'transfer' to transfer and 'stay' to remain seated")
            if user_input== "transfer":
                print (E_Transferwyou)
                choice1E=True
            elif user_input== "Stay":
                print(E_shutdown)
                choice1E=True
            else:
                print("type 'transfer' or 'stay'")
    else:
        print("Please type 'F' or 'E'");

laststop= '''
At the last stop, everyone exits. You could take the main roads a ways from home
or the backroads which are closer yet secluded. Which?
'''
main= '''
In the crowds you lose him for a moment, only to see him gaining on you. Do you run?
'''

run='''
He sees you and begins running too. You make it into a corner store and ask the employee for help.
You call 911 and help arrives, though he is long gone.
The officers take a report and you get home safely.
'''

dontrun='''
You try to act normal, and he keeps his distance.
Eventually you have to turn into your quiet neighborhood.
'''
backroads= '''
You turn left off the main road and towards home.
The man from the train takes the same route as you. You turn to see him the only other person on the road behind you.
You begin to pick up your pace. So does he. Eventually you are in an all out sprint and come to a intersection.
Do you turn left or right?
'''

Left= '''
You turn left, further into your neighborhood.
You don't want to lead him home, but you are getting tired.
He closes in, brandishing his knife.
'''

right= '''
You turn right and back onto the main road.
'''

print(laststop)
ending=False
while not ending:
    user_input = input("Type 'mainroads' or 'backroads'")
    if user_input == "mainroads":
        print(main)
        ending= True

        dourun= False
        while not dourun:
            user_input = input("Type 'Run' or 'don't run'")
            if user_input== "Run":
                print(run)
                dourun=True
            elif user_input== "don't run":
                print(dontrun)
                print(backroads)
                dourun= True
            else:
                print("Type 'Run' or 'don't run'")

    elif user_input == "backroads":
        print(backroads)
        ending= True

        leftorright= False
        while not leftorright:
            user_input = input("Type 'left' or 'right'")
            if user_input== "left":
                print(Left)
                print ("U dead.")
                leftorright= True
            elif user_input == "right":
                print(right)
                print(run)
                leftorright= True
    else:
        print("Type 'mainroads' or 'backroads'")
