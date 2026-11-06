from dataclasses import dataclass
import pydiffer.parser as parser
import ast
from pathlib import Path


@dataclass
class ComparisonResult:
    """
    Represents a codebase comparison result.
    
    Attributes: 
        matching: The set of modules that are in both codebases with the same code.
        differing: The set of modules that are in both codebases with different code.
        only_in_a: The set of modules that are only in Codebase A
        only_in_b: The set of modules that are only in Codebase B
    """
    
    matching: set[str]
    differing: set[str]
    only_in_a: set[str]
    only_in_b: set[str]


def compare_generic(path_a: str | Path, path_b: str | Path) -> ComparisonResult:
    """
    Performs a basic comparison between two codebases based on their file structure and ASTs.
    
    Args:
        `path_a`: The path to Codebase A
        `path_b`: The path to Codebase B
    
    Returns:
        A `ComparisonResult` containing files that match, differ, or exist in only one of the two codebases.
    """

    codebase_a = parser.parse_codebase(path_a)
    codebase_b = parser.parse_codebase(path_b)

    files_a = set(codebase_a.files)
    files_b = set(codebase_b.files)

    m = files_a & files_b
    d = set()

    # m.copy() to avoid the size changing during iteration
    for path in m.copy():
        tree_a = codebase_a.files[path]
        tree_b = codebase_b.files[path]

        if ast.dump(tree_a) != ast.dump(tree_b):
            d.add(path)
            m.remove(path)
    
    a = files_a - files_b
    b = files_b - files_a

    return ComparisonResult(m, d, a, b)