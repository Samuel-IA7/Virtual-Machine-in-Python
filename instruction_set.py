import pygame
import os
import random

class InstructionSet:
    def __init__(self, vm):
        self.vm = vm
        pygame.mixer.init()

    def ADD(self, args):
        self.vm.registers[args[0]] = self.vm.registers[args[1]] + self.vm.registers[args[2]]

    def SUB(self, args):
        self.vm.registers[args[0]] = self.vm.registers[args[1]] - self.vm.registers[args[2]]

    def JMP(self, args):
        self.vm.pc = args[0]

    def JZ(self, args):
        if self.vm.registers[args[1]] == 0:
            self.vm.pc = args[0]

    def LOAD(self, args):
        self.vm.registers[args[0]] = self.vm.memory[args[1]]

    def STORE(self, args):
        self.vm.memory[args[1]] = self.vm.registers[args[0]]

    def PLAY_MUSIC(self, args):
        song_path = os.path.join("assets", "songs", f"{args[0]}.mp3")
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(-1)  # O "-1" faz a música tocar em loop.
        print(f"Tocando música: {args[0]}")
        if self.vm.current_process:
            self.vm.current_process.state = 'RUNNING'
    
    def STOP_MUSIC(self, args):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            print("Música parada")
            if self.vm.current_process:
                self.vm.current_process.state = 'TERMINATED'

    def CHOOSE_MUSIC(self, args):
        self.vm.current_music = args[0]
        print(f"Música selecionada: {args[0]}")

    def INC(self, args):
        self.vm.registers[args[0]] += 1

    def PRINT(self, args):
        print(f"Valor do registro {args[0]}: {self.vm.registers[args[0]]}")

    def GUESS_NUMBER(self, args):
        number_to_guess = random.randint(1, 100)
        attempts = 0
        print("Adivinhe o número entre 1 e 100:")
        while True:
            guess = int(input("Seu palpite: "))
            attempts += 1
            if guess < number_to_guess:
                print("Muito baixo!")
            elif guess > number_to_guess:
                print("Muito alto!")
            else:
                print(f"Parabéns! Você acertou em {attempts} tentativas.")
                if self.vm.current_process:
                    self.vm.current_process.state = 'TERMINATED'
                break
