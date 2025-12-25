import subprocess
import os
def run_python_file(working_dir, file_path, args=None):
    #Gets the absolute file path of the working directory
    working_dir_abs = os.path.abspath(working_dir)
    #Gets the absolute file path of the desired file in the directory and normalizes it
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    #Checks if the absolute path of the desired file is in the working directory as a boolean
    valid_target_dir = (os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs)

    if valid_target_dir == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif os.path.isfile(target_file) == False:
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if target_file.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_file]
    if args != None:
        command.extend(args)
    try:
        process_return = subprocess.run(command, text=True, capture_output=True, timeout=30)
        if process_return.returncode != 0:
            return f"Process exited with return code {process_return.returncode}"
        elif process_return.stdout == None and process_return.stdstderr == None:
            return "No output produced"
        else:
            return f"STDOUT: {process_return.stdout}STDERR: {process_return.stderr}\n"
    except:
        return f"Error: executing Python file: {e}"
    

