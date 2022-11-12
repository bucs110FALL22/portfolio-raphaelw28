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
    length = len(self.string)
    my_list = ''
    for i in range(length):
      if ord(self.string[i]) in range(65, 91):
        if ord(self.s[i]) + length <= 90:
          my_list = my_list + chr(ord(self.string[i]) + length)
        else:
          my_list = my_list + chr(ord("A") + chr(ord(self.string[i]) + length - 90)
                                  
      elif ord(self.string[i]) in range(97, 123):
                                  
        if ord(self.string[i]) + length <= 122:
          my_list = my_list + chr(ord(self.string[i]) + length)
        else:
          my_list = my_list + chr(ord("A") + chr(ord(self.string[i]) + length - 90)

      else:
        my_list = my_list + self.string[i]
    return my_list


    


      
        

    
    
