class Process:
    def __init__(self, pid, instructions):
        self.pid = pid
        self.instructions = instructions
        self.state = "READY"
        self.pc = 0
        self.registers = [0] * 8
        self.memory = [0] * 256

    def execute_instruction(self):
        if self.pc < len(self.instructions):
            instruction = self.instructions[self.pc]
            self.pc += 1
            return instruction
        else:
            self.state = 'TERMINATED'
            return None

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.next_pid = 1

    def create_process(self, instructions):
        pid = self.next_pid
        self.next_pid += 1
        process = Process(pid, instructions)
        self.processes[pid] = process
        return process
        
    def terminate_process(self, pid):
        if pid in self.processes:
            del self.processes[pid]
        else:
            print(f"No process with PID {pid}")

    def get_all_processes(self):
        return self.processes