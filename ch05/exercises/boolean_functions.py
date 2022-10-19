def percentage_to_letter(score = 0):
  for i in [score]:
    if score >= 90: 
      return ("A")
    elif score < 90 and score >= 80:
      return ("B")
    elif score < 80 and score >=70:
      return ("C")
    elif score < 70 and score >= 60:
      return ("D")
    elif score < 60:
      return ("F")

def is_passing(percentage_to_letter):
  if percentage_to_letter == ("A") or ("B") or ("C"):
    return True
  else:
    return False
      
score = float(input("What is your score"))
print(percentage_to_letter())

  