import pygame  # Adicione esta linha
import time

class CLI:
    def __init__(self, vm):
        self.vm = vm

    def start(self):
        while True:
            command = input("> ").strip().split()
            if not command:
                continue
            cmd, *args = command
            if cmd == "create_process":
                self.create_process(args)
            elif cmd == "run_vm":
                self.vm.run()
            elif cmd == "run_process":
                self.run_process(args)
            elif cmd == "list_processes":
                self.list_processes()
            elif cmd == "monitor_resources":
                self.monitor_resources()
            elif cmd == "exit":
                break
            else:
                print(f"Unknown command: {cmd}")

    def list_processes(self):
        processes = self.vm.process_manager.get_all_processes()
        if not processes:
            print("No processes are running.")
        else:
            print(f"Total of {len(processes)} process(es):")
            for pid, process in processes.items():
                print(f"PID: {pid}, State: {process.state}")

    def show_music_menu(self):
        print("Escolha uma das músicas para tocar:")
        print("1. Música 1")
        print("2. Música 2")
        print("3. Parar música")
        choice = input("Digite o número da sua escolha: ")
        return choice

    def handle_music_choice(self, choice):
        if choice == "1":
            return [("CHOOSE_MUSIC", "song1"), ("PLAY_MUSIC", "song1")]
        elif choice == "2":
            return [("CHOOSE_MUSIC", "song2"), ("PLAY_MUSIC", "song2")]
        elif choice == "3":
            return [("STOP_MUSIC",)]
        else:
            print("Escolha inválida.")
            return []

    def ensure_music_stopped(self):
        # Verifica e garante que a música seja parada
        import time
        max_retries = 5  # Tentativas máximas para garantir a parada
        retries = 0
        while retries < max_retries and pygame.mixer.music.get_busy():
            print("Parando música...")
            pygame.mixer.music.stop()
            time.sleep(1)  # Aguarda um tempo antes de verificar novamente
            retries += 1

        if not pygame.mixer.music.get_busy():
            print("Música foi parada com sucesso.")
        else:
            print("Falha ao parar a música após várias tentativas.")

    def create_process(self, args):
        if args[0] == "music_player":
            choice = self.show_music_menu()
            instructions = self.handle_music_choice(choice)
            if instructions:
                process = self.vm.process_manager.create_process(instructions)
                self.vm.scheduler.add_process(process)
                print(f"Processo 'music_player' criado com PID {process.pid}")
        elif args[0] == "guess_game":
            instructions = [("GUESS_NUMBER",)]
            process = self.vm.process_manager.create_process(instructions)
            self.vm.scheduler.add_process(process)
            print(f"Processo 'guess_game' criado com PID {process.pid}")
        else:
            print("Unknown process")

    def run_process(self, args):
        print(f"Running process with PID {args[0]}")

    def monitor_resources(self):
        print("Monitoring resources (mock implementation)")
