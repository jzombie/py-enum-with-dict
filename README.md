# EnumWithDict

`EnumWithDict` is a Python package that extends the standard library's `Enum` class to include `to_dict` and `get_initial` class methods. This enhancement allows for straightforward conversion of enum classes to dictionaries and provides easy access to the initial enum value, facilitating a more versatile use of enumerations in Python applications.

## Features

- **to_dict**: Convert an enum class to a dictionary representation, mapping member names to their values.
- **get_initial**: Retrieve the first value defined in the enum, useful for cases where a default or initial value is needed.

## Installation

Install `EnumWithDict` using pip:

```bash
pip install enum_with_dict
```

## Usage

### Defining an Enum with `EnumWithDict`

```python
from enum_with_dict import EnumWithDict

class Color(EnumWithDict):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

```

### Converting an Enum to a Dictionary

```python
color_dict = Color.to_dict()
print(color_dict)
# Output: {'RED': 'red', 'GREEN': 'green', 'BLUE': 'blue'}
```

### Getting the Initial Enum Value

```python
initial_color = Color.get_initial()
print(initial_color)
# Output: 'red'
```

## LICENSE

`EnumWithDict` is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
