# ROYONCHERENTS: A fun combat game where you play against a Bot, where you get to select a unique character
# Video Demo:  <URL HERE>
## Description:
In this game you get to select one of 5 interesting characters, paired agaisnt a bot. Each character has it's own health, defense, attack-potency and a special move.

# EXPLAINING FUNCTIONS:
## **Main**:
The main function would first prompt the user if they want to play the game or exit it.
It would then carry out various actions such as welcoming the user, printing all the neccessary stuff
in a way I formatted it to, such that it gives a game-ish vibe but in a console. This function is key to the code since it's the one decieding sequence of how functions would be executed!

## get_character:
The function first prompts the user if they want to stay in the character selection menu or if they want to go back to main menu. It asks the user to select a valid character, by showing them a list and once the character is retrieved,
<ins> it passes it into Main.</ins>

## bot_getter:
Randomly Selects bot's characters from the list of characters available, minus the character selected by the user.
<ins>Returns it to Main</ins>

## **arena_select:**
Selects the arena for where the battle would be fought
<ins>Returns it to Main</ins>

## boost_select:
Selects a boost for character based on the Arena Selected
For example; *Fice* would get a +15 stat to it's attack in *Bipolar Weather*, however, other characters get a HP buff of 25 and +5 to their attacks.

## players_init:
~~ The most complicated function that I've ever written..~~
What this function does is assigns variables to different characteristics of characters for i.e *"player_name = player["name"]* for easier accessing later down the code
It also initializes some variables like n, j, k which are used to count certain things in the code for i.e j counts if the user's attack would be further boosted upon dodging an attack, similarly "n" is used to count turns. It then passes on some variables into attack function if that's what the user selects or into dodge function respectively. If user get's their ultimat then it passes those functions into the user_special function. It continues looping through the fight until one of their healths Hit Zero after which, the game ends!
So technically its doing more than just initializing characters
### To summarize the function calling:
It calls, attack function, dodge function based and the ultimate function, retrieves back values and calculates healths based on the values returned.

## attack:
Calculates the damage for both the user and the bot, if bot selects dodge then it calls the dodge function.
*Returns back health to players_init function*

## dodge:
Reduces the damage taken, subsquently calls damange inc function, *returns health back to attack function or players_init*

## dmg_inc_calc:
Increases the damage of the user who dodged, max raised 3 times, *returns back to dodge which further passes it into the relevant function*

## user_special:
Calls for user's special attack. Calculates users, and bot's health after user's special attack and *returns it back to player's init function*

## close_game:
Exits the code

# This was my first project ever, and I coded this back in 2024!
