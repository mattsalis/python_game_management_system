def rent_game():
  availability = True
  cus_rented = 0
  valid_input=False
  while valid_input == False:
    cusid = input('Enter Your Customer ID: ')
    gamid = input('Enter game ID: ')
    subscriptions = subMan.load_subscriptions()
    validation = subMan.check_subscription(cusid, subscriptions)
    if validation == True:
      valid_input = True
    else:
      print('Invalid input')
      valid_input = False
  rMatrix = []
  with open('Rental.txt'.format(path=filepath), 'r') as f:
      f.readline()
      for line in f:
          s = line.strip()
          rMatrix.append(list(s.split(",")))
  for i in range(len(rMatrix)):
      if rMatrix[i][2] == "" and rMatrix[i][0] == gamid:
          availability = False
  for i in range(len(rMatrix)):
    if rMatrix[i][3] == cusid and rMatrix[i][2] == "":
      cus_rented = cus_rented +1
  siMatrix = []
  with open('Subscription_Info.txt'.format(path=filepath), 'r') as f:
      f.readline()
      for line in f:
          s = line.strip()
          siMatrix.append(list(s.split(",")))
  sub_type = ""
  for i in range(len(siMatrix)):
    if siMatrix[i][0] == cusid:

      sub_type = siMatrix[i][1]

  if availability == True and (cus_rented+1) <= subMan.get_rental_limit(sub_type):
    current_date = input('Enter Current Date: ')


    with open('Rental.txt', 'a') as f:
      f.write(",".join([gamid, current_date, "", cusid]) + "\n")


    print('Rental Completed!\n')
    print(rMatrix)
  else:
    print('Invalid - Cannot complete rental\n')
    
