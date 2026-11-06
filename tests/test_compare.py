import ast
from pathlib import Path
from pydiffer import Codebase, compare_generic

def test_different_code(tmp_path: Path):
    project_a = tmp_path / "project_a"
    project_b = tmp_path / "project_b"

    project_a.mkdir()
    project_b.mkdir()

    (project_a / "main.py").write_text("x = 1")
    (project_b / "main.py").write_text("x = 2")

    result = compare_generic(project_a, project_b)

    assert result.matching == set()
    assert result.differing == {"main.py"}
    assert result.only_in_a == set()
    assert result.only_in_b == set()

def test_matching_code(tmp_path: Path):
    project_a = tmp_path / "project_a"
    project_b = tmp_path / "project_b"

    project_a.mkdir()
    project_b.mkdir()

    (project_a / "main.py").write_text("x = 1")
    (project_b / "main.py").write_text("x = 1")

    result = compare_generic(project_a, project_b)

    assert result.matching == {"main.py"}
    assert result.differing == set()
    assert result.only_in_a == set()
    assert result.only_in_b == set()


def test_unique_files(tmp_path: Path):
    project_a = tmp_path / "project_a"
    project_b = tmp_path / "project_b"

    project_a.mkdir()
    project_b.mkdir()

    (project_a / "one.py").write_text("x = 1")
    (project_b / "two.py").write_text("x = 1")

    result = compare_generic(project_a, project_b)

    assert result.matching == set()
    assert result.differing == set()
    assert result.only_in_a == {"one.py"}
    assert result.only_in_b == {"two.py"}


def test_matching_and_unique_files(tmp_path: Path):
    project_a = tmp_path / "project_a"
    project_b = tmp_path / "project_b"

    project_a.mkdir()
    project_b.mkdir()

    (project_a / "main.py").write_text("x = 1")
    (project_a / "one.py").write_text("x = 1")

    (project_b / "main.py").write_text("x = 1")
    (project_b / "two.py").write_text("x = 1")


    result = compare_generic(project_a, project_b)

    assert result.matching == {"main.py"}
    assert result.differing == set()
    assert result.only_in_a == {"one.py"}
    assert result.only_in_b == {"two.py"}


def test_differing_and_unique_files(tmp_path: Path):
    project_a = tmp_path / "project_a"
    project_b = tmp_path / "project_b"

    project_a.mkdir()
    project_b.mkdir()

    (project_a / "main.py").write_text("x = 1")
    (project_a / "one.py").write_text("x = 1")

    (project_b / "main.py").write_text("x = 2")
    (project_b / "two.py").write_text("x = 1")


    result = compare_generic(project_a, project_b)

    assert result.matching == set()
    assert result.differing == {"main.py"}
    assert result.only_in_a == {"one.py"}
    assert result.only_in_b == {"two.py"}


def test_multiple_files(tmp_path: Path):
    project_a = tmp_path / "project_a"
    project_b = tmp_path / "project_b"

    project_a.mkdir()
    project_b.mkdir()

    (project_a / "main.py").write_text("x = 1")
    (project_a / "one.py").write_text("x = 1")
    (project_a / "three.py").write_text("x = 1")

    (project_b / "main.py").write_text("x = 2")
    (project_b / "two.py").write_text("x = 1")
    (project_b / "three.py").write_text("x = 1")


    result = compare_generic(project_a, project_b)

    assert result.matching == {"three.py"}
    assert result.differing == {"main.py"}
    assert result.only_in_a == {"one.py"}
    assert result.only_in_b == {"two.py"}