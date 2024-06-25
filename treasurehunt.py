print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go?")
print("Type 'LEFT' for left, or 'RIGHT' for right: ")

direction = input().upper()

while direction not in ["LEFT", "RIGHT"]:
    direction = input("Please type in 'LEFT' or 'RIGHT': ").upper()

print(f"You chose to go {direction}.")

if direction.upper() == "RIGHT":
    print("Sorry, you fell in a hole and died")
    
if direction.upper() == "LEFT":
    print("You come to a lake.")

    swimorboat = input("Do you swim or take a boat? Type 'SWIM' or 'BOAT'").upper()
    
    while swimorboat not in ["SWIM", "BOAT"]:
        swimorboat = input("Please type in 'SWIM' or 'BOAT': ").upper()
    
    print(f"You chose to {swimorboat}.")
    
    if swimorboat == "SWIM":
        print("Oh, no, a shark ate you!")
    
    if swimorboat == "BOAT":
        print("You arrive to an island with a castle with three doors.")
        print("Do you choose red, yellow, or green door")
        door = input("Type 'RED', 'YELLOW', or 'GREEN'.").upper()
        
        while door not in ["RED", "YELLOW", "GREEN"]:
            door = input("Please type 'RED', 'YELLOW', or 'GREEN'.")
            
            if door == "RED":
                print("A dragon eats you.")
                
            if door == "YELLOW":
                print("A dwarf kills you.")
            
            if door == "GREEN":
                print("You win. Congrats, you've found the treasure.")
