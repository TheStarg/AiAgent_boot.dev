import os
from config import MAX_CHARS

def get_file_content(working_dir, file_path):

    working_dir_abs = os.path.abspath(working_dir)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = (os.path.commonpath([working_dir_abs, target_dir]) in working_dir_abs)
    if valid_target_file == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isfile(target_dir) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
   
    with open(target_dir, "r") as file:
        try:
            contents = file.read(MAX_CHARS)
            if file.read(1):
                contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        except:
            return f"Error: Problem opening or reading file at {file_path}"
    return contents

