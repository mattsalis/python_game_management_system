def pruning():
  validate1 = False
  while validate1 == False:
    game_type = input('Do you want to prune video games (v) or board games (b)\n')
    if game_type == 'v' or game_type == 'b':
      validate1=True
    else:
      validate1 = False
      print('Invalid input - "v" or "b"\n ')
  if game_type == 'v':
    vgMatrix = []
    with open('Video_Game_Info.txt'.format(path=filepath), 'r') as f:
        f.readline()
        for line in f:
            s = line.strip()
            vgMatrix.append(list(s.split(",")))
    for i in range(len(vgMatrix)):
      gamid = vgMatrix[i][0]
      gamname = vgMatrix[i][1]
      total=0
      rMatrix = []
      with open('Rental.txt'.format(path=filepath), 'r') as f1:
        f1.readline()
        for line in f1:
          s= line.strip()
          rMatrix.append(list(s.split(",")))
      for i in range(len(rMatrix)):
        if gamid == rMatrix[i][0]:
          total = total+1
      if total < 3:
        print('Game ID '+str(gamname)+ ' has only been rented '+str(total)+ ' times!')
    print('End of Pruning\n')
