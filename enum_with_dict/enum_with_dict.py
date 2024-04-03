from enum import Enum

class EnumWithDict(Enum):
    @classmethod
    def to_dict(cls):
        """Return a dictionary representation of the enum."""
        return {member.name: member.value for member in cls}

    @classmethod
    def get_initial(cls):
        """Get the first value from the enum dictionary."""
        return next(iter(cls.to_dict().values()))

    @classmethod
    def get(cls, key, default=None):
        """Get the value for the given key or return default or initial value."""
        # If default is not provided, use the initial value
        if default is None:
            default = cls.get_initial()
        return cls.to_dict().get(key, default)
