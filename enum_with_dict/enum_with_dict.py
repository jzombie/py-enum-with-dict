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
  