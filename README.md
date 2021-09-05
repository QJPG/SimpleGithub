# Simple Github Repositories Manager w. Python
<h2>Search, Create and Modify Github Reposiories</h2>

- Required REQUESTS lib and Python 3.x



<code>GithubSearchRepositories()</code> -> To search all rerpositories of GitHub

<code>Github()</code> -> To Create and Modify user Repositories
- <code>.add_token(t_str)</code> to append yours tokens
- <code>.create_repository(user, token_index, repo_data)</code>
- <code>.destroy_repository(user, token_index, repo_name)</code>
- <code>.get_user_and_notifications(user, token_index)</code> -> return list(**login_json**, **notifications_json**)
