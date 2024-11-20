class Skill:
    def __init__(self, name, effect, rs, cooldown):
        self.name = name
        self.effect = effect
        self.level = 0
        self.points_required = None
        self.rs = rs
        self.cooldown = cooldown
        self.cdl = 0

    def __str__(self):
        return self.name

# Basic, tutorial skills
PUNCH = Skill("Punch", 
              [["phyisical_damage", 1]], 
              0, 0)
MAGIC_BULLET = Skill("Magic Bullet", 
                     [["magical_damage", 2], ["mana", -2]], 
                     1, 1)