from pathlib import Path
import yaml

def load_system_prompt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    

def load_Path_system_prompt(path_object: Path) -> str:
    content = path_object.read_text(encoding='utf-8')    
    return content

def load_yaml_system_prompt(file_path: str) -> str:
    
    with open(file_path) as f:
        try: 
            content = yaml.load(f, Loader=yaml.FullLoader)
            # print("YAML FILE READ SUCCESS: ", content)
        except Exception as e: 
            print("Error reading yaml file:", e)
    
    return content



# print(load_yaml_system_prompt("agent/Prompts/QuestionAnsweringAgent.yaml")['messages'][1])