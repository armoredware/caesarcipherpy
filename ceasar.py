def caesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print "Your ciphertext is: ", cipherText
  return cipherText


x = 0
while x < 27:
    caesar("jxufqiimehtyisxysaud",x)
    x = x + 1
