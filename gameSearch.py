def search_game():
    valid_input=False
    game_found=False
    while valid_input == False:
        game_type=input('Do you want to search for a board game or video game? ')
        search_type=input('Search by title or genre? ')
        if (game_type == 'board game' or game_type == 'video game') and (search_type == 'title' or search_type == 'genre'):
            valid_input=True
        else:
            valid_input=False
            print('Invalid Input\n')
    if game_type == 'video game':
        vgMatrix = []
        with open('Video_Game_Info.txt'.format(path=filepath), 'r') as f:
            f.readline()
            for line in f:
                s = line.strip()
                vgMatrix.append(list(s.split(",")))

        if search_type == 'title':
            title=input('Enter game title: ')
            for i in range(len(vgMatrix)):
                if vgMatrix[i][1] == title:
                    print(vgMatrix[i])
                    game_found = True

        elif search_type == 'genre':
            genre=input('Enter game genre: ')
            for i in range(len(vgMatrix)):
                if vgMatrix[i][3] == genre:
                    print(vgMatrix[i])
                    game_found = True
        else:
            print('Invalid Entry\n')

    elif game_type == 'board game':
        bgMatrix = []
        with open('Board_Game_Info.txt', 'r') as f:
            f.readline()
            for line in f:
                s = line.strip()
                bgMatrix.append(list(s.split(",")))

        if search_type == 'title':
            title=input('Enter game title: ')
            for i in range(len(bgMatrix)):
                if bgMatrix[i][1] == title:
                    print(bgMatrix[i])
                    game_found = True

        elif search_type == 'genre':
            genre=input('Enter game genre: ')
            for i in range(len(bgMatrix)):
                if bgMatrix[i][3] == genre:
                    print(bgMatrix[i])
                    game_found = True
        else:
            print('Invalid Entry\n')

    if game_found == False:
            print('Could not find game.\n')
    else:
        print('\n')
