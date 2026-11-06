from pydiffer.codebase import Codebase
from pathlib import Path
import ast

def parse_codebase(path: str | Path) -> Codebase:
    """
    Performs a basic comparison between two codebases based on their file structure and ASTs.
    
    Args:
        `path`: The path to the codebase
    
    Returns:
        A `Codebase` object containing the codebase name, path, and mapping of modules to ASTs.
    """

    path = Path(path)
    files = path.rglob(f'*.py')
    file_structure : dict[str, ast.AST] = {}
    
    for file in files:
        relative_path = file.relative_to(path)
        ast_tree = ast.parse(file.read_text())
        # as_posix() normalises the path to "parent/child" (instead of "parent\\child")
        file_structure[relative_path.as_posix()] = ast_tree
    
    codebase = Codebase(path.name, path, file_structure)
    return codebase