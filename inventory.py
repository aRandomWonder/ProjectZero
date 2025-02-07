class Item:
    def __init__(self, name, description, effect, stack = False):
        self.name = name
        self.description = description
        self.effect = effect
        self.stack = stack

    def __str__(self):
        return f"{self.name}\n{self.description}\nEffects: WIP"

class Equipment(Item):
    def __init__(self, name, description, effect, location, stack = False):
        super().__init__(name, description, effect, stack)
        self.location = location

    def __str__(self):
        return f"{self.location}: {self.name}\n{self.description}\n" \
                "Effects: WIP"

class Consumable(Item):
    def __init__(self, name, description, effect, usages, requirement, stack):
        super().__init__(name, description, effect, stack)
        self.usages = usages
        self.requirement = requirement

    def use(self, ):
        print(f"{self.name} was used.")
        return self.effect
    




basic_health_potion = Item("Basic Health Potion", "A fine made mini elixir",
                   {"hp": 3})

