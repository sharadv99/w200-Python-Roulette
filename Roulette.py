#!/usr/bin/env python
#Sharad Varadarajan - Project 1 - Casino Roulette

import random

class bet_type():
    
    def straight_up(self):
        """Users are guided here to make straight-up bets. This function will return the option the user bets on"""
        print("""
\n--STRAIGHT-UP BETS--
You have chosen to bet on a single number on the board. The numbers on the board are listed below. Please choose one of the 
options below by entering the corresponding digit\n
 1) 0    11) 10    21) 20    31) 30        
 2) 1    12) 11    22) 21    32) 31    
 3) 2    13) 12    23) 22    33) 32    
 4) 3    14) 13    24) 23    34) 33    
 5) 4    15) 14    25) 24    35) 34    
 6) 5    16) 15    26) 25    36) 35   
 7) 6    17) 16    27) 26    37) 36    
 8) 7    18) 17    28) 27    38) 00    
 9) 8    19) 18    29) 28             
10) 9    20) 19    30) 29\n""")    
        return self.catch_exceptions_and_return_numbers(38,straight_up_nums,"Straight Up")
            
    def corner(self):
        """Users are guided here to make all corner bets. This function will return the option the user bets on"""
        print("""
\n--CORNER BETS--
You have chosen to bet on four adjoining numbers on the board. The blocks are listed below. Please choose one of the 
options below by entering the corresponding digit\n
1) [1,2,4,5]     7) [10,11,13,14]     13) [19,20,22,23]     19) [28,29,31,32]
2) [2,3,5,6]     8) [11,12,14,15]     14) [20,21,23,24]     20) [29,30,32,33]
3) [4,5,7,8]     9) [13,14,16,17]     15) [22,23,25,26]     21) [31,32,34,35]
4) [5,6,8,9]    10) [14,15,17,18]     16) [23,24,26,27]     22) [32,33,35,36]
5) [7,8,10,11]  11) [16,17,19,20]     17) [25,26,28,29]
6) [8,9,11,12]  12) [17,18,20,21]     18) [26,27,29,30]\n""")
        return self.catch_exceptions_and_return_numbers(22,corner_nums,"Corner")
        
    def split(self):
        """Users are guided here to make split bets. This function will return the option the user bets on"""
        print("""
\n--SPLIT BETS--
You have chosen to bet on two adjoining numbers on the board. The pairs are listed below. Please choose one of the 
options below by entering the corresponding digit\n
  1) [1,2]    11) [7,8]    21) [13,14]    31) [19,20]    41) [25,26]    51) [31,32]     
  2) [1,4]    12) [7,10]   22) [13,16]    32) [19,22]    42) [25,28]    52) [31,34]
  3) [2,3]    13) [8,9]    23) [14,15]    33) [20,21]    43) [26,27]    53) [32,33]
  4) [2,5]    14) [8,11]   24) [14,17]    34) [20,23]    44) [26,29]    54) [32,35]
  5) [3,6]    15) [9,12]   25) [15,18]    35) [21,24]    45) [27,30]    55) [33,36]
  6) [4,5]    16) [10,11]  26) [16,17]    36) [22,23]    46) [28,29]    56) [34,35]
  7) [4,7]    17) [10,13]  27) [16,19]    37) [22,25]    47) [28,31]    57) [35,36]
  8) [5,6]    18) [11,12]  28) [17,18]    38) [23,24]    48) [29,30]
  9) [5,8]    19) [11,14]  29) [17,20]    39) [23,26]    49) [29,32]
 10) [6,9]    20) [12,15]  30) [18,21]    40) [24,27]    50) [30,33]\n""")
        return self.catch_exceptions_and_return_numbers(57,split_nums,"Split")
    
    def column(self):
        """Users are guided here to make column bets. This function will return the option the user bets on"""
        print("""
\n--COLUMN BETS--
You have chosen to bet that a number will be in the chosen vertical column of 12 numbers. The columns are listed below. 
Please choose one of the options below by entering the corresponding digit\n
1) [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]    
2) [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]     
3) [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]\n""")
        return self.catch_exceptions_and_return_numbers(3,column_nums,"Column")
    
    def street(self):
        """Users are guided here to make street bets. This function will return the option the user bets on"""
        print("""
\n--STREET BETS--
You have chosen to bet on three consecutive numbers in a horizontal line. The rows are listed below. 
Please choose one of the options below by entering the corresponding digit\n
1) [1,2,3]       7) [19,20,21] 
2) [4,5,6]       8) [22,23,24]
3) [7,8,9]       9) [25,26,27]
4) [10,11,12]   10) [28,29,30]
5) [13,14,15]   11) [31,32,33]
6) [16,17,18]   12) [34,35,36]\n""")
        return self.catch_exceptions_and_return_numbers(12,street_nums,"Street")
                
    def line(self):
        """Users are guided here to make line bets. This function will return the option the user bets on"""
        print("""
\n--LINE BETS--
You have chosen to bet on six consecutive numbers that form two horizontal lines. The lines are listed below. 
Please choose one of the options below by entering the corresponding digit\n
1) [1,2,3,4,5,6]          4) [19,20,21,22,23,24] 
2) [7,8,9,10,11,12]       5) [25,26,27,28,29,30]
3) [13,14,15,16,17,18]    6) [31,32,33,34,35,36]\n""")
        return self.catch_exceptions_and_return_numbers(6,line_nums,"Line")
                
    def color(self):
        """Users are guided here to make color bets. This function will return the option the user bets on"""
        print("""
\n--COLOR BETS--
You have chosen to make a bet on whether a red or black number is selected. The numbers are listed below. 
Please choose one of the options below by entering the corresponding digit\n
1) Red Numbers:{}
2) Black Numbers:{}\n""".format(color_nums[0], color_nums[1]))
        return self.catch_exceptions_and_return_numbers(2,color_nums,"Color")
                
    def even_odd(self):
        """Users are guided here to make even/odd bets. This function will return the option the user bets on"""
        print("""
\n--EVEN/ODD BETS--
You have chosen to make a bet on whether an even or odd number is selected. The numbers are listed below. 
Please choose one of the options below by entering the corresponding digit\n
1) Odd Numbers:{}
2) Even Numbers:{}\n""".format(oe_nums[0], oe_nums[1]))
        return self.catch_exceptions_and_return_numbers(2,oe_nums,"Even/Odd")
    
    def dozen(self):
        """Users are guided here to make dozen bets. This function will return the option the user bets on"""
        print("""
\n--DOZEN BETS--
You have chosen to bet that the number will be fall within a consectuive dozen values. The batches of 12 are listed 
below. Please choose one of the options below by entering the corresponding digit\n
1) [1,2,3,4,5,6,7,8,9,10,11,12]          
2) [13,14,15,16,17,18,19,20,21,22,23,24]       
3) [25,26,27,28,29,30,31,32,33,34,35,36]\n""")
        return self.catch_exceptions_and_return_numbers(3,dozen_nums,"Dozen")
    
    def high_low(self):
        """Users are guided here to make high/low bets. This function will return the option the user bets on"""
        print("""
\n--HIGH/LOW BETS--
You have chosen to bet that the number will be fall within 18 consectuive values. The batches of 18 are listed 
below. Please choose one of the options below by entering the corresponding digit\n
1) {}        
2) {}\n""".format(hl_nums[0],hl_nums[1]))
        return self.catch_exceptions_and_return_numbers(2,hl_nums,"High/Low")
            
class wheel():
    
    def spin(self):
        """Where users are directed to spin the wheel and reveal the winning number"""
        print("""\n
----------------WHEEL SPINNING------------
----------------STILL SPINNING------------
------------THE SUSPENSE IS REAL!----------\n""")
        
        self.wheel_number = random.choice(wheel_nums) 
        print("\nThe wheel has stopped spinning......The ball has landed on {}".format(self.wheel_number))
        while True:
            try:
                self.wheel_results = input("Are you ready to view your results? If so enter 'yes' to proceed: ")
                if self.wheel_results == "yes":
                    wheel.current_results(self)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("You can only enter yes")
    
    def current_results(self):
        """After spinning the wheel, users find themselves here. Their bets have been evaluated against the winning number
        to determine the winnings/losses. Many variables are reset to prepare for subsequent rounds"""
        print("\n")
        self.num_of_games += 1
        for i in self.numbers:
            if self.wheel_number in [str(j) for j in i]:
                self.bet_outcomes.append("won")
            else:
                self.bet_outcomes.append("lost")
        for i in range(0,len(self.bets)):
            if self.bet_outcomes[i] == "won":
                self.funds += self.winnings[i][0]
                print("{}) For your ${} wager for a {} bet on {}, you won!! You made a profit of ${}!".format(i+1, self.wagers[i],self.bets[i], self.numbers[i], self.winnings[i][0]-self.wagers[i]))
                self.net_profit += self.winnings[i][0] - self.wagers[i]
            else:
                self.net_profit -= self.wagers[i]
                print("{}) For your ${} wager for a {} bet on {}, you lost...".format(i+1, self.wagers[i],self.bets[i], self.numbers[i]))
        self.past_winnings[self.num_of_games] = self.net_profit
        self.past_bets[self.num_of_games] = self.bets
        self.numbers = []
        self.wagers = []
        self.bets = []
        self.bet_outcomes = []
        self.winnings = []
        if self.net_profit > sum(self.wagers):
            print("\nYou made ${} during this round!".format(self.net_profit))
            self.net_profit = 0
            self.funds_()
        elif self.net_profit < sum(self.wagers):
            print("\nYou lost ${} during this round!".format(abs(self.net_profit)))
            self.net_profit = 0
            self.funds_()
        else:
            print("\nYour neither made nor lost money this round")
            self.net_profit = 0
            self.funds_()
            
class player():
    
    def __init__(self, name = "my friend"):
        self.net_profit = 0
        self.funds = 2000
        self.name = name
        self.numbers = []
        self.wagers = []
        self.past_bets = {}
        self.past_winnings = {}
        self.bets = []
        self.bet_outcomes = []
        self.winnings = []
        self.num_of_games = 0
        self.betting_categories = {1:bet_type.straight_up,2:bet_type.corner,3:bet_type.split,4:bet_type.column,
                                   5:bet_type.street,6:bet_type.line,7:bet_type.color,8:bet_type.even_odd,
                                   9:bet_type.dozen,10:bet_type.high_low}
        self.betting_odds = {1:36, 2:9, 3:18, 4:3, 5:12, 6:6, 7:2, 8:2, 9:3, 10:2}
        
    def main_menu(self):
        """The main menu where users can choose from a variety of options. If a user enters an incorrect value it will be caught"""
        print("""
--MAIN MENU--\n{}, please choose one of the options below by entering the corresponding digit(1, 2, 3, or 4):\n
     1) Place a bet
     2) View funds
     3) View results from previous bets
     4) Quit\n""".format(self.name))
        while True:
            try:
                self.welcome_choice = int(input("Which option would you like to choose?: "))
                if self.welcome_choice == 1:
                    self.bet()
                    break
                elif self.welcome_choice == 2:
                    self.funds_()
                    break
                elif self.welcome_choice == 3:
                    self.results()
                    break
                elif self.welcome_choice == 4:
                    self.quit()
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter only the digit that corresponds to the option you want to proceed with")
        
    def bet(self):
        """The menu for all bets that a user can choose from. Communicates with many other functions from all classes
        Once a user has finished their bets, they initiate the spin method within the Wheel class """
        print("""
\n--AVAILABLE BETS--
Below are the possible bets that you can place. Enter the digit that corresponds to the bet you would like to 
place(1-10):\n
     1) Straight Up           6) Line
     2) Corner                7) Color
     3) Split                 8) Even/Odd
     4) Column                9) Dozen
     5) Street               10) High/Low""")   
        while True:
            try:
                self.choose_bet = int(input("\nPlease choose an option: "))
                if self.choose_bet in range(1,11):
                    self.winnings.append([self.payout(self.betting_odds[self.choose_bet])])
                    self.numbers.append(self.betting_categories[self.choose_bet](self))
                    print("\nYou have wagered ${} for a {} bet on {}\nIf successful you will make a profit of ${}!\nYou have ${} left to play with.".
                          format(self.wagers[-1],self.bets[-1], self.numbers[-1], self.winnings[-1][0]-self.wagers[-1], self.funds))
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter only the digit that corresponds to the option you want to proceed with")
        while True:
            if self.funds > 0:
                try:
                    bet_more = input("\nWould you like to make any more bets prior to the wheel being spun? [yes or no]: ")
                    if bet_more.lower() == "yes":
                        self.bet()
                        break
                    elif bet_more.lower() == "no":
                        print("\nYou have made {} bets for a total amount of ${} --> Time to spin the wheel!\n".format(len(self.wagers), sum(self.wagers)))
                        wheel.spin(self)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("You can only enter yes or no")
            else:
                print("\nYou have made {} bets for a total amount of ${} --> Time to spin the wheel!\n".format(len(self.wagers), sum(self.wagers)))
                print("You have no more my money to bet. Lets spin the wheel!")
                wheel.spin(self)
                break
    
    def payout(self,value):
        """Stores the amount the user wants to wager on a bet, and returns the possible winnings to the bet function"""
        while True:
            try:
                self.possible_win = int(input("Please enter the amount you would like to wager on this bet :"))
                if self.possible_win > 0 and self.possible_win <= self.funds:
                    self.wagers.append(self.possible_win)
                    self.funds -= self.possible_win
                    return self.possible_win * value
                elif self.possible_win <= 0:
                    raise Exception("You can only enter positive whole numbers")
                elif self.possible_win > self.funds:
                    raise Exception("That is bet exceeds your current funds")
                else:
                    raise ValueError
            except ValueError:
                print("You can not include non-numeric values")
            except Exception as e:
                print(str(e))
        
    def funds_(self):
        """User navigate here from the main-menu, and are sent here automatically after a round is completed. 
        This is where they view their funds and determine whether they want to keep playing or not"""
        if self.funds > 0:
            print("""
\n--MY FUNDS--
At this point, you have ${} to gamble with! Please choose one of the options below by entering the corresponding 
digit(1 or 2):\n
     1) Continue Playing
     2) Cash Out\n""".format(str(self.funds)))
            while True:
                try:
                    self.funds_choice = int(input("Which option would you like to choose?: "))
                    if self.funds_choice == 1:
                        self.main_menu()
                        break
                    elif self.funds_choice == 2:
                        self.quit()
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Please enter only the digit that corresponds to the option you want to proceed with")
        else:
            print("You currently have no more money to gamble with. Thank you for playing and we hope to see you again soon!")
 
    def catch_exceptions_and_return_numbers(self,num_of_options,values,bet_type):
        """This function communicates directly with each betting_type function, and catches any exceptions that occur"""
        while True:
            try:
              x = int(input("Enter the number corresponding to the bet you would like to place: "))
              if x in range(1,num_of_options+1) and values[x - 1] not in self.numbers:
                self.bets.append(bet_type)
                return (values[x - 1])
              elif x not in range(1,num_of_options+1):
                raise IndexError
              elif values[x - 1] in self.numbers:
                #raise TypeError
                print("You must really like {} bets on {}, because this isnt the first time you've made that bet this round!".format(bet_type,values[x-1]))
                self.bets.append(bet_type)
                return(values[x-1])
              else:
                raise ValueError
            except ValueError:
                print("\nYou may only enter a digit between 1 and {}\n".format(num_of_options))
            except IndexError:
                print("\nYou may only enter a digit between 1 and {}\n".format(num_of_options))
                
    def results(self):
        """Users navigate here from the main menu. This is where they view their net winnings/losses from each round they have played"""
        print("""
\n--PAST RESULTS--""")
        if len(self.past_bets) > 0:
            for i in range(1,len(self.past_bets)+1):
                if self.past_winnings[i] > 0:
                    print("Round number[{}]--> You made {} bets and made a profit of ${}".format(i,len(self.past_bets[i]),self.past_winnings[i]))
                elif self.past_winnings[i] < 0:
                    print("Round number[{}]--> You made {} bets and suffered a loss of ${}".format(i,len(self.past_bets[i]),abs(self.past_winnings[i])))
                else:
                    print("Round number[{}]--> You made {} bets and drew even".format(i,len(self.past_bets[i])))
        else:
            print("You have not played any rounds of roulette yet!")
        while True:
            try:
                self.results_choice = input("\nAre you ready to return to the main menu? If so, enter 'yes' to proceed: ")
                if self.results_choice == "yes":
                    self.main_menu()
                    break
                else:
                    raise ValueError
            except ValueError:
                print("You can only enter yes")
        
    def quit(self):
        print("Thank you for playing! I hope you had a great experience. You began with $2000 and are leaving with $" + str(self.funds))
    
#---------------------------Initializing Global Lists----------------------------------------
straight_up_nums = [[str(i)] for i in (range(37))]
straight_up_nums.append(["00"])

corner_nums = [[1,2,4,5], [2,3,5,6], [4,5,7,8], [5,6,8,9], [7,8,10,11], [8,9,11,12], [10,11,13,14], [11,12,14,15],
                  [13,14,16,17], [14,15,17,18], [16,17,19,20], [17,18,20,21], [19,20,22,23], [20,21,23,24], [22,23,25,26],
                  [23,24,26,27], [25,26,28,29], [26,27,29,30], [28,29,31,32], [29,30,32,33], [31,32,34,35], [32,33,35,36]]

split_nums = [[1,2], [1,4], [2,3], [2,5], [3,6], [4,5], [4,7], [5,6], [5,8], [6,9], [7,8], [7,10], [8,9], [8,11], [9,12],
                  [10,11], [10,13], [11,12], [11,14], [12,15], [13,14], [13,16], [14,15], [14,17], [15,18], [16,17],
                  [16,19], [17,18], [17,20], [18,21], [19,20], [19,22], [20,21], [20,23], [21,24], [22,23], [22,25],
                  [23,24], [23,26], [24,27], [25,26], [25,28], [26,27], [26,29], [27,30], [28,29], [28,31], [29,30],
                  [29,32], [30,33], [31,32], [31,34], [32,33], [32,35], [33,36], [34,35], [35,36]]

column_nums = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
              [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]

street_nums = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21], [22,23,24],
             [25,26,27], [28,29,30], [31,32,33], [34,35,36]]

line_nums = [list(range(1,7)), list(range(7,13)), list(range(13,19)), list(range(19,25)), list(range(25,31)), list(range(31,37))]
red_nums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_nums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
color_nums = [red_nums, black_nums]
even_nums = list(range(2,37,2))
odd_nums = list(range(1,36,2))
oe_nums = [odd_nums, even_nums]
dozen_nums = [list(range(1,13)), list(range(13,25)), list(range(25,37))]
hl_nums = [list(range(1,19)), list(range(19,37))]
wheel_nums = [str(i) for i in range(37)]
wheel_nums.insert(1,"00")
                
#---------------------------User Interface----------------------------------------
print("""
Welcome to the roulette table! Hope you are ready to
have some fun and make some money in the process!\n""")
enter_name = input("Please enter your name: ")
a = player(enter_name)
a.main_menu()
