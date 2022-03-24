# memory game
# intialization
list1 = [i for i in range (0, 20)]
list2 = ['a', 's', 'f', 'h', 'k','l', 'm', 'n', 'o', 'b', 's', 'h', 'k', 'a', 'f', 'l', 'm', 'o', 'n', 'b']
list3 = []
player1_score = 0
player2_score = 0
total_score = 0
print("Welcome: ", end = '')
for i in range(0, 20):
    print(list1[i], end = ' ')
while total_score != 10:
    # player1 choices
    # check a number is valid or not
    num1 = int(input("\nPlayer1 - Score " + str(player1_score) + "\nplayer1 enter 2 numbers:\n"))
    valid_num1 = num1 >= 0 and num1 <= 20 and num1 not in list3
    while not valid_num1:
        num1 = int(input("Enter correct number...\n"))
        valid_num1 = num1 >= 0 and num1 <= 20 and num1 not in list3
    num2 = int(input())
    valid_num2 = num2 >= 0 and num2 <= 20 and num2 not in list3
    while not valid_num2:
        num2 = int(input("Enter correct number...\n"))
        valid_num2 = num2 >= 0 and num2 <= 20 and num2 not in list3
        # printing list of stars

    if list2[num1] != list2[num2] :
        list1[num1] = list2[num1]
        list1[num2] = list2[num2]
        print("Welcome: ", end='')
        for i in range(0, 20):
            print(list1[i], end=' ')
            list1[num1] = num1
            list1[num2] = num2
    if list2[num1] == list2[num2]:
        list1[num1] = list2[num1]
        list1[num2] = list2[num2]
        print("\nWelcome: ", end='')
        for i in range(0, 20):
            print(list1[i], end=' ')
        # calculate player1 score
    if list2[num1] == list2[num2]:
        player1_score +=1
    if list2[num1] == list2[num2]:
        list3.append(num1)
        list3.append(num2)
        list1[num1] = '*'
        list1[num2] = '*'
        print("\nWelcome: ", end='')
        for i in range(0, 20):
            print(list1[i], end = ' ')
    total_score = player1_score + player2_score
    if total_score == 10:
        break
        #player2
        #check a number is valid or not
    num3 = int(input("\nPlayer2 - Score " + str(player2_score) + "\nplayer2 enter 2 numbers:\n"))
    valid_num3 = num3 >= 0 and num3 <= 20 and num3 not in list3
    while not valid_num3:
        num3 = int(input("Enter correct number...\n"))
        valid_num3 = num3 >= 0 and num3 <= 20 and num3 not in list3
    num4 = int(input())
    valid_num4 = num4 >= 0 and num4 <= 20 and num4 not in list3
    while not valid_num4:
        num4 = int(input("Enter correct number...\n"))
        valid_num4 = num4 >= 0 and num4 <= 20 and num4 not in list3
    # printing list of stars
    if  list2[num3] != list2[num4]  :
        list1[num3] = list2[num3]
        list1[num4] = list2[num4]
        print("\nWelcome: ", end='')
        for i in range(0, 20):
            print(list1[i], end=' ')
            list1[num1] = num1
            list1[num2] = num2
    if list2[num3] == list2[num4]:
        list3.append(num3)
        list3.append(num4)
        list1[num3] = list2[num3]
        list1[num4] = list2[num4]
        print("\nWelcome: ", end='')
    # calculate player 2 score
        for i in range(0, 20):
            print(list1[i], end=' ')
    if list2[num3] == list2[num4]:
        player2_score +=1
    if list2[num3] == list2[num4]:
        list1[num3] = '*'
        list1[num4] = '*'
        print("\nWelcome: ", end='')
        for i in range(0, 20):
            print(list1[i], end=' ')
    # show the the winner
    total_score = player1_score + player2_score
if player1_score > player2_score:
    print("\nplayer1 win.")
elif player2_score > player1_score:
    print("\nplayer2 win.")
else:
    print("\ngame is draw.")