from os import system  # Allows clearing the command line screen
from json import load, dump, JSONDecodeError
from colorama import init, deinit, Fore
from keyboard import is_pressed

# Just gonna store this because it takes up so much space
title = """
████████╗██╗  ██╗███████╗    ██╗  ██╗ ██████╗ ██╗   ██╗███████╗███████╗       ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ ███████╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝    ██║  ██║██╔═══██╗██║   ██║██╔════╝██╔════╝██╗    ██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗
   ██║   ███████║█████╗      ███████║██║   ██║██║   ██║███████╗█████╗  ╚═╝    ██████╔╝█████╗  ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝█████╗  ██║  ██║
   ██║   ██╔══██║██╔══╝      ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝  ██╗    ██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██║  ██║
   ██║   ██║  ██║███████╗    ██║  ██║╚██████╔╝╚██████╔╝███████║███████╗╚═╝    ██║  ██║███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║███████╗██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝       ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                                                                                                                                  
"""
version = """
██╗   ██╗ ██╗    ██████╗                                                                                                                                          
██║   ██║███║   ██╔═████╗                                                                                                                                         
██║   ██║╚██║   ██║██╔██║                                                                                                                                         
╚██╗ ██╔╝ ██║   ████╔╝██║                                                                                                                                         
 ╚████╔╝  ██║██╗╚██████╔╝                                                                                                                                         
  ╚═══╝   ╚═╝╚═╝ ╚═════╝
"""

############################# Supporting Functions

def build_json():
    decoded_json = {
        'Money': 0,
        
        'Smelting Oven': False,
        'Carpenter\'s Table': False,
        'Metal-Working Table': False,
        
        'Pickaxe': 'Wooden Pickaxe',
        'Axe': None,
        'Shovel': None,
        'Bucket': 0,
        
        'Stone': 0,
        'Gold': 0,
        'Diamond': 0,
        'Emerald': 0,
        
        'Coal': 0,
        'Metal': 0,
        'Wood': 0,
        'Bucket Filled with Clay': 0,
        'Bucket Filled with Sand': 0,
        
        'Wood Plank': 0,
        'Door': 0,
        'Brick': 0,
        'Glass': 0,
        'Rebar': 0,
        'Nail': 0
    }
    with open('inventory.json', 'w') as json_file:
        dump(decoded_json, json_file, indent=4)
    return

def choose_option(pre_text, post_text, options):

    # Updates the screen when the selector moves
    def update_screen(selected_option_index):
        system('cls')
        if pre_text is not None:
            print(f"{Fore.RED}{pre_text}")
        if post_text is not None:
            print(f"{Fore.GREEN}{post_text}")
        for index, option in enumerate(options):
            if index == selected_option_index:
                print(f"  {Fore.YELLOW}>{Fore.WHITE}{option}{Fore.YELLOW}<")
            else:
                print(f"  {Fore.WHITE}{option}")

    selected_option_index = 0
    update_screen(selected_option_index)
    
    # Loop that checks for input at all times
    while True:
        if is_pressed('up'):
            selected_option_index -= 1
            selected_option_index %= len(options)  # If the index number goes over the list length or under 0, just resets it to where it should be
            update_screen(selected_option_index)
            while is_pressed('up'):
                pass  # To avoid scrolling when held down, await for key to become unpressed
        elif is_pressed('down'):
            selected_option_index += 1
            selected_option_index %= len(options)  # If the index number goes over the list length or under 0, just resets it to where it should be
            update_screen(selected_option_index)
            while is_pressed('down'):
                pass  # To avoid scrolling when held down, await for key to become unpressed
        elif is_pressed('enter'):
            while is_pressed('enter'):
                pass  # To avoid scrolling when held down, await for key to become unpressed
            return options[selected_option_index]

############################# Game Functions

def title_menu():
    # Checks to see if we have a previously started game to change the displayed options
    with open('inventory.json', 'r') as json_file:
        try:
            json_data = load(json_file)
        except JSONDecodeError:
            json_data = None
    if json_data == None:
        options = ["Play", "Patch Notes", "Exit"]
    else:
        options = ["Resume", "Start New Game", "Patch Notes", "Exit"]
    
    # Title Screen
    choose_option(version, title, ["Press Enter to Start"])
    
    # Main menu loop
    while True:
        chosen_option = choose_option(None, "The House: Remastered(v1.0)", options)
        if chosen_option == 'Play':
            build_json()
            play()
        elif chosen_option == 'Resume':
            play()
        elif chosen_option == 'Start New Game':
            verification_choice = choose_option("Are you sure you want to delete your current saved data and start again? There is no going back from this option.", None, ["Yes, I am sure", "No, go back"])
            if verification_choice == 'Yes, I am sure':
                build_json()
                play()
            elif verification_choice == 'No, go back':
                continue
        elif chosen_option == 'Patch Notes':
            with open('patch_notes.txt', 'r') as patch_notes_file:   
                choose_option(None, ''.join(patch_notes_file.readlines()), ["Exit"])
            continue
        elif chosen_option == 'Exit':
            break

def play():
    pass

# Main Guard (Script starts here)
if __name__ == '__main__':
    init(autoreset=True)  # Initiate colorama so I can color text
    title_menu()
    system('cls')
    print(f"{Fore.RED}Thank you for playing. Goodbye.")
    deinit()  # I don't know what this does, but regardless, I call it just in case
