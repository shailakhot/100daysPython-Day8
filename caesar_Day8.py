import caesar_logo
def caesar(msg, shift,enc_dcode):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    for letter in msg:
        if letter not in alphabet:
            result += letter
        elif enc_dcode == "encode":
           shifted_pos = alphabet.index(letter) + shift
        else:
            shifted_pos = alphabet.index(letter) - shift

        shifted_pos %= len(alphabet)
        result += alphabet[shifted_pos]

    return result


print(caesar_logo.logo)
do_continue = True
while do_continue:
  enc_dcode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
  msg = input("Type your message:\n")
  shift = int(input("Type your shift:\n"))
  result =""
  if enc_dcode == "encode" or enc_dcode == "decode":
     result = caesar(msg, shift,enc_dcode)
     print(f"Here's the {enc_dcode}d result: {result}")
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()

  if restart == "no":
     do_continue = False
     print("Thank you for playing! Good Bye")



