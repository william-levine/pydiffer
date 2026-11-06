from dataclasses import dataclass
import pydiffer.parser as parser
import ast
from pathlib import Path


@dataclass
class ComparisonResult:
    matching: list[str]
    differing: list[str]
    only_in_a: list[str]
    only_in_b: list[str]


def compare_generic(path_a: str | Path, path_b: str | Path):
    codebase_a = parser.parse_codebase(Path(path_a))
    codebase_b = parser.parse_codebase(Path(path_b))

    files_a = set(codebase_a.files)
    files_b = set(codebase_b.files)

    m = list(files_a & files_b)
    d = []

    # m.copy() to avoid the size changing during iteration
    for path in m.copy():
        tree_a = codebase_a.files[path]
        tree_b = codebase_b.files[path]

        if ast.dump(tree_a) != ast.dump(tree_b):
            d.append(path)
            m.remove(path)
    
    a = list(files_a - files_b)
    b = list(files_b - files_a)

    return ComparisonResult(m, d, a, b)