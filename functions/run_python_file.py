
import os
import subprocess
from google.genai import types



def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir=os.path.abspath(working_directory) #get jail address
    full_path=os.path.join(working_directory, file_path) #get jail cell
    abs_full_path=os.path.abspath(full_path) #jail cell address
    if not abs_full_path.startswith(abs_working_dir): #if outside jail
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'


    try:  #running python using subprocess

        pos_args = ["python", file_path] + args

        completed_process = subprocess.run(
           pos_args, 
           timeout=30, 
           capture_output = True, 
           cwd=abs_working_dir,
           text=True)

        out=completed_process.stdout or ""
        err=completed_process.stderr or ""
        code=completed_process.returncode

        if out == "" and err == "":
            return "No output produced"

        formatted_output_string = f"STDOUT: {out} \nSTDERR: {err}"
        if code != 0:
            return formatted_output_string + " Process exited with code {code}"

    except Exception as e:
        return f"Error: executing Python file: {e}"

    return formatted_output_string




schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a file in python3",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The path to the working directory. Defaults to current dir"),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to the file you want to run."),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="A list of string arguments to pass into the script. Defaults to an empty list."),
        },
        required=["file_path"],
    ),
)
