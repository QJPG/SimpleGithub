import requests
from requests import api
import json

class GithubSearchRepositories:
	def __init__(self) -> None:
		self.data = None
		self.repository_names_found = []
		pass

	def get_found_names(self):
		return self.repository_names_found
		pass

	def search_repository_by_name(self, name: str):
		self.data = requests.get("https://api.github.com/search/repositories", {"q": name}).json()
		
		if self.data:
			for i in range(len(self.data["items"])):
				self.repository_names_found.append([self.data["items"][i]["name"], self.data["items"][i]["private"]])

		return self.data
		pass

	def get_absolute_repository_by_name(self, name: str):
		if self.data:
			if len(self.data["items"]) > 0:
				for i in range(len(self.data["items"])):
					if self.data["items"][i]["name"] == name:
						return self.data["items"][i]
		pass
