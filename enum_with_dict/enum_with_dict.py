from enum import Enum
from typing import Any, Dict, List, KeysView, ValuesView, Union


class EnumWithDict(Enum):
    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        """Return a dictionary representation of the enum."""
        return {member.name: member.value for member in cls}
    
    @classmethod
    def get_initial_key(cls) -> Any:
        """Get the first key from the enum dictionary."""
        return next(iter(cls.to_dict().keys()))

    @classmethod
    def get_initial_value(cls) -> Any:
        """Get the first value from the enum dictionary."""
        return next(iter(cls.to_dict().values()))
    
    @classmethod
    def get_initial(cls) -> Any:
        """Alias to `get_initial_value`."""
        return cls.get_initial_value()

    @classmethod
    def get(cls, key: str, default: Any = None, mapping: Dict[str, Any] = None) -> Any:
        """
        Get the value for the given key from the optional mapping or the enum,
        return default or initial value if not found.
        
        Args:
            key (str): The key to look for.
            default (Any, optional): The default value to return if the key is not found. 
                                    If not provided, the initial enum value is used.
            mapping (Dict[str, Any], optional): An optional mapping of keys to custom values.
        
        Returns:
            Any: The value associated with the key, either from the mapping or the enum's default values.
        """
        # Use the initial value as the default if no default is provided
        if default is None:
            default_key = cls.get_initial_key()

            if mapping is not None:
                default = mapping[default_key]
            else:
                default = cls.to_dict()[default_key]
        
        # If a mapping is provided, try to get the value from it
        if mapping is not None:
            cls.validate_mapping_keys(mapping)

            return mapping.get(key, default)
        else:
            # Fallback to the enum's default values if no mapping is provided or the key is not in the mapping
            return cls.to_dict().get(key, default)
    
    @classmethod
    def keys(cls, as_list = True) -> Union[List[str], KeysView[str]]:
        """
        Return a view of the keys of the enum class as a list or as a `KeysView`.

        Parameters:
            as_list (bool, optional): If True, return keys as a list. If False, return keys as a `KeysView`.
                                      Defaults to True.

        Returns:
            Union[List[str], KeysView[str]]: A list of keys if `as_list` is True, otherwise a `KeysView` object
                                              containing the keys.

        Example:
            # Get keys as a list
            keys_list = MyEnum.keys()

            # Get keys as a `KeysView`
            keys_view = MyEnum.keys(as_list=False)
        """
        keys_view = cls.to_dict().keys()

        if as_list:
            return list(keys_view)
        else:
            return keys_view
    
    @classmethod
    def values(cls, as_list = True) -> Union[List[any], ValuesView]:
        """
        Return a view of the values of the enum class as a list or as a `ValuesView`.

        Parameters:
            as_list (bool, optional): If True, return values as a list. If False, return values as a `ValuesView`.
                                      Defaults to True.

        Returns:
            Union[List[Any], ValuesView[Any]]: A list of values if `as_list` is True, otherwise a `ValuesView` object
                                                containing the values.

        Example:
            # Get values as a list
            values_list = MyEnum.values()

            # Get values as a `ValuesView`
            values_view = MyEnum.values(as_list=False)
        """
        values_view = cls.to_dict().values()

        if as_list:
            return list(values_view)
        else:
            return values_view

    @classmethod
    def validate_mapping_keys(cls, mapping: Dict[str, Any]) -> bool:
        """Validate that every enum member has a mapping, raising a KeyError if any are missing.
        
        Args:
            mapping (Dict[str, Any]): The mapping dictionary to validate.

        Returns:
            bool: True if the mapping is valid (raises `KeyError` otherwise).

        Raises:
            KeyError: If any enum members are missing in the provided mapping.
        """
        # Check if the names of enum members are in the mapping's keys
        missing = [member.name for member in cls if member.name not in mapping]
        if missing:
            # missing now contains the names of the enum members that are not keys in the mapping
            missing_keys = ', '.join(missing)  # Joining missing member names directly
            raise KeyError(f"Missing mappings for: {missing_keys}")
        
        # Check for extra keys in the mapping
        extra_keys = [key for key in mapping if key not in {member.name for member in cls}]
        if extra_keys:
            # extra_keys now contains the extra keys found in the mapping
            extra_keys_str = ', '.join(extra_keys)  # Joining extra keys for the error message
            raise KeyError(f"Extra keys found in mapping: {extra_keys_str}")
        
        return True

    @classmethod
    def map(cls, key_mapping: Dict[Enum, Any]) -> Dict[Enum, Any]:
        """Map enum members to values using the provided dictionary.

        This mapping operation does not alter the values within the Enum itself; instead, it generates a new dictionary with the same keys and updated values.

        Internally, `validate_mapping_keys` is invoked to confirm that the keys align with the Enum members, but the value types remain arbitrary.

        Args:
            key_mapping (Dict[Enum, Any]): A dictionary mapping enum members to new values.

        Returns:
            Dict[Enum, Any]: A dictionary containing the mapped enum members with their corresponding new values.

        Raises:
            KeyError: If any enum members are missing in the provided mapping.
        """
       
        # Map enum members to values
        mapped_values = {}
        for member in cls:
            if member in key_mapping:
                mapped_values[member.name] = key_mapping[member]

        # Validate the provided key mapping contains all enum members
        cls.validate_mapping_keys(mapped_values)

        return mapped_values
