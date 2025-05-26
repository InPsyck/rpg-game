import json
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

class Player:
    def __init__(self, name, character_class, race, stats, level=1, experience=0, inventory=None, gold=100, completed_missions=None):
        self.name = name
        self.character_class = character_class
        self.race = race
        self.stats = stats
        self.level = level
        self.experience = experience
        self.inventory = inventory if inventory is not None else []
        self.gold = gold
        self.completed_missions = completed_missions if completed_missions is not None else []
    
    def to_dict(self):
        return {
            'name': self.name,
            'character_class': self.character_class,
            'race': self.race,
            'stats': self.stats,
            'level': self.level,
            'experience': self.experience,
            'inventory': self.inventory,
            'gold': self.gold,
            'completed_missions': self.completed_missions
        }

    @staticmethod
    def from_dict(data):
        return Player(
            data['name'], data['character_class'], data['race'],
            data['stats'], data['level'], data['experience'],
            data['inventory'], data.get('gold', 100),
            data.get('completed_missions', [])
        )

def save_game(player):
    with open('save_game.json', 'w') as f:
        json.dump(player.to_dict(), f)
    print(Fore.GREEN + "Jogo salvo com sucesso!")

def load_game():
    try:
        with open('save_game.json', 'r') as f:
            data = json.load(f)
            player = Player.from_dict(data)
            print(Fore.GREEN + "Jogo carregado com sucesso!")
            return player
    except FileNotFoundError:
        print(Fore.RED + "Nenhum jogo salvo encontrado.")
        return None

def menu():
    while True:
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(Fore.YELLOW + "                    -- EldoriaRPG --                    ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(" 1. Carregar Jogo                                        ")
        print(" 2. Novo Jogo                                           ")
        print(" 3. Sobre o Jogo                                        ")
        print(" 4. Sair do Jogo                                        ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        
        try:
            choice = int(input(Fore.YELLOW + "> Escolha uma opção: "))
        except ValueError:
            print(Fore.RED + "Por favor, insira um número válido.")
            continue
        
        if choice == 1:
            player = load_game()
            if player:
                game_menu(player)
        elif choice == 2:
            player = create_new_game()
            game_menu(player)
        elif choice == 3:
            about_game()
        elif choice == 4:
            print(Fore.GREEN + "Saindo do jogo... Até a próxima!")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

def create_new_game():
    print(Fore.CYAN + "+--------------------------------------------------------+")
    print(Fore.YELLOW + "                -- Criação de Personagem --              ")
    print(Fore.CYAN + "+--------------------------------------------------------+")
    name = input("Digite o nome do seu personagem: ")
    character_class = choose_class()
    race = choose_race()
    stats = initialize_stats(character_class, race)
    player = Player(name, character_class, race, stats)
    print(Fore.GREEN + f"\nPersonagem {name}, {race} {character_class} criado com sucesso!\n")
    return player

def choose_class():
    while True:
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(Fore.YELLOW + " > Escolha sua classe:                                   ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(f" {Fore.RED}1. Guerreiro{Style.RESET_ALL}                                            ")
        print(f" {Fore.GREEN}2. Arqueiro{Style.RESET_ALL}                                            ")
        print(f" {Fore.BLUE}3. Mago{Style.RESET_ALL}                                                ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        
        choice = input("> Escolha sua classe: ")
        if choice == '1':
            print_class_info("Guerreiro")
            if confirm_choice():
                return "Guerreiro"
        elif choice == '2':
            print_class_info("Arqueiro")
            if confirm_choice():
                return "Arqueiro"
        elif choice == '3':
            print_class_info("Mago")
            if confirm_choice():
                return "Mago"
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

def print_class_info(class_name):
    if class_name == "Guerreiro":
        print(
            Fore.RED + """
+--------------------------------------------------------+            
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣠⣾⣿⣿⣶⣦⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉
⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⢉⣉⣉⣉⣉⣉⡉⠙⠛⠻⠿⣿⠟⠋⠀⠀⠀⠀
⠀⠀⢀⣤⣌⣻⣿⣿⣿⣿⣿⣿⠟⢉⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⠿⠛⠋⣉⣁⣀⣀⣀⣉⡉⠛⠻⢿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣿⠃⡴⠋⣁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⠃⠜⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠛⠿⠿⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⡟⠀⢰⣿⣿⣿⡿⠛⢋⣁⣤⣤⣴⣶⣶⣶⣶⣶⣤⣤⣀⣴⣾⠀⠀⠀⠀⠀⠀
⠀⢿⣿⣿⣿⣿⣿⠇⠀⣿⣿⣿⣿⠃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⣶⣿⣿⣿⣿⣿⠀⢰⣿⣿⣿⡏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⠇⠀⢸⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⡿⠛⠋⠉⠉⠉⠛⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⠏⠀⠀⢸⣿⣿⣷⣄⡙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠈⢿⣿⣿⠀⠀⠀⠀⠀⠀
⣸⣿⡿⠟⠁⠀⠀⠀⢸⣿⣿⣿⣿⣿⣄⠙⢿⣿⣿⣿⣿⣿⣷⣶⣤⡄⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀
⠉⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⠈⢻⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠙⠿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢸⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
+--------------------------------------------------------+
                     -- Guerreiro --                        
+--------------------------------------------------------+
 +10% Redução de dano
 +10% Ataque
 +50% Ataque crítico
Habilidades:
 - Frenesi: Libere um dano massivo no inimigo.
 - Seismic Strike: Onda de choque.
 - Iron Skin: Defesa temporária forte.
+--------------------------------------------------------+
"""
        )
    elif class_name == "Arqueiro":
        print(
            Fore.GREEN + """
+--------------------------------------------------------+
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀
⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇
⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠈⢂⠀⠀⠀⠀⠀
+--------------------------------------------------------+
                      -- Arqueiro --                         
+--------------------------------------------------------+
 +15% Velocidade
 +40% Precisão
Habilidades:
 - Tiro rápido: Dispara flechas rapidamente que atravessam múltiplos inimigos.
 - Flecha Fantasma: Atira uma flecha espectral.
+--------------------------------------------------------+
"""
        )
    elif class_name == "Mago":
        print(
            Fore.BLUE + """
+--------------------------------------------------------+            
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀
⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀
⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃
⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀
⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
+--------------------------------------------------------+
                        -- Mago --                          
+--------------------------------------------------------+
 +10% Poder Arcano
 +10% Velocidade de Conjuração
Feitiços:
 - Fireball: Libere chamas poderosas.
 - Frostflare: Vento congelante.
 - Thunderbolt: Relâmpago estrondoso.
+--------------------------------------------------------+
"""
        )

def confirm_choice():
    confirm = input("Esta é sua escolha? (s/n): ")
    return confirm.lower() == 's'

def choose_race():
    while True:
        print(Fore.CYAN + "+-------------------------------------------------------+")
        print(Fore.YELLOW + " > Qual é a sua raça:                                  ")
        print(Fore.CYAN + "+-------------------------------------------------------+")
        print(" 1. Humano                                             ")
        print(" 2. Elfo                                               ")
        print(" 3. Demônio                                            ")
        print(Fore.CYAN + "+-------------------------------------------------------+")
        
        choice = input("> Escolha sua raça: ")
        if choice == '1':
            print_race_info("Humano")
            if confirm_choice():
                return "Humano"
        elif choice == '2':
            print_race_info("Elfo")
            if confirm_choice():
                return "Elfo"
        elif choice == '3':
            print_race_info("Demônio")
            if confirm_choice():
                return "Demônio"
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

def print_race_info(race_name):
    if race_name == "Humano":
        print(
            """
+-------------------------------------------------------+
Humano:
+-------------------------------------------------------+
Os Humanos são adaptáveis e versáteis, com equilíbrio entre atributos.

Atributos:
- Força: 45
- Resistência: 45
- Agilidade: 45
- Destreza: 45
- Inteligência: 45
- Sabedoria: 45
- Sorte: 45
+-------------------------------------------------------+
"""
        )
    elif race_name == "Elfo":
        print(
            """
+-------------------------------------------------------+
Elfo:
+-------------------------------------------------------+
Seres místicos com resistência natural a magia e venenos.

Atributos:
- Força: 40
- Resistência: 30
- Agilidade: 30
- Destreza: 50
- Inteligência: 50
- Sabedoria: 50
- Sorte: 40
Habilidades:
- Imunidade a venenos
- Resistência elemental (raio, fogo, sombrios)
+-------------------------------------------------------+
"""
        )
    elif race_name == "Demônio":
        print(
            """
+-------------------------------------------------------+
Demônio:
+-------------------------------------------------------+
Seres astutos com poderes infernais e resistência ao fogo.

Atributos:
- Força: 40
- Resistência: 50
- Agilidade: 40
- Destreza: 50
- Inteligência: 60
- Sabedoria: 50
- Sorte: 30
Habilidades:
- Manipulação Sombria
- Magia Infernal
- Resistencia ao fogo (50%)
Fraquezas:
- Recebe 150% de dano de luz sagrada
+-------------------------------------------------------+
"""
        )

def initialize_stats(character_class, race):
    base_stats = {
        'HP': 640,
        'MP': 400,
        'Attack': 0,
        'Defense': 0,
        'Speed': 0
    }
    
    if character_class == "Guerreiro":
        base_stats['Attack'] += 10
        base_stats['Defense'] += 10
    elif character_class == "Arqueiro":
        base_stats['Speed'] += 15
    elif character_class == "Mago":
        base_stats['MP'] += 100

    if race == "Humano":
        base_stats['HP'] += 45
    elif race == "Elfo":
        base_stats['HP'] += 30
    elif race == "Demônio":
        base_stats['HP'] += 50

    return base_stats

def game_menu(player):
    while True:
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(Fore.YELLOW + f" > Bem-vindo ao EldoriaRPG, {player.name}!                ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(" 1. Ver Estatísticas                                     ")
        print(" 2. Loja                                                ")
        print(" 3. Missões                                             ")
        print(" 4. Inventário                                          ")
        print(" 5. Salvar Jogo                                         ")
        print(" 6. Sair                                               ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        
        try:
            choice = int(input(Fore.YELLOW + "> Escolha uma opção: "))
        except ValueError:
            print(Fore.RED + "Por favor, insira um número válido.")
            continue
        
        if choice == 1:
            print_stats(player)
        elif choice == 2:
            shop(player)
        elif choice == 3:
            missions(player)
        elif choice == 4:
            inventory(player)
        elif choice == 5:
            save_game(player)
        elif choice == 6:
            print(Fore.GREEN + "Saindo do jogo... Até a próxima!")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

def print_stats(player):
    print(Fore.CYAN + "+-------------------------------------------------------+")
    print(Fore.YELLOW + f"Nome: {player.name}")
    print(Fore.YELLOW + f"Classe: {player.character_class}")
    print(Fore.YELLOW + f"Raça: {player.race}")
    print(Fore.YELLOW + f"Nível: {player.level}")
    print(Fore.YELLOW + f"Experiência: {player.experience} / 100")
    print(Fore.YELLOW + f"HP: {player.stats['HP']} / {640 + (50 if player.race == 'Demônio' else 45 if player.race == 'Humano' else 30)}")
    print(Fore.YELLOW + f"MP: {player.stats['MP']} / {400 + (100 if player.character_class == 'Mago' else 0)}")
    print(Fore.CYAN + "+-------------------------------------------------------+")

def shop(player):
    while True:
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(Fore.YELLOW + f" > Loja (Ouro disponível: {player.gold})                 ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(" 1. Poção de Vida (10 de ouro)                          ")
        print(" 2. Poção de Mana (15 de ouro)                          ")  
        print(" 3. Espada (50 de ouro)                                 ")
        print(" 4. Cajado Arcano (50 de ouro)                          ")
        print(" 5. Arco Composto (50 de ouro)                          ")
        print(" 6. Voltar ao menu anterior                             ")  
        
        choice = input("> Escolha um item para comprar: ")
        if choice == '1':
            if player.gold >= 10:
                if player.stats['HP'] < 640 + (50 if player.race == 'Demônio' else 45 if player.race == 'Humano' else 30):
                    player.inventory.append("Poção de Vida")
                    player.gold -= 10
                    print(Fore.GREEN + "Você comprou uma Poção de Vida!")
                else:
                    print(Fore.YELLOW + "Você já está com HP cheio!")
            else:
                print(Fore.RED + "Ouro insuficiente para comprar a Poção de Vida!")
        
        elif choice == '2':  
            if player.gold >= 15:
                if player.stats['MP'] < 400 + (100 if player.character_class == 'Mago' else 0):
                    player.inventory.append("Poção de Mana")
                    player.gold -= 15
                    print(Fore.GREEN + "Você comprou uma Poção de Mana!")
                else:
                    print(Fore.YELLOW + "Você já está com MP cheio!")
            else:
                print(Fore.RED + "Ouro insuficiente para comprar a Poção de Mana!")
                
        elif choice in ['3', '4', '5']:
            if player.gold >= 50:
                player.inventory.append("Arma comprada")
                player.gold -= 50
                print(Fore.GREEN + "Você comprou um item!")
            else:
                print(Fore.RED + "Ouro insuficiente para comprar este item!")
        elif choice == '6':
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")



def use_item(player, item_index):
    item = player.inventory[item_index]
    
    if item == "Poção de Vida":
        recovered = 60
        max_hp = 640 + (45 if player.race == 'Demônio' else 45 if player.race == 'Humano' else 45)
        player.stats['HP'] = min(player.stats['HP'] + recovered, max_hp)
        print(Fore.GREEN + f"Você usou uma Poção de Vida e recuperou {recovered} de HP!")
        player.inventory.pop(item_index)

    elif item == "Poção de Mana":
        recovered = 50
        max_mp = 400 + (100 if player.character_class == 'Mago' else 0)
        player.stats['MP'] = min(player.stats['MP'] + recovered, max_mp)
        print(Fore.GREEN + f"Você usou uma Poção de Mana e recuperou {recovered} de MP!")
        player.inventory.pop(item_index)
    
    else:
        print(Fore.YELLOW + f"O item '{item}' não pode ser usado agora.")



def nova_missao_caçada(player):
    print("\nUm comerciante pediu sua ajuda para caçar uma criatura perigosa na floresta!")
    combat(player, enemy_name="Lobo Gigante", enemy_hp=90, reward_exp=60, reward_gold=40)
    print("Você caçou o Lobo Gigante com sucesso e salvou o comerciante!")
    player.completed_missions.append("Caçada na Floresta")
    player.inventory.append("Pele de Lobo")
    input("Pressione Enter para retornar ao menu de missões...")

def nova_missao_exploracao(player):
    print("\nVocê explora as ruínas antigas em busca de tesouros esquecidos...")
    print("Mas uma armadilha foi ativada!")
    import random
    dano = random.randint(10, 30)
    player.stats['HP'] -= dano
    print(f"Você sofreu {dano} de dano, mas encontrou um artefato antigo!")
    player.inventory.append("Artefato Antigo")
    player.experience += 70
    player.gold += 35
    level_up(player)
    player.completed_missions.append("Exploração nas Ruínas")
    input("Pressione Enter para retornar ao menu de missões...")

def nova_missao_contrabando(player):
    print("\nUm estranho oferece ouro em troca de ajuda para transportar uma carga suspeita...")
    escolha = input("Você aceita ajudar? (s/n): ").lower()
    if escolha == 's':
        print("Você ajudou no contrabando e ganhou recompensas, mas sente que alguém te observava...")
        player.experience += 60
        player.gold += 70
        player.completed_missions.append("Ajuda ao Contrabando")
        level_up(player)
    else:
        print("Você recusou a proposta suspeita e manteve sua honra intacta.")
    input("Pressione Enter para retornar ao menu de missões...")

def missions(player):
    while True:
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(Fore.YELLOW + " > Escolha uma missão:                                   ")
        print(Fore.CYAN + "+--------------------------------------------------------+")

        print(" 1. Derrote o Dragão das Sombras (Missão Principal)")
        
        mission_map = {
            '2': ("Encontre a Espada Perdida", mission_explore_sword),
            '3': ("Salve a Aldeia dos Elfos", mission_save_village),
            '4': ("Resolver Enigma do Mago", solve_puzzle),
            '5': ("Caçada na Floresta", nova_missao_caçada),
            '6': ("Exploração nas Ruínas", nova_missao_exploracao),
            '7': ("Ajuda ao Contrabando", nova_missao_contrabando)
        }

        for key, (title, _) in mission_map.items():
            if title not in player.completed_missions:
                print(f" {key}. {title} (Missão Secundária)")

        print(" 8. Voltar ao menu anterior")
        print(Fore.CYAN + "+--------------------------------------------------------+")

        choice = input("> Escolha uma missão: ")

        if choice == '1':
            combat(player, enemy_name="Dragão das Sombras", enemy_hp=650, reward_exp=150, reward_gold=100)
        elif choice in mission_map:
            mission_name, mission_func = mission_map[choice]
            if mission_name not in player.completed_missions:
                if choice == '4':
                    if mission_func(player):
                        print(Fore.GREEN + "Você resolveu o enigma e ganhou 50 de experiência e 30 de ouro!")
                        player.experience += 50
                        player.gold += 30
                        level_up(player)
                        player.completed_missions.append(mission_name)
                    else:
                        print(Fore.RED + "Você não conseguiu resolver o enigma.")
                else:
                    mission_func(player)
                    player.completed_missions.append(mission_name)
            else:
                print(Fore.YELLOW + "Você já completou essa missão.")
        elif choice == '8':
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

def combat(player, enemy_name="Inimigo", enemy_hp=300, reward_exp=50, reward_gold=0):
    print(Fore.RED + "+--------------------------------------------------------+")
    print(f"Você encontrou um {enemy_name}! Prepare-se para a batalha!")
    print(Fore.RED + "+--------------------------------------------------------+")
    while enemy_hp > 0 and player.stats['HP'] > 0:
        print(Fore.YELLOW + f"HP do {enemy_name}: {enemy_hp}")
        print(Fore.YELLOW + f"Seu HP: {player.stats['HP']}")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print("Escolha uma ação:")
        print("1. Ataque Físico")
        print("2. Ataque Mágico")
        print("3. Fugir")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        
        action = input("> Escolha uma ação: ")
        if action == '1':
            damage = random.randint(10, 20) + player.stats.get('Attack', 0)
            enemy_hp -= damage
            print(Fore.GREEN + f"Você causou {damage} de dano ao {enemy_name}!")
        elif action == '2':
            if player.stats['MP'] >= 10:
                damage = random.randint(15, 25) + int(player.stats.get('MP', 0)*0.1)
                enemy_hp -= damage
                player.stats['MP'] -= 10
                print(Fore.GREEN + f"Você lançou um ataque mágico e causou {damage} de dano ao {enemy_name}!")
            else:
                print(Fore.RED + "MP insuficiente para ataque mágico!")
                continue
        elif action == '3':
            print(Fore.YELLOW + "Você fugiu da batalha!")
            return
        else:
            print(Fore.RED + "Ação inválida. Tente novamente.")
            continue
        
        # Ataque do inimigo
        enemy_damage = random.randint(30, 50)
        player.stats['HP'] -= enemy_damage
        print(Fore.RED + f"O {enemy_name} causou {enemy_damage} de dano a você!")
        print(Fore.YELLOW + f"HP do {enemy_name}: {max(enemy_hp,0)} | Seu HP: {max(player.stats['HP'],0)}")
        print()
    
    if player.stats['HP'] <= 0:
        print(Fore.RED + "Você foi derrotado! Fim de jogo.")
        exit()
    else:
        print(Fore.GREEN + f"Você derrotou o {enemy_name}!")
        player.experience += reward_exp
        player.gold += reward_gold
        print(Fore.YELLOW + f"Você ganhou {reward_exp} de experiência e {reward_gold} de ouro!")
        level_up(player)

def mission_explore_sword(player):
    print(Fore.CYAN + "\nVocê parte em busca da Espada Perdida...")
    print("No caminho você encontra um inimigo guardando a espada.")
    combat(player, enemy_name="Guardião da Espada", enemy_hp=120, reward_exp=80, reward_gold=30)
    print("Você encontrou a Espada Perdida e a adicionou ao seu inventário!")
    player.inventory.append("Espada Perdida")
    extra_gold = 20
    player.gold += extra_gold
    print(Fore.YELLOW + f"Você também recebeu {extra_gold} de ouro como bônus!")
    input("Pressione Enter para retornar ao menu de missões...")

def mission_save_village(player):
    print(Fore.CYAN + "\nVocê chega à Aldeia dos Elfos, que está sob ataque!")
    print("Você deve defender a aldeia enfrentando vários inimigos.")
    for i in range(2):
        combat(player, enemy_name=f"Inimigo {i+1} da Aldeia", enemy_hp=80, reward_exp=40, reward_gold=20)
        if player.stats['HP'] <= 0:
            print(Fore.RED + "Você não conseguiu salvar a aldeia...")
            return
    print(Fore.GREEN + "Você salvou a Aldeia dos Elfos e ganhou 150 de experiência e 50 de ouro!")
    player.experience += 150
    player.gold += 50
    level_up(player)
    input("Pressione Enter para retornar ao menu de missões...")



def solve_puzzle(player):
    print(Fore.CYAN + "\nVocê encontrou um enigma do Mago!")
    print("Resolva o enigma para continuar: Trago luz na escuridão, Mas queimo o tolo que me toca, Sem mim tudo é frio e sombrio, Quem sou eu??")
    answer = input("> Resposta: ").strip().lower()
    return answer == "fogo"
   

def level_up(player):
    while player.experience >= 100:
        player.level += 1
        player.experience -= 100
        player.stats['HP'] += 20
        player.stats['MP'] += 10
        print(Fore.MAGENTA + f"\nParabéns! Você subiu para o nível {player.level}!")
        print(Fore.MAGENTA + "Seus pontos de HP e MP aumentaram!")

def inventory(player):
    while True:
        print(Fore.CYAN + "+--------------------------------------------------------+")
        print(Fore.YELLOW + " > Inventário                                           ")
        print(Fore.CYAN + "+--------------------------------------------------------+")
        if player.inventory:
            print("Itens no inventário:")
            for idx, item in enumerate(player.inventory, 1):
                print(f" {idx}. {item}")
            print(" 0. Voltar ao menu anterior")
        else:
            print("Você não tem itens no inventário")
            print(" 0. Voltar ao menu anterior")
        
        choice = input("> Escolha um item para usar ou 0 para voltar: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(player.inventory):
                use_item(player, choice - 1)
                input("Pressione Enter para continuar...")
            else:
                print(Fore.RED + "Opção inválida. Tente novamente.")
        else:
            print(Fore.RED + "Entrada inválida. Digite o número da opção.")

def about_game():
    print(Fore.CYAN + "+-------------------------------------------------------+")
    print(Fore.YELLOW + " > Sobre EldoriaRPG                                    ")
    print(Fore.CYAN + "+-------------------------------------------------------+")
    print("EldoriaRPG é um RPG de aventura em texto inspirado por")
    print("clássicos do gênero, desenvolvido integralmente em Python.")
    print("\nDesenvolvido por Pablo Silva, Thiago Guimarães, Vitor Hugo, Fábio Luiz, Diogo Lourenço, Marli, Angelo Rocha, Kadu Luis, Rayan Roque.")
    print(Fore.CYAN + "+-------------------------------------------------------+")
    input("Pressione Enter para voltar ao menu...")
menu()
