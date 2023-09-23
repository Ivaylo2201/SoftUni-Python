def isValid(password):
    rule1 = True
    rule2 = True
    rule3 = True
    valid_Chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5"
        , "6", "7", "8", "9", "0"]

    digitsList = ["1", "2", "3", "4", "5",
                  "6", "7", "8", "9", "0"]

    if len(password) < 6 or len(password) > 10:
        rule1 = False
        print("Password must be between 6 and 10 characters")

    for x in password.lower():
        if x not in valid_Chars:
            rule2 = False
            print("Password must consist only of letters and digits")
            break

    digits = 0
    for x in password:
        if x in digitsList:
            digits += 1

    if digits < 2:
        rule3 = False
        print("Password must have at least 2 digits")

    if rule1 is True and rule2 is True and rule3 is True:
        print("Password is valid")


passwordInput = input()
isValid(passwordInput)
