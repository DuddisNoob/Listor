
#Function

def int_input(prompt):
  while True:
    text = input(prompt + ": ")
    try:
      result = int(text)
      return result
    except ValueError:
      pass

def totalsum(a):
  n = len(a)
  ta = 0
  i = 0
  while i<n:
    ta += a[i]
    i += 1
  return ta




n = int_input("Hur många spelare")
playerhealth: list = []
playermagic = []
playertype = []
i = 0
while i<n:
  playerhealth.append(0)
  playermagic.append(0)
  playertype.append("Ghost")
  i = i +1

playertype[0]= "archer"

i = 0
while i<n:
  playerhealth[i] += int_input("Hur mycket hp har spelare "+str(i+1))
  if playertype[i] == "archer":
    playerhealth[i] += 1
  i = i +1

  
print(playerhealth)

def totalsum(a):
  n = len(a)
  ta = 0
  i = 0
  while i<n:
    ta += a[i]
    i += 1
  return ta
print(totalsum(playerhealth))

print("Hello")


