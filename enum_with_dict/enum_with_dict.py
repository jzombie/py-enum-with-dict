from enum import Enum
from typing import Any, ClassVar, Dict, Type


class EnumWithDict(Enum):
    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        """Return a dictionary representation of the enum."""
        return {member.name: member.value for member in cls}

    @classmethod
    def get_initial(cls) -> Any:
        """Get the first value from the enum dictionary."""
        return next(iter(cls.to_dict().values()))

    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        """Get the value for the given key or return default or initial value."""
        # If default is not provided, use the initial value
        if default is None:
            default = cls.get_initial()
        return cls.to_dict().get(key, default)

    @classmethod
    def validate_mapping(cls, mapping: Dict[str, Any]) -> bool:
        """Validate that every enum member has a mapping, raise error if any are missing."""
        # Check if the names of enum members are in the mapping's keys
        missing = [member.name for member in cls if member.name not in mapping]
        if missing:
            # missing now contains the names of the enum members that are not keys in the mapping
            missing_keys = ', '.join(missing)  # Joining missing member names directly
            raise ValueError(f"Missing mappings for: {missing_keys}")
        
        # Check for extra keys in the mapping
        extra_keys = [key for key in mapping if key not in {member.name for member in cls}]
        if extra_keys:
            # extra_keys now contains the extra keys found in the mapping
            extra_keys_str = ', '.join(extra_keys)  # Joining extra keys for the error message
            raise ValueError(f"Extra keys found in mapping: {extra_keys_str}")
        
        return True
