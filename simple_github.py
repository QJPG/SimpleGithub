import requests
from requests import api
from requests.auth import HTTPBasicAuth
import json

class GithubSearchRepositories:
	def __init__(self) -> None:
		self.data = None
		self.repository_names_found = []

		self.filter_code
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

	def get_repository(self, owner: str, repo: str):
		data = requests.get("https://api.github.com/repos/{o}/{r}".format(o = owner, r = repo))
		
		print(data.status_code)
		
		if data.status_code == 200:
			data = data.json()
			return data
		pass
	



class Github:
	def __init__(self) -> None:
		self.tokens = []
		pass

	def add_token(self, token):
		self.tokens.append(token)
		pass

	def create_repository(self, user, token_index, repo_data):
		if token_index < len(self.tokens):
			return requests.post("https://api.github.com/user/repos", auth = (user, self.tokens[token_index]), data = json.dumps(repo_data)).status_code
		pass

	def destroy_repository(self, user, token_index, repo_name):
		if token_index < len(self.tokens):
			h = {'Authorization': 'token ' + self.tokens[token_index]}
			return requests.delete("https://api.github.com/repos/{}/{}".format(user, repo_name), headers = h).status_code
		pass

	def get_user_and_notifications(self, user, token_index):
		if token_index < len(self.tokens):
			user_json = requests.get("https://api.github.com/user", auth = (user, self.tokens[token_index])).json()
			not_json = requests.get("https://api.github.com/notifications", auth = (user, self.tokens[token_index])).json()
			return (user_json, not_json)
		pass

