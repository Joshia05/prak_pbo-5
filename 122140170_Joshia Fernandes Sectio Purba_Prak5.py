import random

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan metode abstrak")

    def display_winner(self, winner):
        print(f"Pemenang nya adalah {winner}!")

    def display_draw(self):
        print("Permainan Seimbang!")


class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan metode abstrak")


class HumanPlayer(Player):
    def make_move(self):
        move = input(f"{self.name}, tentukan pilihanmu: ")
        return move


class ComputerPlayer(Player):
    def make_move(self):
        move = random.choice(['batu', 'kertas', 'gunting'])
        print(f"{self.name} chooses {move}")
        return move


class BatuGuntingKertas(Game):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)

    def play(self):
        while True:
            move1 = self.player1.make_move()
            move2 = self.player2.make_move()
            if move1 == move2:
                self.display_draw()
            elif (move1 == 'batu' and move2 == 'gunting') or \
                 (move1 == 'kertas' and move2 == 'batu') or \
                 (move1 == 'gunting' and move2 == 'kertas'):
                self.display_winner(self.player1.name)
            else:
                self.display_winner(self.player2.name)
            play_again = input("Apakah kamu ingin lanjut ? (yes/no): ")
            if play_again.lower() != 'Iya':
                break


if __name__ == "__main__":
    player1_name = input("Masukkan nama player 1: ")
    player2_name = input("Masukkan nama player 2: ")
    
    if player2_name.lower() == 'computer':
        player2 = ComputerPlayer("Computer")
    else:
        player2 = HumanPlayer(player2_name)
    
    player1 = HumanPlayer(player1_name)
    
    game = BatuGuntingKertas(player1, player2)
    game.play()