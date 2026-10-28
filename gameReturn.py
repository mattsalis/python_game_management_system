def return_game():
  found = False
  date = input('Current date: ')
  gamid = input('Enter game ID: ')
  rating = int(input('Enter Star Rating (/10): '))
  comments = input('Enter any comments (optional): \n')
  feeMan.add_feedback(gamid, rating, comments, 'Game_Feedback.txt')
  print('Feedback added, Thank You!\n')
  rMatrix=[]
  with open('Rental.txt'.format(path=filepath), 'r') as f:
      f.readline()
      for line in f:
          s = line.strip()
          rMatrix.append(list(s.split(",")))
  for i in range(len(rMatrix)):
      if rMatrix[i][0] == gamid and rMatrix[i][2] == "":
          rMatrix[i][2] = date
          found = True
  if found == False:
    print('Error - Could not return\n')

  with open('Rental.txt', 'w') as f:
      f.write("GameID,Rental Date,Return Date,Rental Customer ID\n")
      for line in rMatrix:
        f.write(",".join(line)+"\n")
