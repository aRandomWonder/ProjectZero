from math import round 
# Physical damage - calculated using vit, strength, defense, 
# Magical damage - calculated using magic, 1/2 strength, 1/2 defense, 
# Slow - calculated using agility
# Run - calculated using agility

# Damage equation - and other mathy stuff
# Crit chance, 0.01 + p.agil/10
# Dodge chance, only possible if agility is greater than enemy's
# 

# Physical damage
# Defense
# Effect proce

# EFFECT TRANSLATOR
"""
effects = [ # Damage Types
            "physical_damage", "magical_damage",
            # Attr (True) Types
            "hp", "agil", "defe+", "defe-", "ag"
          ]


# Mathematical part of it
def effect_translator(effect: list, stats1, stats2 = None):
    # Stats1 is the initiater/attacker
    # Stats2 is the defender
    es = []
    for e in effect:
        if e[0] == "physical_damage":
            es.append(("hp", 
                       -round((stats1["str"] - stats2["defe"] + e[1]) 
                             * (stats2["vit"]/1000+1))))
            # Mathematical troubles *sigh*
        elif e[0] == "magical_damage":
            es.append(("hp",
                       -round(
                          (stats1["str"]/2 - stats2["defe"]/2 + e[1])
                           * stats1["magic"]
                          )))
        elif e[0] == "hp":
            es.append(("hp", round((e[1]) * (1+stats1["magic"]))))
        else:
            print("Effect still in dev. Effect is " + e[0])

    return es
"""

# add the rizz effect *rize