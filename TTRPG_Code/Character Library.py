import random

class Actor:
    def __init__(self, name, max_hp, current_hp, attack, damage, ac, perception):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attack = attack
        self.damage = damage
        self.ac = ac
        self.perception = perception

    def strike(self, target):
        attack_roll = random.randint(1, 20) + self.attack
        if attack_roll >= target.ac:
            if attack_roll >= target.ac*10 or attack_roll == 20:
                damage_taken = random.randint(1, self.damage)
                target.current_hp -= damage_taken*2
            else:
                damage_taken = random.randint(1, self.damage)
                target.current_hp -= damage_taken*2
    
    def heal(self, target):
        target.current_hp += random.randit(1, 8)
        if target.current_hp > target.max_hp:
            target.current_hp = target.max_hp