import random
def primary():
  print("Keep it logically awesome.")
  last =13
  ran= random.randint(0, last)
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[ran])

if __name__== "__main__":
  primary()
