
# This script fetches the repositories of a given GitHub user and updates the README.md file with a list of projects.
# It excludes forked repositories and includes the number of stars and a description for each project.

import requests

USERNAME = "GunalHincal"
README_FILE = "README.md"

def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def generate_project_list(repos):
    project_lines = []
    for repo in repos:
        if repo["fork"]:
            continue
        description = repo["description"] or "No description provided."
        stars = repo["stargazers_count"]
        line = f'- [{repo["name"]}]({repo["html_url"]}) — ⭐ {stars} | _{description}_'
        project_lines.append(line)
    return "\n".join(project_lines)

def update_readme(project_list):
    with open(README_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    start_marker = "<!-- PROJECTS:START -->"
    end_marker = "<!-- PROJECTS:END -->"

    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]
    new_section = f"{start_marker}\n{project_list}\n{end_marker}"

    updated_content = before + new_section + after

    with open(README_FILE, "w", encoding="utf-8") as file:
        file.write(updated_content)

def main():
    repos = fetch_repositories(USERNAME)
    project_list = generate_project_list(repos)
    update_readme(project_list)

if __name__ == "__main__":
    main()
