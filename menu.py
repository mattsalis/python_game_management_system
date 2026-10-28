#----------------------------------------
# Create buttons for menu
#----------------------------------------

btn_Rent_Game = widgets.Button(description='Rent Game', button_style='info')
btn_search_vgame = widgets.Button(description='Video Game Search', style={'description_width': 'initial'}, button_style='info')
btn_search_bgame = widgets.Button(description='Board Game Search', style={'description_width': 'initial'}, button_style='info')
btn_Book_Sessions = widgets.Button(description='Book in-house group sessions', layout=widgets.Layout(width='auto'), button_style='info')
btn_Return_Game = widgets.Button(description='Return a game', button_style='info')
btn_Prune_Game = widgets.Button(description='Prune', button_style='info')
btn_Quit = widgets.Button(description='Quit', button_style='info')

#----------------------------------------
# Link buttons to event handler
#----------------------------------------

btn_Rent_Game.on_click(rent_game)
btn_Quit.on_click(quit)
btn_Return_Game.on_click(return_game)
btn_search_bgame.on_click(search_bgame)
btn_search_vgame.on_click(search_vgame)
btn_Book_Sessions.on_click(booking)
btn_Prune_Game.on_click(pruning)

#-------------------------------------------
# Display menu GUI
#-------------------------------------------

display(btn_Rent_Game, btn_Return_Game, btn_search_bgame, btn_search_vgame, btn_Book_Sessions,btn_Prune_Game, btn_Quit)
display(menu)
