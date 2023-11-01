import random

class Character:
    def __init__(self, name, health, attack, level=1, experience=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.level = level
        self.experience = experience

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)

    def __str__(self):
        return f"{self.name} (Level {self.level}, Health: {self.health}, Attack: {self.attack})"

class Enemy(Character):
    def __init__(self, name, health, attack, experience_reward):
        super().__init__(name, health, attack)
        self.experience_reward = experience_reward

class Hero(Character):
    def __init__(self, name, health=100, attack=10):
        super().__init__(name, health, attack)
        self.inventory = {'Health Potion': 3, 'Sword': 1}
        self.gold = 50

def main():
    print("Welcome to the Text-Based RPG Game!")

    hero_name = input("Enter your hero's name: ")
    hero = Hero(hero_name)

    enemies = [
        Enemy("Goblin", 20, 5, 10),
        Enemy("Dragon", 50, 10, 30),
        Enemy("Witch", 30, 8, 20),
    ]

    waves = 0

    while hero.is_alive():
        waves += 1
        print(f"Wave {waves} - A new set of enemies approaches!")

        for enemy in enemies:
            if not hero.is_alive():
                print("Game over!")
                break

            print(f"A wild {enemy.name} appears!")
            while hero.is_alive() and enemy.is_alive():
                action = input("What will you do? (1. Attack, 2. Run, 3. Use Health Potion, 4. Visit Shop): ")
                if action == "1":
                    hero.attack_enemy(enemy)
                    if enemy.is_alive():
                        enemy.attack_enemy(hero)
                elif action == "2":
                    print(f"You run away from the {enemy.name}!")
                    break
                elif action == "3":
                    if hero.inventory['Health Potion'] > 0:
                        hero.inventory['Health Potion'] -= 1
                        hero.health += 20  # Use a health potion
                        print(f"{hero.name} uses a health potion. Health restored to {hero.health}.")
                    else:
                        print("You're out of health potions!")
                elif action == "4":
                    print("Welcome to the Shop!")
                    print(f"Gold: {hero.gold}")
                    print("1. Buy Health Potion (20 gold)")
                    print("2. Buy Sword (40 gold)")
                    print("3. Leave Shop")
                    shop_choice = input("Enter your choice: ")
                    if shop_choice == "1":
                        if hero.gold >= 20:
                            hero.gold -= 20
                            hero.inventory['Health Potion'] += 1
                            print("You've bought a Health Potion.")
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "2":
                        if hero.gold >= 40 and 'Sword' not in hero.inventory:
                            hero.gold -= 40
                            hero.inventory['Sword'] = 1
                            hero.attack += 10
                            print("You've bought a Sword. Your attack has increased.")
                        else:
                            print("You don't have enough gold or you already have a Sword!")
                    elif shop_choice == "3":
                        print("You leave the shop.")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid choice. Try again.")

            if hero.is_alive():
                hero.experience += enemy.experience_reward
                print(f"You defeated the {enemy.name}! You gained {enemy.experience_reward} experience points.")

            if hero.experience >= hero.level * 100:
                hero.level_up()
                print(f"Congratulations! You've leveled up to Level {hero.level}!")

        if not hero.is_alive():
            print(f"You were defeated by the {enemy.name}. Game over!")
            break
        else:
            print(f"Wave {waves} complete! You have {hero.health} health remaining.")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
