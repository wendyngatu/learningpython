command=""
while True:
    command=input("> ").lower()
    if command ==("start"):
        print("car started...")
    elif command=="stop":
        print("car stopped...")
        
    elif command ==("help"):
            print("""
start-to start the car
stop-stop the car
quit-to quit
            """
            )
    elif command=="quit":
        break
    else:
        print("i don't understand this")
