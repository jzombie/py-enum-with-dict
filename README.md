# EnumWithDict

`EnumWithDict` is a Python package that extends the standard library's Enum class to include `to_dict`, `get_initial`, and other class methods. This enhancement allows for the straightforward conversion of enum classes to dictionaries, easy access to the initial enum value, and additional functionalities such as retrieving enum values with a fallback option, validating mappings, and more.

## Extends Enum with the Following Methods:

- **to_dict**: Convert an enum class to a dictionary representation, mapping member names to their values.
- **get_initial**: Retrieve the first value defined in the enum, useful for cases where a default or initial value is needed.
- **get**: Mimics the dictionary `get` method, allowing retrieval of enum values with an optional default fallback. Additionally, it supports an optional custom mapping dictionary for dynamically mapped value retrieval.
- **validate_mapping_keys**: Ensure that a provided mapping includes all enum values, raising an error for any missing mappings.
- **map**: Map enum members to values based on the provided dictionary.
- **keys**: Retrieve the keys of the enum class as a list or as a KeysView.
- **values**: Retrieve the values of the enum class as a list or as a ValuesView.

## Installation

Install `EnumWithDict` using pip:

```bash
pip install enum-with-dict
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

### Using the `get` Method

Retrieve an enum value by its name, with an option to specify a default value if the name does not exist. Additionally, you can pass a custom mapping dictionary to retrieve a mapped value instead of the enum's default value.

#### Get a value for an existing key

```python
print(Color.get('RED'))  # Output: 'red'
```

### Get a value for a non-existing key with a default value

```python
print(Color.get('PURPLE', default='unknown'))  # Output: 'unknown'
```

### Get a value for a non-existing key, falling back to the initial value

```python
print(Color.get('PURPLE'))  # Output: 'red'
```

### Get a value using a custom mapping

You can also use a custom mapping dictionary to retrieve a value. This is useful when you need to map enum members to different values dynamically.

```python
custom_mapping = {'RED': 'Rouge', 'GREEN': 'Vert', 'BLUE': 'Bleu'}
print(Color.get('RED', mapping=custom_mapping))  # Output: 'Rouge'
```

## Ensuring Completeness of Mappings with `validate_mapping_keys`

Validate that a provided mapping covers all enum members.

```python
# Assuming a partial mapping for demonstration
partial_mapping = {'RED': 'Rouge', 'GREEN': 'Vert'}

try:
    Color.validate_mapping_keys(partial_mapping)
except ValueError as e:
    print(e)
# Expected output: Missing mappings for: BLUE
```

### Mapping Enum Members with `map`

Map enum members to values using the provided dictionary.

This mapping operation does not alter the values within the Enum itself; instead, it generates a new dictionary with the same keys and updated values.

Internally, `validate_mapping_keys` is invoked to confirm that the keys align with the Enum members, but the value types remain arbitrary.

```python
# Define the key mapping
key_mapping = {
    TestEnum.VALUE_1: "some_new_value",
    TestEnum.VALUE_2: "another_new_value",
    TestEnum.VALUE_3: "a new value"
}

# Perform the mapping and validate
mapped_values = TestEnum.map(key_mapping)

# ----- The above is equivalent to the following: -----

# Validate the mapped values
expected_values = {
    TestEnum.VALUE_1.name: "some_new_value",
    TestEnum.VALUE_2.name: "another_new_value",
    TestEnum.VALUE_3.name: "a new value"
}

assert mapped_values == expected_values

```

## Retrieving Keys and Values with `keys()` and `values()`

Retrieve the keys and values of the enum class as a list or as a `KeysView` or `ValuesView`.

### Get keys as a list

```python
keys_list = Color.keys()
```

### Get keys as a `KeysView`

```python
keys_view = Color.keys(as_list=False)
```

### Get values as a list

```python
values_list = Color.values()
```

### Get values as a ValuesView

```python
values_view = Color.values(as_list=False)
```

## LICENSE

`EnumWithDict` is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
