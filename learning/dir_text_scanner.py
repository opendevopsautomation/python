import os
class Directory():

    def __init__(self,path:str) -> None:
        self.path = path
    
    def traverse(self):
        for root,dirs,files in os.walk(self.path):
            for name in files:
                 # Only target specific file extensions
                # if not name.endswith(('.txt', '.log')):
                #     continue  # Skip non-matching files
                file_path = os.path.join(root,name)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        for line_number, line in enumerate(file, 1):
                            if "string" in line.lower():
                                print(f'"string" found in file: {file_path}, line {line_number}')
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")



obj=Directory('/Users/vikas/Downloads/')
obj.traverse()
