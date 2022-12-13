class StringUtility():
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string
    
  def vowels(self):
    count = 0
    for i in self.string:
      vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
      if i in vowels:
        count += 1
    if count < 5:
      return f"{count}"
    else:
      return "many"
      
  def bothEnds(self): 
      length = len(self.string)
      if length > 0:
        return f"{self.string[0]}{self.string[1]}{self.string[length-2]}{self.string[length-1]}"
      else:
        return ""
        
  def fixStart(self):
    if len(self.string) <=1:
      return self.string
    first_letter = self.string[0]
    string = self.string
    for i in self.string:
      if i == first_letter:
        string = string.replace(i,"*")
    string = string.replace("*",first_letter,1)
    return string

  def asciiSum(self):
    string = self.string
    sum = 0
    for i in string:
      sum = sum + ord(i)
    return(sum)

  def cipher(self):
    new_cipher = ""
    shift = len(self.string)

    for char in self.string:
      if char.isalpha():
        if char.isupper():
          new_cipher += chr((ord(char) + shift - 65) % 26 + 65)
        else:
          new_cipher += chr((ord(char) + shift - 97) % 26 + 97)
      else:
        new_cipher += char

    return new_cipher
        
           
    

    


      
        

    
    
