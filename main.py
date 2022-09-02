morse_code = {
    "A": "._",
    "B": "_...",
    "C": "_..",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__.."

}
on = True
print("Welcome to the morse code generator!!")
while on:
    print("Type a text and the program will return the morse code for you :)")
    user_entry = input("Text: ").upper()
    print("This is the value, if you typed a non letter, then it will return 'Invalid Value Entered'")
    for letter in user_entry:
        try:
            print(morse_code[letter], end=' ')
        except KeyError:
            print("Invalid Value Entered")
    wants_to_do_more = input("\nWant to convert more text?\nAnswer with 'Y' or 'N'\n").upper()
    if wants_to_do_more == "N":
        print("Exiting the program..")
        print("Good Bye!!!")
        on = False


