from game_data import data
import random
import art

#print(f'{choiceA['name']} a {choiceA['description']} with {choiceA['follower_count']} followers from {choiceA['country']}')



choices = {"a":"", "b":""}

#print(f'{B['name']} a {B['description']} with {B['follower_count']} followers from {B['country']}')

#print(choices["a"]['follower_count'])

def compare(a,b):
    if choices['a']['follower_count'] > choices['b']['follower_count']:
        return choices['a']['follower_count']
    else:
        return choices['b']['follower_count']

def high_or_low():
    print(art.logo)
    gameon = True
    user_score = 0
    for key in choices:
        choices[key] = random.choice(data)
    while gameon:
        print(f'Score:{user_score}')
        print(f'Compare A: {choices['a']['name']} a {choices['a']['description']} from {choices['a']['country']}')
        print(art.vs)
        print(f'Against B: {choices['b']['name']} a {choices['b']['description']} from {choices['b']['country']}')
        user_answer = input("Who has more followers. Type 'A' or 'B' ").lower()
        while user_answer != 'a' and user_answer != 'b':
            print("You have entered an invalid response")
            user_answer = input("Who has more followers. Type 'A' or 'B' ").lower()
        user_choice = choices[user_answer]
        if user_choice['follower_count'] == compare(choices['a'],choices['b']):
            print("Correct")
            print('\n'*20)
            user_score += 1
            choices['a'] = choices['b']
            choices['b'] = random.choice(data)

        else:
            gameon = False
            print("You lost")

high_or_low()