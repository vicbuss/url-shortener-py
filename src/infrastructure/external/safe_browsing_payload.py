from dataclasses import dataclass
from typing import List


@dataclass
class Client:
	clientId: str
	clientVersion: str


@dataclass
class ThreatEntry:
	url: str


@dataclass
class ThreatInfo:
	threatTypes: List[str]
	platformTypes: List[str]
	threatEntryTypes: List[str]
	threatEntries: List[ThreatEntry]


@dataclass
class SafeBrowsingPayload:
	client: Client
	threatInfo: ThreatInfo
