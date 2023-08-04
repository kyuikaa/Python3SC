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