import json
from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # Will this be working?
    lines = open(path, 'r').read().split('\n')
    return lines


def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    processed_file_list = []
    for english_line, german_line in zip(english_file_list, german_file_list):
        # Remove leading and trailing whitespaces, and line breaks
        english_line = english_line.strip()
        german_line = german_line.strip()
        
        # Create a dictionary with English and German keys
        data = {
            "English": english_line,
            "German": german_line
        }
        
        # Convert the dictionary to a JSON string
        json_string = json.dumps(data, ensure_ascii=False)
        
        processed_file_list.append(json_string)
        
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')