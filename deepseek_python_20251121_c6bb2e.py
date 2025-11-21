# Missing: Cleanup strategy
class WorkspaceManager:
    def __init__(self, output_dir, keep_intermediates=False):
        self.keep_intermediates = keep_intermediates
        self.temp_files = []
    
    def register_temp_file(self, file_path):
        self.temp_files.append(file_path)
    
    def cleanup(self):
        if not self.keep_intermediates:
            for temp_file in self.temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)