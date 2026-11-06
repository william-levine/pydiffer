from dataclasses import dataclass
from pathlib import Path
import ast

@dataclass
class Codebase:
    """
    Represents a Python codebase.

    Attributes: 
        `name`: The name of the Python codebase.
        `path`: The path to the Python codebase.
        `files`: Mapping of module name to ASTs.
    """

    name: str
    path: Path
    files: dict[str, ast.AST]