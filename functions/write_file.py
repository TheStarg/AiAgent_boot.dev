import os


def write_file(working_directory, file_path, content):

    working_dir_abs = os.path.abspath(working_dir)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = (os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs)
    if valid_target_dir == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    dicts = ""

    for content in os.listdir(target_dir):
        relative_path = os.path.join(target_dir, content)
        abs_path = os.path.abspath(relative_path)

        try:
            os.path.getsize(abs_path)
        except:
            print(f"Error: Failed to get size of {abs_path}")
        try:
            os.path.isdir(abs_path)
        except:
            print(f"Error: Failed to deterimine if {abs_path} is a directory or not")

        dicts = dicts + f"- {content}: file_size={os.path.getsize(abs_path)}, is_dir={os.path.isdir(abs_path)}\n"
    return dicts


