#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set()
        while len(self.mines) < mines:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            self.mines.add((x, y))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        for y in range(self.height):
            print(f'{y:2} ', end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (x, y) in self.mines:
                        print('💣', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else '·', end=' ')
                else:
                    print('■', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("❌ Coordonnées hors limites.")
            return True  # Ne termine pas le jeu

        if self.revealed[y][x]:
            return True  # Déjà révélé

        if (x, y) in self.mines:
            return False  # Mine touchée

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (x, y) not in self.mines:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Entrez la coordonnée X : "))
                y = int(input("Entrez la coordonnée Y : "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 BOOM ! Tu as touché une mine. Game Over.")
                    break
                elif self.check_win():
                    self.print_board(reveal=True)
                    print("🎉 Félicitations ! Tu as gagné !")
                    break
            except ValueError:
                print("❌ Entrée invalide. Entrez uniquement des nombres.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()