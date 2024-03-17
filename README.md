# competitive-eating-scoreboard
 

This Python script generates a scoreboard for a competitive eating competition based on the scores of the participants. Each participant earns points based on the quantity of each type of food they consume, and the scoreboard is sorted by score, with ties broken alphabetically by name.

Usage:
1. Ensure you have Python installed on your system. You can download it from https://www.python.org/downloads/.
2. Save the provided Python script (competitive_eating_scoreboard.py) to your local machine.
3. Prepare a list of participants in the competition. Each participant should be represented by a dictionary containing their name, the quantity of chicken wings, hamburgers, and hot dogs they consumed.
4. Run the script using a Python interpreter. You can do this by opening a terminal or command prompt, navigating to the directory where the script is saved, and typing `python3 competitive_eating_scoreboard.py`.
5. The script will output the scoreboard, showing the participants sorted by score, with ties broken alphabetically by name.

Example:
Suppose we have two participants:
- Habanero Hillary: 5 chicken wings, 17 hamburgers, 11 hot dogs
- Big Bob: 20 chicken wings, 4 hamburgers, 11 hot dogs

The generated scoreboard will look like this:
[{'name': 'Big Bob', 'score': 134}, {'name': 'Habanero Hillary', 'score': 98}]

Each participant's score is calculated by multiplying the quantity of each type of food by its corresponding point value (chicken wings: 5 points, hamburgers: 3 points, hot dogs: 2 points), and then summing these values.

For any inquiries or issues, please contact the script author.
