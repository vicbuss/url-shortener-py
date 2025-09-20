import bcrypt


class User:
	def __init__(
		self, username: str, password: str, role: str, hashPwd: bool = False
	) -> None:
		self.username = username
		self.role = role

		if hashPwd:
			hashed = bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
			self.password = hashed.decode()
		else:
			self.password = password

	def verify_password(self, password: str) -> bool:
		return bcrypt.checkpw(
			password=password.encode(), hashed_password=self.password.encode()
		)
