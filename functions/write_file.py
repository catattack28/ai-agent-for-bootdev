import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir=os.path.abspath(working_directory) #get jail address
    full_path=os.path.join(working_directory, file_path) #get jail cell
    abs_full_path=os.path.abspath(full_path) #jail cell address
    if not abs_full_path.startswith(abs_working_dir): #if outside jail
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(os.path.dirname(abs_full_path)): 
            os.makedirs(os.path.dirname(abs_full_path), exist_ok=True) #I think this makes the dirs if necessary 
    except Exception as e:
        return f"Error: couldn't create dir: {e}"

    try:
        with open(abs_full_path, 'w') as f:
            f.write(content) #steps 2.4.3 and 2.4.4 at once?
    except Exception as e:
        return f"Error: couldn't create file or write the content: {e}"

    else:
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'




schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes, overwrites files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The path to the working directory. Defaults to current dir"),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to the file you want to create or edit."),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Overwrites the file with this"),
        },
        required=["file_path", "content"],
    ),
)


