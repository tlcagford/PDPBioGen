# Essential for long-running pipelines
class ProgressTracker:
    def __init__(self, total_steps):
        self.total_steps = total_steps
        self.current_step = 0
    
    def start_step(self, step_name):
        self.current_step += 1
        print(f"[{self.current_step}/{self.total_steps}] {step_name}...")
    
    def step_complete(self, message=""):
        print(f"   ✅ Complete {message}")