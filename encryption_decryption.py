# this is a  program to create a program on the basis of encryption called ''caesar caephar''

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""







print(f"Welcome\n {logo}")



text = "abcdefghijklmnopqrstuvwxyz"
TEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main(inp,shift,direc):
    encrypt_text = ""

    if direc == 'd':
        shift *= -1

    for char in inp:

            if char in text:  # this codition is for lowercase letters
                char_position = text.index(char)
                new_position = (char_position + shift) % 26
                new_letter = text[new_position]

                encrypt_text += new_letter
            elif char in TEXT:
                char_position = TEXT.index(char)
                new_position = (char_position+shift)%26
                new_letter = TEXT[new_position]
                encrypt_text += new_letter
            else:
                new_letter = char
                encrypt_text+=new_letter
    return encrypt_text

while True:
    direction = input("Enter 'e' for  encryption and 'd' for dercyption -- " )
    message = input("Enter your message here!\n")
    shift = int(input("Enter the shift number!\n"))

    print(main(inp=message,shift=shift%26,direc=direction))
    yes_no = input("Enter 'y' for yes if you want to continue and 'n' for no!!")
    if yes_no == 'n':
        break