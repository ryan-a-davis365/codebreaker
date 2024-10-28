def main_logo():
    """
    Displays the main logo for the game
    """
    print(f"""                       /
                _,---~-LJ,-~-._
             ,-^  '   '   '    ^:,
            :   .    '      '     :
           :     /| .   /\   '     :
          :   . //|    // \   '     :
          :     `~` /| `^~`    '     ;
          :  '     //|         '    :
          :   \-_  `~`    ,    '    :
          ;  . \.\_,--,_;^/   ,    :
           :    ^-_!^!__/^   ,    :
            :,  ,  .        ,    :
              ^--_____     .   ;`
                      `^''----`
            """)

def header_image():
    """
    A banner that displays above the home screen
    """
    print(f"""
 ▄████▄   ▒█████  ▓█████▄ ▓█████  ▄▄▄▄    ██▀███  ▓█████ ▄▄▄       ██ ▄█▀▓█████  ██▀███  
▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓█████▄ ▓██ ▒ ██▒▓█   ▀▒████▄     ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▒██▒ ▄██▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██░█▀  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░▓█  ▀█▓░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░▒▓███▀▒░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░▒░▒   ░   ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░        ░ ░ ░ ▒   ░ ░  ░    ░    ░    ░   ░░   ░    ░    ░   ▒   ░ ░░ ░    ░     ░░   ░ 
░ ░          ░ ░     ░       ░  ░ ░         ░        ░  ░     ░  ░░  ░      ░  ░   ░     
░                  ░                   ░                                                 
    """)

def you_win():
    """
    An image that is displayed if the user wins
    """
    print(f"""   

▓██   ██▓ ▒█████   █    ██     █     █░ ██▓ ███▄    █ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▓██▒ ██ ▀█   █ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░██░▒██░   ▓██░
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░   ▒ ░░ ░░   ░ ▒░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░   ▒ ░   ░   ░ ░ 
 ░ ░         ░ ░     ░            ░     ░           ░ 
 ░ ░                                                  
    """)

def game_over():
    """
    An image that is displayed if the user loses
    """
    print(f"""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
    """)