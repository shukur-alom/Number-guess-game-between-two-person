import getpass
print(f"\n\t\t\t\t\t\t\t\t\t\tWELCOME TO THE GUESS GAME")
user_input1 = int(getpass.getpass(f"Enter 1st Number: "))
user_input2 = int(getpass.getpass(f"Enter 2nd Number: "))
fst_player_try = 0
sst_player_try = 0

while True:
   fst_player_input = int(input(f"\n1nd player\nGuess a number: "))   
   if user_input2 > fst_player_input:
      fst_player_try = fst_player_try + 1
      print(f"""\n1st player number greather than {fst_player_input}
      1st player try {fst_player_try}""")

   elif user_input2 < fst_player_input:
      fst_player_try = fst_player_try + 1
      print(f"""\n1st player number lesser than {fst_player_input}
      1st player try {fst_player_try}""")
   
   elif user_input2 == fst_player_input:
      fst_player_try = fst_player_try + 1
      print(f"""\n1st player successfully gase 2nd player number. it's {user_input2}
      1st player try {fst_player_try}\n\n""")
      break

while True:
   sst_player_input = int(input(f"\n2nd player\nGuess a number: "))   
   if user_input1 > sst_player_input:
      sst_player_try = sst_player_try + 1
      print(f"""\n2nd player number greather than {sst_player_input}
      2nd player try {sst_player_try}""")

   elif user_input1 < sst_player_input:
      sst_player_try = sst_player_try + 1
      print(f"""\n2nd player number lesser than {sst_player_input}
      2nd player try {sst_player_try}""")
   
   elif user_input1 == sst_player_input:
      sst_player_try = sst_player_try + 1
      print(f"""\n2nd player successfully gase 1st player number. it's {user_input1}
      2nd player try {sst_player_try}\n\n""")
      break

if fst_player_try < sst_player_try:
   print(f'''1st player try {fst_player_try} 2st player try {sst_player_try}
   \nWIN 1st PLAYER''')
elif fst_player_try > sst_player_try:
   print(f'''1st player try {fst_player_try} 2st player try {sst_player_try}
   \nWIN 2nd PLAYER''')
elif fst_player_try == sst_player_try:
   print(f'''1st player try {fst_player_try} 2st player try {sst_player_try}
   \nDROW THE MATCH''')
