"""Utility functions for handling VLNV strings."""


class VLNV:
    """
    Represents a VLNV (Vendor:Library:Name:Version) identifier.

    Attributes:
        vendor (str): The vendor part of the VLNV string.
        library (str): The library part of the VLNV string.
        name (str): The name part of the VLNV string.
        version (str): The version part of the VLNV string.
    """

    _original: str
    vendor: str
    library: str
    name: str
    version: str

    def __init__(
        self,
        original: str,
        vendor: str = None,
        library: str = None,
        name: str = None,
        version: str = None,
    ):
        self._original = original
        self.vendor = vendor
        self.library = library
        self.name = name
        self.version = version

    @classmethod
    def from_string(cls, vlnv: str) -> "VLNV":
        """
        Parses a VLNV string and returns a VLNV instance.
        If vendor or library are missing, sets them to None.

        Args:
            vlnv (str): The VLNV string to parse (format: vendor:library:name:version).

        Returns:
            VLNV: The parsed VLNV instance.
        """
        parts = vlnv.split(":", 3)

        original = vlnv
        vendor = None
        library = None
        name = None
        version = None

        if len(parts) == 1:
            name = parts[0]
        elif len(parts) == 2:
            name = parts[0]
            version = parts[1]
        elif len(parts) == 3:
            vendor = parts[0]
            name = parts[1]
            version = parts[2]
        else:
            vendor = parts[0]
            library = parts[1]
            name = parts[2]
            version = parts[3]

        return cls(original, vendor, library, name, version)

    def to_string(self) -> str:
        """
        Returns the VLNV as a colon-separated string.
        """
        return ":".join(
            str(part) for part in [self.vendor, self.library, self.name, self.version]
        )

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()

    def __eq__(self, other: "VLNV") -> bool:
        if not isinstance(other, VLNV):
            return False
        return (
            self.vendor == other.vendor
            and self.library == other.library
            and self.name == other.name
            and self.version == other.version
        )
