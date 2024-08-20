# This function is called when your game ends, it calls information from another file to display a demonic reaper face.
def grim():
    with open("grim.txt") as f:
        print(f.read())

def main_menu():
    #  Print the introduction and available player commands
    print("GrimsGate")
    print("-----------------------------------------------------------------------------------------------------")
    print("Welcome to your end! Your soul has been chosen as Death's next meal. "
          "If you want to survive you need")
    print("to collect eight unique items and make your way past Death..")
    print("Make one wrong move and you surely will be dealing with Death itself, Good luck...")
    print()
    print("Move Commands: North, South, West, East (Case Sensitive)")
    print("Add to Inventory: get 'Item Name' (Case Sensitive)")
    print("-----------------------------------------------------------------------------------------------------")



def main():
    main_menu()
    # Create a dictionary to house the rooms and items
    rooms = {
        'Hellscape': {'name': 'Hellscape', 'South': 'River of Forgotten Dreams', 'North': 'Lucy''s tomb',
                      'East': 'Throne of bones', 'West': 'The Endless Maze', 'item': 'nothing'},
        'Lucy''s tomb': {'name': 'Lucy''s tomb', 'North': 'Death''s Domain', 'East': 'Soulful Chasm',
                         'West': 'Fallen Point', 'item': 'a Strange Skull'},
        'Soulful Chasm': {'name': 'Soulful Chasm', 'West': 'Lucy''s tomb', 'South': 'Throne of bones',
                          'item': 'a Strange Horn'},
        'Throne of bones': {'name': 'Throne of bones', 'North': 'Soulful Chasm',
                            'South': 'Torture Yard', 'West': 'Hellscape',
                            'East': 'Death''s Domain', 'item': 'a Silky Black Cloak'},
        'Torture Yard': {'name': 'Torture Yard', 'West': 'River of Forgotten Dreams', 'North': 'Throne of bones',
                         'item': 'a Scythe'},
        'River of Forgotten Dreams': {'name': 'River of Forgotten Dreams', 'West': 'Hellish Church',
                                      'East': 'Torture Yard', 'South': 'Death''s Domain', 'North': 'Hellscape',
                                      'item': 'a Vial of a Strange Substance'},
        'Hellish Church': {'name': 'Hellish Church', 'East': 'River of Forgotten Dreams', 'North': 'The Endless Maze',
                           'item': 'a Vile of Holy Water'},
        'Fallen Point': {'name': 'Fallen Point', 'East': 'Lucy''s tomb', 'South': 'The Endless Maze',
                         'item': 'a Strange White Feather'},
        'The Endless Maze': {'name': 'The Endless Maze', 'East': 'Lucy''s Tomb', 'South': 'Hellish Church',
                             'West': 'Death''s Domain', 'item': 'a Severed Finger'},
        'Death''s Domain': {'name': 'Death''s Domain', 'item': 'Death..'}  # Villain
    }

    # Establish how players current location will be called
    current_location = rooms['Hellscape']

    # Establish the current commands available to the player
    commands = ['North', 'South', 'West', 'East', 'Item']

    # Create a blank list for the inventory
    inventory = []

    # Begin the game
    while True:
        print('You are in the {}.'.format(current_location['name'], ))  # Print the player's current location
        print('This room contains {}.'.format(current_location['item'], ))  # Print the item in the locations
        print('Your Inventory: {}'.format(inventory, ))  # Print the player's inventory

        command = input('\nWhat would you like to do?').strip()  # Get player command input
        if command in commands:
            if command in current_location:
                current_location = rooms[current_location[command]]

                if current_location == rooms['Death''s Domain']:
                    if len(inventory) == 8:
                        print('You are in Death''s Domain')
                        print(
                            "---------------------------------------------------------------------------------------"
                            "--------------")
                        print('You collected all of the items, and escaped your death!!?!')
                        print(
                            "---------------------------------------------------------------------------------------"
                            "--------------")
                        break
                    else:
                        grim()
                        print('You are in Death''s Domain')
                        print(
                            "---------------------------------------------------------------------------------------"
                            "--------------")
                        print('It looks like you have not found everything, you have succumbed to death!')
                        break


            else:
                # Prompt user to choose a valid direction
                print('You run headlong into a rocky wall..'
                      'Please try a different direction.')

        elif command.lower() in 'quit':  # quit command
            print('You embrace death and...')
            grim()
            break

        elif command.lower().split()[0] == 'get':
            item = command.lower().split()[1]
            if item in [x.lower() for x in current_location['item']]:
                inventory.append(current_location['item'])
                print('You collected {}.'.format(current_location['item']))
                current_location['item'] = 'nothing'
                print(
                    "---------------------------------------------------------------------------------------"
                    "--------------")
            else:
                print("There is no available item here.")
                print(
                    "---------------------------------------------------------------------------------------"
                    "--------------")
        else:
            # Print statement when invalid command is given
            print('Please give a valid command!')
    print()
main()