class Player:
    def __init__(self, name, level, prof, sub_prof, stats, hidden_stats, inventory, equips, status, affil):
        # Basic information
        self.name = name
        self.level = level
        self.prof = prof
        self.sub_prof = sub_prof

        # Stats
        self.vit = stats["vit"]
        self.hp = self.vit * 50
        self.str = stats["str"]
        self.defe = stats["defe"]
        self.agi = stats["agi"]
        self.mana = stats["mana"]
        self.magic = self.mana * 50
        self.afi = stats["afi"]

        # Hidden Stats
        self.fort = hidden_stats["fortitude"]
        self.luck = hidden_stats["luck"]
        self.dex = hidden_stats["dex"]

        # Inventory
        self.inventory = inventory
        self.equips = equips
        self.status = status
        self.affil = affil

        # Alternate Stats
        self.alt_stats = {}

    def print_status(self):
        return True
    
    def fill_stats(self):
        self.name = input("Enter your name:   ")
        for i in range(0, 15):
            choice = input(f"")
