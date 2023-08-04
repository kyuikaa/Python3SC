## Python3SC
**Push a Source Code To Github Easily using Python**

**Usage**
* To push code to a GitHub repository using Python, you'll need to use the GitHub API. One way to interact with the GitHub API is through the requests library. Before you proceed, ensure you have requests installed. You can install it using pip: 

```bash
pip install requests
```

* Now, here's a Python script to push code to a GitHub repository:

```python
import requests
import base64

def create_file_on_github(repo_owner, repo_name, file_path, commit_message, file_content, branch="main", github_token=None):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    content_bytes = file_content.encode('utf-8')
    content_base64 = base64.b64encode(content_bytes).decode('utf-8')

    data = {
        "message": commit_message,
        "content": content_base64,
        "branch": branch
    }

    response = requests.put(api_url, headers=headers, json=data)

    if response.status_code == 201:
        print("File created successfully.")
    elif response.status_code == 200:
        print("File updated successfully.")
    else:
        print(f"Error: {response.status_code} - {response.json()['message']}")

# Usage example:
if __name__ == "__main__":
    # Replace with your GitHub repository details
    repo_owner = "your_username"
    repo_name = "your_repository"
    file_path = "path/to/your/file.txt"  # Replace with the path to the file in the repository
    commit_message = "Commit message"
    file_content = "Content of your file."

    # Replace with your GitHub personal access token
    github_token = "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"

    create_file_on_github(repo_owner, repo_name, file_path, commit_message, file_content, github_token=github_token)
```

Make sure to replace `your_username`, `your_repository`, `path/to/your/file.txt`, and `YOUR_GITHUB_PERSONAL_ACCESS_TOKEN` with your GitHub username, repository name, the path to the file in the repository, and your GitHub Personal Access Token, respectively.

Remember to use a Personal Access Token with the necessary scopes to create or update files in the repository. You can create a token in your GitHub settings under "**Developer settings**" > "**Personal access tokens.**"
