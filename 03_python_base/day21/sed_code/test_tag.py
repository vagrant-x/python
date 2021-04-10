

tag = True
while tag:
    print("level_1")
    choice = input("level_1 >>>")
    if choice == "quit": break
    if choice == "quit_all": tag = False
    while tag:
        print("level_2")
        choice = input("level_2 >>>")
        if choice == "quit": break
        if choice == "quit_all": tag = False
        while tag:
            print("level_3")
            choice = input("level_3 >>>")
            if choice == "quit": break
            if choice == "quit_all": tag = False