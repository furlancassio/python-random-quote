def principal():
   import random
   print("Keep it logically awesome.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()

   last = 16
   rnd = random.randint(0, last)
   rnd2 = random.randint(0, last)
   print(quotes[rnd],end="")
   print(quotes[rnd2],end="")

if __name__== "__main__":
   principal()
