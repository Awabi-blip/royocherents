import random
import time
import sys
from random import randint
from tabulate import tabulate

Xeon = {
    "name": "Xeon",
    "health": 175,
    "attacks": ["Slice", "Thunder-Slash", "Razer-Kick", "Metal-Head"],
    "potency": [300,350],
    "special": "Terminal Atonement"
}

Rayquace = {
    "name": "Rayquace",
    "health": 225,
    "attacks": ["Stratos-Sunder", "Maxos-Surge", "Tail-Swirl", "Dragons Wrath"],
    "potency": [250,300],
    "special": "Celestial Ascension"
}

Zellyr = {
    "name": "Zellyr",
    "health": 275,
    "attacks": ["Boulder-Throw", "Tremoring-Earth", "Hurri-Coice", "Thousand-Arrows"],
    "potency": [200,250],
    "special": "METEORITE IMPACT"
}

Murkshaft = {
    "name": "Murkshaft",
    "health": 200,
    "attacks": ["Shadow Slither", "Red-Eye Pierce", "Nightfall Peck", "Daunting Hurls"],
    "potency": [25,35],
    "special": "Teleport"
}

Fice = {
    "name": "Fice",
    "health": 150,
    "attacks": ["Flash-Freeze", "Prominence-Burn", "Sub-Zero Fire", "Jet-Kindling", "Hell-Spider"],
    "potency": [300,300],
    "special": "Great Glacier Aieger"
}

display_characters = [
    ["Xeon", 175, ["Slice", "Thunder-Slash", "Razor-Kick", "Metal-Headbutt", "Fire-Blast"], "High",
     "Terminal Atonement"],
    ["Rayquace", 225, ["Stratos-Sunder", "Maxos-Surge", "Tail-Swirl", "Dragons Wrath"], "Medium",
     "Celestial Ascension"],
    ["Zellyr", 250, ["Boulder-Throw", "Trembling-Earth", "Cyclone-Burst", "Thousand-Arrows"], "Low",
     "METEORITE IMPACT"],
    ["Murkshaft", 200, ["Shadow Slither", "Red-Eye Pierce", "Nightfall Peck", "Daunting Hurls"], "Medium", "Teleport"],
    ["Fice", 150, ["Flash-Freeze", "Prominence-Burn", "Sub-Zero Fire", "Jet-Kindling", "Hell-Spider"], "Very High",
     "Great Glacier Aieger"]
]


characters = ["Xeon", "Rayquace", "Zellyr", "Murkshaft", "Fice"]
arena_adjectives = ["Enchanted", "Ominous", "Boundless", "Ethereal", "Celestial", "Majestic", "Volatile", "Tempestuous",
                    "Verdant", "Whispering"]
exaggerations = ['Brutal', 'Whopping', 'Crazy', 'Hefty', 'Overwhelming', 'Irrecoverable']
randexaggerations1 = random.choice(exaggerations)
randexaggerations2 = random.choice(exaggerations)
name = input("Enter your name to get started: ")


def main():
    time.sleep(0.5)
    print("="*135)
    print("="*52+"WELCOME TO ROYOCHERENTS"+"="*52)
    print("=" * 135)
    print("")
    action = input("Type C: to go to character selectin or E to exit the game: ").strip().upper()
    if action == "E":
        close_game()
    elif action == "C":
        character, player = get_character(display_characters)
        print("Loading....")
        time.sleep(1)
        print(f"Character Selected: {player['name'].title()}")
        arena = arena_select()
        boost = boost_select(arena)
        random_adjective_arena = random.choice(arena_adjectives)
        time.sleep(1.5)
        print("Selecting Arena.......")
        time.sleep(1)
        print(f"Arena selected: {arena.upper()}")
        time.sleep(1)
        time.sleep(1)
        bot = bot_getter(character)
        print(f"Getting the opponent's character...")
        time.sleep(1)
        print(f"Opponent's character: {bot['name']}")
        time.sleep(1)
        print(f"{name}'s {player['name']} is going to face off vs {bot['name']}!!!! GOODLUCK!\n")
        time.sleep(1)
        print(f"{boost}\n")
        print("=" * 135)
        players_init(player, bot)


def get_character(dc):
    time.sleep(0.5)
    print("")
    print("="*50+"CHARACTER SELECTION MENU!"+"="*50)
    print("")
    option = input("Type; C to select your character, M to go back to main menu: ").upper().strip()
    while option != "M" and option != "C":
        print("Nah uh")
        option = input("Type; C to select your character, M to go back to main menu: ").upper().strip()
    if option == "M":
        time.sleep(0.5)
        print("Returning to main menu.....")
        time.sleep(1.5)
        main()
    for c in dc:
        c[2] = ", ".join(c[2])
    headers = ["Name", "Health", "Attacks", "Attack-Potency", "Special Attack"]
    time.sleep(0.5)
    print("Loading character list...")
    time.sleep(1.75)
    print("                                                 CHOOSE YOUR CHARACTER:")
    print(tabulate(display_characters, headers, tablefmt="mixed_grid"))
    character = input("Make a choice: ").title().strip()
    while character not in characters:
        print("Tch-Tch, that's not a valid character")
        character = input("Enter Here: ").title()
    if character == "Fice":
        player = Fice
    elif character == "Murkshaft":
        player = Murkshaft
    elif character == "Rayquace":
        player = Rayquace
    elif character == "Zellyr":
        player = Zellyr
    else:
        player = Xeon
    return character, player


def bot_getter(character):
    characters_local = ["Xeon", "Rayquace", "Zellyr", "Murkshaft", "Fice"]
    for i in range(len(characters_local)):
        if characters_local[i] == character:
            break
    del characters_local[i]
    # print(characters_local)
    b = random.choice(characters_local)
    if b == "Fice":
        bot = Fice
    elif b == "Murkshaft":
        bot = Murkshaft
    elif b == "Rayquace":
        bot = Rayquace
    elif b == "Zellyr":
        bot = Zellyr
    else:
        bot = Xeon
    return bot


def arena_select():
    arenas = ['Stratosphere', 'Dark Abyss', 'Forest', 'Galactic Castle', 'Bipolar Weather']
    arena = random.choice(arenas)
    return arena


def boost_select(a):
    if a == "Bipolar Weather":
        # Fice["health"] += 0
        x = Fice["potency"]
        for i in range(len(x)):
            x[i] += 15
        boosted = f"Characters boosted: Fice, increased AP by 15"
        return boosted
    else:
        arena_dict = {'Stratosphere': Rayquace, 'Dark Abyss': Murkshaft, 'Forest': Zellyr,
                      'Galactic Castle': Xeon, }
        arena_dict[a]["health"] += 25
        x = arena_dict[a]["potency"]
        for i in range(len(x)):
            x[i] += 5
        boosted = f"Characters boosted: {arena_dict[a]['name']}, Increased HP by 25 and AP by 5"
        return boosted


def players_init(player, bot):
    ultimate_saved = False
    time.sleep(2)
    weathers = ['The rain continues to pour....', 'The sun is shining brightly.....', 'Thunderclaps everywhere.....']
    randweather = random.choice(weathers)

    player_name = player["name"]
    player_health = player["health"]
    player_attacks = player["attacks"]
    player_damage = player["potency"]
    player_special = player["special"]

    bot_name = bot["name"]
    bot_health = bot["health"]
    bot_attacks = bot["attacks"]
    bot_damage = bot["potency"]
    bot_special = bot["special"]
    n = 0
    dmg_inc = 0
    b_dmg_inc = 0
    j = 0
    k = 0
    while player_health > 0 and bot_health > 0:
        n += 1
        print(f"TURN {n}")
        if dmg_inc != 0:
            player_damage = player_damage[0] + dmg_inc, player_damage[1] + dmg_inc
            j+=1
            dmg_inc = 0
        else:
            pass
        if b_dmg_inc != 0:
            bot_damage = bot_damage[0] + b_dmg_inc, bot_damage[1] + b_dmg_inc
            b_dmg_inc = 0
            j += 1
        else:
            pass
        p_dmg = randint(player_damage[0], player_damage[1])
        b_atk = random.choice(bot_attacks)
        b_dmg = randint(bot_damage[0], bot_damage[1])
        print("")
        action = input("Do you want to Attack or Defend: ").lower().strip()
        while action not in ['attack', 'defend']:
            print("")
            action = input("Do you want to Attack or Defend: ").lower().strip()
        if action == "attack":
            special_chance = randint(1, 4)
            sp = randint(1, 4)
            if special_chance == sp:
                sp_flag = True
            else:
                sp_flag = False
            if sp_flag == True or ultimate_saved == True:
                ult = input("Your special move is ready! Type ULT to use it or SAVE to save it for later: ").upper()
                print("")
                if ult == "ULT":
                    time.sleep(1.5)
                    ultimate_saved = False
                    health = user_special(player_health, player_attacks, player_damage, player_special, bot_health,
                                          bot_attacks, bot_damage, bot_special, player_name, bot_name, p_dmg, b_atk,
                                          b_dmg)
                elif ult == "SAVE":
                    ultimate_saved = True
                    time.sleep(1.5)
                    print(f"Saving your ultiamte\nSelect a normal attack: ")
                    values = attack(player_health, player_attacks, player_damage, player_special, bot_health,bot_attacks,
                                    bot_damage, bot_special, player_name, bot_name, p_dmg, b_atk, b_dmg,k)
                    if len(values) == 3:
                        health = (values[0],values[1])
                        print(health)
                        b_dmg_inc = values[2]
                    elif len(values) == 2:
                        health = (values)
                        print(health)

            else:
                values = attack(player_health, player_attacks, player_damage, player_special, bot_health, bot_attacks,
                       bot_damage, bot_special, player_name, bot_name, p_dmg, b_atk, b_dmg, k)

                if len(values) == 3:
                    health = (values[0],values[1])
                    print(health)
                    b_dmg_inc = values[2]
                elif len(values) == 2:
                    health = (values)

        elif action == "defend":
            health = dodge(player_name, bot_name, b_atk, b_dmg, player_health, bot_health, player_damage)
            dmg_inc = dmg_inc_calc(player_name,player_damage,j)

        player_health = health[0]
        bot_health = health[1]
        var_percent_hp_player = round(player_health / player["health"] * 100)
        percentage_health_player = var_percent_hp_player if var_percent_hp_player > 0 else 0
        var_percent_hp_bot = round(bot_health / bot["health"] * 100)
        percentage_health_bot = var_percent_hp_bot if var_percent_hp_bot > 0 else 0

        if (player_health or bot_health) <= 0:
            if player_health < bot_health:
                winning = f"{name}'s {player_name} wins the battle with {abs(player_health - bot_health)} points!!"
            elif bot_health < player_health:
                winning = f"{bot_name} wins the battle with {abs(bot_health - player_health)} points!!"
            print(winning)
        time.sleep(1.5)
        print(f"Player health remaining = {percentage_health_player}%")
        time.sleep(1)
        print(f"Enemy health remaining = {percentage_health_bot}%")
        time.sleep(1)
        print("")
        print(randweather)
        print("=" * 135)


def attack(player_health, player_attacks, player_damage, player_special, bot_health, bot_attacks, bot_damage,
           bot_special, player_name, bot_name, p_dmg, b_atk, b_dmg,j):
    k = 0
    p_atk = input(f"Select an Attack: {', '.join(player_attacks)}: ").title().strip()
    print("")
    while p_atk not in player_attacks and k < 3:
        p_atk = input(f"Select an available Attack: {', '.join(player_attacks)}: ").title().strip()
        print("")
        k += 1
    if k == 3:
        sys.exit("You lost!")

    randints_bot_defend = randint(1,3)
    if randints_bot_defend == 4:
        health = dodge(bot_name, player_name, p_atk, p_dmg, bot_health, player_health, b_dmg)
        dmg_inc = dmg_inc_calc(bot_name, player_damage,j)
        okay = [health[1], health[0], dmg_inc]
        return okay

    else:
        randintsatk = randint(1, 2)
        if randintsatk == 1:
            player_health -= b_dmg
            bot_health -= p_dmg
            print(f"{player_name} moves first!")
            time.sleep(1)
            print(f"{player_name} uses {p_atk} on {bot_name} dealing a {randexaggerations1} damage of {p_dmg}")
            time.sleep(1)
            print(f"{bot_name} uses {b_atk} on {player_name} dealing a {randexaggerations2} damage of {b_dmg}")
            time.sleep(1)
        else:
            bot_health -= p_dmg
            player_health -= b_dmg
            if (player_health or bot_health) <= 0:
                return [player_health, bot_health]
            print(f"{bot_name} moves first!")
            time.sleep(1)
            print(f"{bot_name} uses {b_atk} on {player_name} dealing a {randexaggerations1} damage of {b_dmg}")
            time.sleep(1)
            print(f"{player_name} uses {p_atk} on {bot_name} dealing a {randexaggerations2} damage of {p_dmg}")
            time.sleep(1)

    health = [player_health, bot_health]
    return health


def dodge(dodger, attacker, atk, dmg, dodger_health, attacker_health, d_atk):
    time.sleep(2)
    dodge_statements = ['slides past over', 'blocks', 'tanks it through', 'weaves', 'jumps over']
    dodge = random.choice(dodge_statements)
    print(f"{dodger} {dodge} {attacker}'s {atk}")
    time.sleep(1)
    dodger_health -= round((dmg / 3.5), 1)
    if dodger_health <= 0:
        return [dodger_health,attacker_health]
    health = [dodger_health, attacker_health]
    return health

def dmg_inc_calc(name, damage,j):
    j += 1
    if j == 4:
        dmg_inc = 0
        print("Maximum attack reached!")
    else:
        if name == "Fice":
            print(f"{name}'s attack has been increased by 5%")
            temp_d = damage
            dmg_inc = round(((temp_d[0] + temp_d[1]) / 2) * (5 / 100))
        else:
            print(f"{name}'s attack has been increased by 10% ")
            temp_d = damage
            dmg_inc = round(((temp_d[0] + temp_d[1]) / 2) * (10 / 100))
    return dmg_inc


def user_special(player_health, player_attacks, player_damage, player_special, bot_health, bot_attacks, bot_damage,
                 bot_special, player_name, bot_name, p_dmg, b_atk, b_dmg):
    print(f"Here comes the ultimate attack!\n")

    if player_special == "Terminal Atonement":
        bot_health -= 90
        player_health -= 25
        print(f"Xeon uses TERMINAL ATONEMENT on {bot_name} DEALING 90 {randexaggerations2} damage\n")
        print(f"Xeon loses 25 health!")
        if (player_health or bot_health) <= 0:
            return [player_health, bot_health]

    elif player_special == "Celestial Ascension":
        bot_health -= 60
        b_dmg = b_dmg/1.25
        player_health -= 0
        print(f"Rayquace uses Celestial Ascension on {bot_name} DEALING 60 damage\n")
        if (player_health or bot_health) <= 0:
            return [player_health, bot_health]



    elif player_special == "METEORITE IMPACT":
        bot_health -= 60
        b_dmg = b_dmg/1.25
        player_health -= 0
        print(f"Zellyr uses METEORITE IMPACT on {bot_name} DEALING 60 damage\n")
        if (player_health or bot_health) <= 0:
            return [player_health, bot_health]

    elif player_special == "Teleport":
        print(f"Murkshaft dissappears into the shadows for 3 turns!!!")
        for i in range(3):
            bot_health -= 15
            player_health += 5
            time.sleep(1.5)
            print(f"{bot_name} gets hit by Murkshaft in a sneak attack losing 15 HP")
            time.sleep(1.5)
            print("Murkshaft heals itself by 5HP\n")
            if (player_health or bot_health) <= 0:
                return [player_health, bot_health]


    elif player_special == "Great Glacier Aieger":
        print(f"{bot_name} has been frozen for 5 turns!!!!\n")
        for i in range(5):
            bot_health -= 10
            player_health -= 0
            b_dmg = b_dmg/2
            time.sleep(1.5)
            print(f"The frost is too cold! {bot_name} loses 10HP\n")
            if (player_health or bot_health) <= 0:
                return [player_health, bot_health]

    player_health -= b_dmg
    print(f"{bot_name} uses {b_atk} on {player_name} dealing a {randexaggerations1} damage of {b_dmg}")

    health = (player_health, bot_health)
    return health


def close_game():
    sys.exit("Thanks for playing ROYOCHERENTS! 🚀 You’re leaving now? 🥺 Hope you saved your dignity—or didn’t. See ya, fellow Poyucher! ✌️🎮")



main()
