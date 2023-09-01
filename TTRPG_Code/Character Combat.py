import random

class Character:
    def __init__(self, name, hp, attack_bonus, damage_dice, ac):
        self.name = name
        self.hp = hp
        self.attack_bonus = attack_bonus
        self.damage_dice = damage_dice
        self.ac = ac
    
    def attack(self, target):
        attack_roll = random.randint(1, 20) + self.attack_bonus
        if attack_roll >= target.ac:
            damage = random.randint(1, self.damage_dice)
            target.hp -= damage

class Enemy:
    def __init__(self, name, hp, attack_bonus, damage_dice, ac):
        self.name = name
        self.hp = hp
        self.attack_bonus = attack_bonus
        self.damage_dice = damage_dice
        self.ac = ac
    
    def attack(self, target):
        attack_roll = random.randint(1, 20) + self.attack_bonus
        if attack_roll >= target.ac:
            damage = random.randint(1, self.damage_dice)
            target.hp -= damage

def simulate_combat(character, enemy):
    while character.hp > 0 and enemy.hp > 0:
        character.attack(enemy)
        if enemy.hp <= 0:
            print(f"{character.name} defeated {enemy.name}!")
            break
        enemy.attack(character)
        if character.hp <= 0:
            print(f"{enemy.name} defeated {character.name}!")
            break

# Create characters and enemies
player = Character("Player", hp=20, attack_bonus=5, damage_dice=8)
goblin = Enemy("Goblin", hp=10, ac=15)

# Simulate combat
simulate_combat(player, goblin)