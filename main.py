from virtual_machine import VM
from cli import CLI 

def main():
    # Cria a instância da VM
    vm = VM()

    # Cria a instância da CLI, passando a VM para ela
    cli = CLI(vm)

    # Inicia a interface de linha de comando
    cli.start()

if __name__ == "__main__":
    main()

