@@ -1,47 +1,48 @@
# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.

listA = [10,24,34,35,67,98,101]

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.

# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.

# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 





# 1. 
A linear search checks each item in a list one by one until it finds the target or goes through all items. 
A binary search only works on sorted lists. It checks the middle item, and then cuts the list in half 
and repeats.
"""
# 2.
In the list [10, 24, 34, 35, 67, 98, 101], we check each item:
1. Check 10
2. Check 24
3. Check 34
4. check 35 
5. Check 67
6. Check 98 (I got it)
It takes 6 steps to find 98 using linear search 


# 3. 
we start with the middle number, 93. Since 150 is bigger, we focus on the right half:
1. Middle is 145
2. Middle is 150 (found it)
It takes 3 steps to find 150 using binary search


# 4. 
An algorithm is a set of steps or rules to solve a problem or do something. 



# 5.
This is O(1), constant time, because no matter how many floors there are, 
the family knows exactly which floor to go to. The number of floors does not change the steps needed.
"""

# 6. 
big_o_phone_search = """
This is O(n), linear time, because you have to check each pair of pants one by one. 
The number of steps increases as the number of pants increases.
"""

# 7.
class GameConsole:
    def __init__(self, brand, model, year,):
        self.brand = brand
        self.model = model
        self.year = year
       

    def power_on(self):
        return f"{self.model} is on."

    def play_game(self, game):
        return f"Playing {game} on {self.model}."

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year}) with GB storage."


console1 = GameConsole("Sony", "PlayStation 5", 2020, 825)
console2 = GameConsole("Microsoft", "Xbox Series X", 2020, 1000)

# 8.
class VideoGame:
    def __init__(self, title, year, platform):
        self.title = title
        self.year = year
        self.platform = platform

    def start_game(self):
        return f"Starting {self.title}."

    def show_details(self):
        return f"{self.title} - ({self.year}), for {self.platform}."

    def pause_game(self):
        return f"{self.title} is paused."

game1 = VideoGame("2k26", "BLack Top", 2020, "PlayStation 5")
game2 = VideoGame("Fortnite", "Shooter", 2021, "Xbox Series X")
