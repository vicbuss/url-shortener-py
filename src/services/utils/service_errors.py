class NotFoundError(Exception):
	"""Exception raised when a requested resource is not found."""

	def __init__(self, message: str = 'Resource not found') -> None:
		super().__init__(message)
