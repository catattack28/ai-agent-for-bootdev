from pathlib import Path
import os
import config
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        file_path_str = os.path.join(working_directory,file_path)
        file_path = Path(file_path_str)   
        if not file_path.is_relative_to(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not file_path.is_file():
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(file_path, "r") as f:
            file_content_string = f.read(1+config.CHARACTER_LIMIT) 
            #added one to check if over
            if len(file_content_string)>1000:
                file_content_string=file_content_string[:-1]+f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"





schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the file's content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself."),
                "file_path" : types.Schema(
                    type=types.Type.STRING,
                    description="The filepath to the file whose contents you want to read."),
                    },
        required=["file_path"],
    ),
)
