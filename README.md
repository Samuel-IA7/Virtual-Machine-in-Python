# Virtual-Machine-in-Python
## DOCUMENTAÇÃO

# Módulo virtual_machine.py
Classe VM
A classe VM representa a máquina virtual que gerencia a execução dos processos e suas instruções.
Métodos
•	__init__(self):
o	Inicializa a máquina virtual, criando instâncias de ProcessManager, Scheduler, e InstructionSet.
o	self.current_process é usado para rastrear o processo em execução no momento.
•	run(self):
o	Controla o ciclo de execução da máquina virtual.
o	A cada iteração, a função verifica se há processos na fila de prontos (ready_queue). Se houver, um processo é selecionado e seu estado é definido como RUNNING.
o	Enquanto o processo está em execução, a instrução atual é executada.
o	Se o processo terminar (TERMINATED), ele é marcado como terminado. Caso contrário, ele é reprogramado na fila.
•	execute_instruction(self, process, instruction):
o	Executa a instrução do processo, buscando a função correspondente no conjunto de instruções (InstructionSet).
o	Caso a instrução não seja reconhecida, uma mensagem de erro é impressa.

# Módulo scheduler.py
Classe Scheduler
O Scheduler é responsável por gerenciar a fila de processos prontos e determinar a ordem de execução dos processos.
Métodos
•	__init__(self):
o	Inicializa a fila de processos prontos (ready_queue) e a referência ao processo em execução no momento.
•	add_process(self, process):
o	Adiciona um processo à fila de prontos se seu estado for READY.
•	schedule_next(self):
o	Seleciona o próximo processo da fila de prontos, define seu estado como RUNNING e retorna o processo selecionado.
•	mark_as_waiting(self, process):
o	Altera o estado do processo para WAITING.
•	mark_as_terminated(self, process):
o	Altera o estado do processo para TERMINATED.
•	reschedule(self):
o	Reprograma o processo atual (que está em execução) voltando-o para a fila de prontos com o estado READY.

# Módulo process_manager.py
Classe ProcessManager
O ProcessManager é responsável por criar e gerenciar os processos.
Métodos
•	__init__(self):
o	Inicializa um dicionário para armazenar processos (processes) e um contador para o próximo PID (next_pid).
•	create_process(self, instructions):
o	Cria um novo processo com as instruções fornecidas, atribui um PID único e o adiciona ao dicionário de processos.
•	terminate_process(self, pid):
o	Remove o processo do dicionário de processos com base no PID.
•	get_all_processes(self):
o	Retorna todos os processos ativos.

# Módulo process.py
Classe Process
A classe Process representa um processo em execução na VM, contendo suas instruções, estado, e registros.
Métodos
•	__init__(self, pid, instructions):
o	Inicializa o processo com um identificador único (pid), uma lista de instruções (instructions), e configura o estado inicial como READY.
•	execute_instruction(self):
o	Executa a próxima instrução na lista e avança o contador de programa (pc).
o	Se todas as instruções forem executadas, o estado do processo é definido como TERMINATED.

# Módulo instruction_set.py
Classe InstructionSet
O InstructionSet contém todas as operações que podem ser executadas pela VM, incluindo operações aritméticas, controle de fluxo, manipulação de memória, e execução de áudio.
Métodos
•	__init__(self, vm):
o	Inicializa o conjunto de instruções, recebendo uma instância da VM.
o	Inicializa o mixer do Pygame para tocar músicas.
•	PLAY_MUSIC(self, args):
o	Carrega e toca uma música em loop. O processo que executa esta instrução é mantido no estado RUNNING.
•	STOP_MUSIC(self, args):
o	Para a música e termina o processo que a executa.
•	CHOOSE_MUSIC(self, args):
o	Escolhe uma música específica para tocar.
•	GUESS_NUMBER(self, args):
o	Implementa um jogo de adivinhação de número, que termina o processo ao final do jogo.

# Módulo cli.py
Classe CLI
A CLI (Command Line Interface) fornece uma interface para interagir com a máquina virtual.
Métodos
•	__init__(self, vm):
o	Inicializa a CLI com uma referência à VM.
•	start(self):
o	Inicia o loop principal da CLI, esperando por comandos do usuário.
•	list_processes(self):
o	Lista todos os processos ativos e seus estados.
•	show_music_menu(self):
o	Exibe um menu para o usuário escolher músicas.
•	handle_music_choice(self, choice):
o	Processa a escolha do usuário e retorna as instruções correspondentes.
•	ensure_music_stopped(self):
o	Verifica e garante que a música foi interrompida.
•	create_process(self, args):
o	Cria um processo com base no tipo de processo especificado (music_player ou guess_game).
•	run_process(self, args):
o	Executa um processo específico com base no PID.
•	monitor_resources(self):
o	Função fictícia para monitorar recursos (não implementada).
