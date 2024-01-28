import markdown
import requests

html1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>nishith-p-shetty</title>
    <meta name="description" content="GitHub profile README.md of Nishith P Shetty">
    <meta name="author" content="Nishith P Shetty">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" sizes="32x32" href="https://nishithpshetty.tk/icons/github.svg">
</head>
<style>
    * {
    font-family: Lato,Helvetica Neue,Helvetica,sans-serif;
}

.markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
    background-color: rgb(30, 30, 30);
    color: white;
}

a, a:visited, a:hover, a:active {
    color: #0C93E4;
}

.markdown-body blockquote {
    margin: 0;
    padding: 0 1em;
    color: #6a737d;
    border-left: 0.25em solid #dfe2e5;
}

.markdown-body code {
    padding: 0.2em 0.4em;
    margin: 0;
    font-size: 85%;
    background-color: rgba(27,31,35,0.05);
    border-radius: 3px;
}

.markdown-body pre {
    word-wrap: normal;
}
</style>

<body class="markdown-body">
"""

html2 = """
</body>
</html>"""

def fetch_readme_content(username, repository):
    url = f"https://raw.githubusercontent.com/{username}/{repository}/main/README.md"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def convert_to_html(markdown_content):
    html_content = markdown.markdown(
        markdown_content,
        extensions=['extra', 'codehilite', 'smarty']
    )
    return html_content

def main():
    # Replace 'username' and 'repository' with your GitHub username and repository name
    username = 'nishith-p-shetty'
    repository = 'nishith-p-shetty'

    readme_content = fetch_readme_content(username, repository)
    print(html1)
    if readme_content:
        html_content = convert_to_html(readme_content)
        print(html_content)
    else:
        print("Failed to fetch README content.")
    print(html2)

if __name__ == "__main__":
    main()
