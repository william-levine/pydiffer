from dataclasses import dataclass
from pathlib import Path
import ast

@dataclass
class Codebase:
    name: str
    path: Path
    files: dict[str, ast.AST]