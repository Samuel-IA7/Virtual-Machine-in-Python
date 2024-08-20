from process_manager import ProcessManager
from scheduler import Scheduler
from instruction_set import InstructionSet

class VM:
    def __init__(self):
        self.process_manager = ProcessManager()
        self.scheduler = Scheduler()
        self.instruction_set = InstructionSet(self)
        self.current_process = None

    def run(self):
        while True:
            process = self.scheduler.schedule_next()
            if not process:
                print("No more processes to run.")
                break
            
            self.current_process = process
            print(f'{process.pid}' +': '+ process.state)
            while process.state == 'RUNNING':
                instruction = process.execute_instruction() #esta linha que esta modificando pra terminated o processo
                
                if instruction:
                    self.execute_instruction(process, instruction)
                

                # Se o processo foi terminado, marque-o como terminado e não o reponha na fila
                if process.state == 'TERMINATED':
                    self.scheduler.mark_as_terminated(process)
                    
                else:
                    self.scheduler.reschedule()

    def execute_instruction(self, process, instruction):
        opcode, *args = instruction
        method = getattr(self.instruction_set, opcode, None)
        if method:
            method(args)
        else:
            print(f"Unknown instruction {opcode} for process {process.pid}")

