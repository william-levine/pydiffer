import ast
from pathlib import Path
from pydiffer.parser import parse_codebase
import pytest


def test_parse_python_file(tmp_path: Path):
    project = tmp_path / "project"
    project.mkdir()

    (project / "main.py").write_text("x = 1")

    result = parse_codebase(project)

    print(f"project {project}")

    assert result.name == "project"
    assert result.path == project
    assert "main.py" in result.files
    assert isinstance(result.files["main.py"], ast.AST)


def test_parse_multiple_files(tmp_path: Path):
    project = tmp_path / "project"
    project.mkdir()

    (project / "main.py").write_text("x = 1")
    (project / "utils.py").write_text("y = 'test'")

    result = parse_codebase(project)

    # convert to a set to get the keys
    assert set(result.files) == {"main.py", "utils.py"}


def test_parse_nested_files(tmp_path: Path):
    project = tmp_path / "project"
    utils = project / "utils"
    
    project.mkdir()
    utils.mkdir()

    (project / "main.py").write_text("x = 1")
    (utils / "utils.py").write_text("y = 'test'")

    result = parse_codebase(project)

    # convert to a set to get the keys
    assert set(result.files) == {"main.py", "utils/utils.py"}


def test_ignores_non_python_files(tmp_path: Path):
    project = tmp_path / "project"
    project.mkdir()

    (project / "main.py").write_text("x = 1")
    (project / "README.md").write_text("# Project")
    (project / "info.txt").write_text("information")

    result = parse_codebase(project)

    assert set(result.files) == {"main.py"}


def test_invalid_python_syntax(tmp_path: Path):
    project = tmp_path / "project"
    project.mkdir()

    (project / "main.py").write_text("x = 2 + ")

    with pytest.raises(SyntaxError):
        parse_codebase(project)