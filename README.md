# pydiffer

## Installation

`pydiffer` is currently in development and is not yet available on PyPI.

To install the latest development version directly from GitHub:

### Using HTTPS

```bash
pip install git+https://github.com/william-levine/pydiffer.git
```

### Using SSH
```bash
pip install git+ssh://git@github.com/william-levine/pydiffer.git
```


## Example Usage
```python
from pydiffer import compare_generic

result = compare_generic("project_a_path", "project_b_path")

print(result.matching)  # Returns the Python files that are identical
print(result.differing) # Returns the Python files that have the same name but differing code
print(result.only_in_a) # Returns the Python files that are only in Project A
print(result.only_in_b) # Returns the Python files that are only in Project B
```