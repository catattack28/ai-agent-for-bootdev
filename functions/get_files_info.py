import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    abs_working_dir=os.path.abspath(working_directory) #get jail address
    full_path=os.path.join(working_directory, directory) #get jail cell
    abs_full_path=os.path.abspath(full_path) #jail cell address
    if not abs_full_path.startswith(abs_working_dir): #if outside jail
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        files = os.listdir(abs_full_path) #lists contents 
        dir_contents=""
        for f in files:
            filepath=os.path.join(abs_full_path, f)
            file_size=os.path.getsize(filepath)
            is_dir=os.path.isdir(filepath)
            dir_contents+=f" - {f}: file_size={file_size} bytes, is_dir={is_dir}\n"
        return dir_contents
    except Exception as e:
        return f"Error: {str(e)}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
