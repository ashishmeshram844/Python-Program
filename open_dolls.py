def OpenRussianDoll(doll):
    if doll == 1:
        print("All dolls opens")
    else:
        OpenRussianDoll(doll-1)

OpenRussianDoll(10)