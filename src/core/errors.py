class TranspilerError(Exception):
    """Base exception for transpiler errors."""
    pass

class LanguageNotFoundError(TranspilerError):
    """Raised when a language file is not found."""
    pass

class ValidationError(TranspilerError):
    """Raised when a language file fails validation."""
    pass