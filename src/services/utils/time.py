from datetime import datetime, timedelta, timezone


class Time:
	__iso_format = '%Y-%m-%d %H:%M:%S'

	@classmethod
	def utcnow(cls) -> datetime:
		return datetime.now(timezone.utc)

	@classmethod
	def datetime_to_iso(cls, dt: datetime) -> str:
		return dt.strftime(cls.__iso_format)

	@classmethod
	def iso_to_datetime(cls, iso_str: str) -> datetime:
		return datetime.strptime(iso_str, cls.__iso_format).replace(tzinfo=timezone.utc)

	@classmethod
	def difference_is_larger_than_period(
		cls, start: datetime, end: datetime, period_in_days: float
	) -> bool:
		diff = end - start
		return diff > timedelta(days=period_in_days)
