import random

input_list = ["rock", "scissors", "paper"]
status = True

print("=============Rock-Paper-Scissors start!!=============")

while status:
    user_choice = input('Please choice yours from rock, scissors and paper: ')

    if user_choice in input_list:
        computer_choice = random.choice(input_list)
        if user_choice == computer_choice:
            print(f'Computer choice {computer_choice}\nDraw!!')

        elif user_choice == "rock":
            status = False
            if computer_choice == "paper":
                print(f'Computer choice {computer_choice}\nYou lose!!')
            else:
                print(f'Computer choice {computer_choice}\nYou win!!')

        elif user_choice == "scissors":
            status = False
            if computer_choice == "rock":
                print(f'Computer choice {computer_choice}\nYou lose!!')
            else:
                print(f'Computer choice {computer_choice}\nYou win!!')

        elif user_choice == "paper":
            status = False
            if computer_choice == "scissors":
                print(f'Computer choice {computer_choice}\nYou lose!!')
            else:
                print(f'Computer choice {computer_choice}\nYou win!!')

    else:
        print("Your choice isn't correct!")