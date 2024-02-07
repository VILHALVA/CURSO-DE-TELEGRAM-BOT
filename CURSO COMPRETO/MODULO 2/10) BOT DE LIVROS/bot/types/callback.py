import json


class CallbackQueryData:
	"""Um objeto representando os dados de uma callback query."""
	def __init__(self, data: str) -> None:
		self.__dict__.update(json.loads(data))