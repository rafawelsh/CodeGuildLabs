#13.ROT.cipher.py

English = ['a', 'b', 'c', 'd', 'e',	'f', 'g', 'h', 'i',	'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rotate(alpha, m):
    return alpha[m:] + alpha[:m]

m = int(input('Rotate: '))
ROTN = rotate(English, m)
translator = dict(zip(English, ROTN))
print(translator)

message = input('What is your message? ')
def encode(message):
    output = ""
    for i in message:
        #print(output)
        output += translator[i]
    return output
print(encode(message))


#notes from class
# for char in message:
#     index = alphabet.find(char)
#     encoded += rot13[index]
# return encoded


#Xavier's help.
# translator = dict(zip(English, ROTN))
# message = "abcdef"
# def encode(message):
#     output = ""
#     for i in message:
#         #print(output)
#         output += translator[i]
#     return output
# print(encode(message))
# print(list(translator.keys()))

# message = "Hello"
# def encode(message):
#     for char in English == char in ROTN
#     return message





#encrypting
# message = input("What is your message? ")
# key = 3
#
# # for symbol in message:
#     if symbol.isalpha():
#         num = ord(symbol)
#         num += key
#
#         if symbol.isupper():
#             if num >ord('Z'):
#                 num -= 26
#             elif num += 26
#         elif symbol.islower():
#             if num > ord('z'):
#                 num -= 26
#             elif num < ord('a')
#                 num +=26
#
#         transalated += chr(num)
#     else:
#         transalated += symbol
#     return transalated
