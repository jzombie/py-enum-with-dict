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
    def validate_mapping(cls, mapping: Dict[Any, Any]) -> bool:
        """Validate that every enum member has a mapping, raise error if any are missing."""
        missing = [member for member in cls if member.value not in mapping]
        if missing:
            # Convert member values to strings to ensure compatibility with join
            missing_keys = ', '.join([str(member.value) for member in missing])
            raise ValueError(f"Missing mappings for: {missing_keys}")
        return True

  