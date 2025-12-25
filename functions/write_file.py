import os


def write_file(working_dir, file_path, content):
    #Gets the absolute file path of the working directory
    working_dir_abs = os.path.abspath(working_dir)
    #Gets the absolute file path of the desired file in the directory and normalizes it
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    #Checks if the absolute path of the desired file is in the working directory as a boolean
    valid_target_dir = (os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs)
    if valid_target_dir == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    #Just becuase the desired file path is in the working directory does not mean that all the required subdirectories exist.
    #Makes all required subdirectories.
    target_dir = os.path.dirname(target_file)
    os.makedirs(target_dir, exist_ok=True)

    with open(target_file, "w") as file:
        try:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
            return f"Error: Problem writing to file at {file_path}"
