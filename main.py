
# Flowchart
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


from treasure import treasure_art

print(treasure_art)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if left_or_right == 'left':
    wait_or_swim = input(
        'You\'ve come to a lake. there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if wait_or_swim == 'wait':
        red_yellow_or_blue = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One re, one yellow and one blue. Which colour do you choose?\n").lower()
        if red_yellow_or_blue == 'red':
            print("It's a room full of fire. Game Over.")
        elif red_yellow_or_blue == 'yellow':
            print("you found the treasure! You Win!")
        elif red_yellow_or_blue == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
