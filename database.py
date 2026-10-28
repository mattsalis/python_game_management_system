#Interacting with rental database
      with open('Rental.txt'.format(path=filepath), 'r') as f1:
        f1.readline()
        for line in f1:
          s= line.strip()
          rMatrix.append(list(s.split(",")))
      for i in range(len(rMatrix)):

#Interacting with video game database
    with open('Video_Game_Info.txt'.format(path=filepath), 'r') as f:
        f.readline()
        for line in f:
            s = line.strip()
            vgMatrix.append(list(s.split(",")))
    for i in range(len(vgMatrix)):

#Interacting with board game database
    with open('Board_Game_Info.txt'.format(path=filepath), 'r') as f:
        f.readline()
        for line in f:
            s = line.strip()
            bgMatrix.append(list(s.split(",")))
    for i in range(len(bgMatrix)):


#Interacting with booking database
  with open('Booking.txt'.format(path=filepath), 'r') as f:
      f.readline()
      for line in f:
          s = line.strip()
          bMatrix.append(list(s.split(",")))
  for i in range(len(bMatrix)):


#Interacting with subscription database
  with open('Subscription_Info.txt'.format(path=filepath), 'r') as f:
      f.readline()
      for line in f:
          s = line.strip()
          siMatrix.append(list(s.split(",")))
  sub_type = ""
  for i in range(len(siMatrix)):





