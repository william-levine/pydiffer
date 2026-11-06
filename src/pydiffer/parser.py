from pydiffer.codebase import Codebase
from pathlib import Path
import ast

def parse_codebase(path: Path) -> Codebase:
    file_structure : dict[str, ast.AST] = {}
    
    files = path.rglob(f'*.py')
    for file in files:
        relative_path = file.relative_to(path)
        ast_tree = ast.parse(file.read_text())
        # as_posix() normalises the path to "parent/child" (instead of "parent\\child")
        file_structure[relative_path.as_posix()] = ast_tree
    
    codebase = Codebase(path.name, path, file_structure)
    return codebase