"""Hangman Game (Jogo da Forca).

Programação Orientada a Objetos
"""
# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    def __init__(self, word):
        self.word = word
        self.letras_erradas = []
        self.letras_corretas = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.letras_corretas:
            self.letras_corretas.append(letter)
        elif letter not in self.word and letter not in self.letras_erradas:
            self.letras_erradas.append(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 7)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        hide = ''
        for letra in self.word:
            if letra in self.letras_corretas:
                hide += letra
            else:
                hide += '_'
        return hide

    def print_game_status(self):
        """Método para checar o status do game e imprimir o board na tela."""
        print(board[len(self.letras_erradas)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ',)
        for letra in self.letras_erradas:
            print(letra,)
        print('\nLetras corretas: ',)
        for letra in self.letras_corretas:
            print(letra,)
        print()


def rand_word():
    """Função para ler uma palavra de forma aleatória do banco de palavras."""
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado,
    # print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        letra = input('Digite uma letra: ')
        game.guess(letra)

    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)
        print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
