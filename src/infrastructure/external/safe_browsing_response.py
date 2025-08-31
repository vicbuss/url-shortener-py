from typing import List, Literal, TypedDict

ThreatType = Literal[
	'THREAT_TYPE_UNSPECIFIED',
	'MALWARE',
	'SOCIAL_ENGINEERING',
	'UNWANTED_SOFTWARE',
	'POTENTIALLY_HARMFUL_APPLICATION',
]

PlatformType = Literal[
	'PLATFORM_TYPE_UNSPECIFIED',
	'WINDOWS',
	'LINUX',
	'ANDROID',
	'OSX',
	'IOS',
	'ANY_PLATFORM',
	'ALL_PLATFORMS',
	'CHROME',
]

ThreatEntryType = Literal[
	'THREAT_ENTRY_TYPE_UNSPECIFIED',
	'URL',
	'EXECUTABLE',
]


class ThreatEntry(TypedDict, total=False):
	hash: str
	url: str
	digest: str


class MetadataEntry(TypedDict):
	key: str
	value: str


class ThreatEntryMetadata(TypedDict):
	entries: List[MetadataEntry]


class ThreatMatch(TypedDict):
	threatType: ThreatType
	platformType: PlatformType
	threatEntryType: ThreatEntryType
	threat: ThreatEntry
	threatEntryMetadata: ThreatEntryMetadata
	cacheDuration: str


class ThreatMatchesResponse(TypedDict):
	matches: List[ThreatMatch]
