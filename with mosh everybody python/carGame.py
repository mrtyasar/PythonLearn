command = "" # kullanıcından bilgi alacağımız için boş karakter dizisi koyduk
started = False
while True: # aksi belirtilmediği sürece döngü devam etsin
    command = input("> ").lower() # kullanıcıdan veri alacaz ve veriyi küçük harfe çevrilecek
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")
        quit()