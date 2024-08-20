class Scheduler:
    def __init__(self):
        self.ready_queue = []
        self.current_process = None

    def add_process(self, process):
        if process.state == 'READY':
            self.ready_queue.append(process)

    def schedule_next(self):
        if not self.ready_queue:
            return None

        self.current_process = self.ready_queue.pop(0)
        self.current_process.state = 'RUNNING'
        return self.current_process

    def mark_as_waiting(self, process):
        process.state = 'WAITING'

    def mark_as_terminated(self, process):
        process.state = 'TERMINATED'

    def reschedule(self):
        if self.current_process and self.current_process.state == 'RUNNING':
            self.current_process.state = 'READY'
            self.ready_queue.append(self.current_process)
