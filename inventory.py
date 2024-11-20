class Item:
    def __init__(self, name, description, effect, ):
        self.name = name
        self.description = description
        self.effect = effect

    def __str__(self):
        return f"{self.name}\n{self.description}\nEffects: WIP"

# First time using inheritence. Boy am I nervous.
class Equipment(Item):
    def __init__(self, name, description, effect, location):
        super().__init__(name, description, effect)
        self.location = location

    def __str__(self):
        return f"{self.location}: {self.name}\n{self.description}\n" \
                "Effects: WIP"

class Consumable(Item):
    def __init__(self, name, description, effect, u, p):
        super().__init__(name, description, effect)
        self.u = u
        self.p = p

    def use(self):
        print(f"{self.name} was used.")
        return self.effect

basic_health_potion = Item("Basic Health Potion", "A fine made mini elixir",
                   {"hp": 3})