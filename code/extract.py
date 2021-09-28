import os
import json
import time
from dotenv import load_dotenv
from github import Github, RateLimitExceededException
from frictionless import Package, Resource, FrictionlessException


load_dotenv()
PAUSE = 1
RETRY = 10
QUERY = "resources filename:datapackage.json path:/"
github = Github(os.environ["GITHUB_TOKEN"], per_page=100)


# Helpers


def search_items():
    items = []
    results = github.search_code(QUERY)
    time.sleep(PAUSE)
    page_number = 0
    while True:
        try:
            page = results.get_page(page_number)
        except RateLimitExceededException:
            time.sleep(RETRY)
            continue
        time.sleep(PAUSE)
        page_number += 1
        if not page:
            break
        for result in page:
            repo = result.repository
            item = {}
            item["code"] = "-".join([repo.owner.login, repo.name])
            item["user"] = repo.owner.login
            item["repo"] = repo.name
            item["branch"] = repo.default_branch
            item["path"] = result.path
            item["stars"] = repo.stargazers_count
            item["download_url"] = result.download_url
            try:
                package = Package(json.loads(result.decoded_content))
                item["title"] = package.title
                item["description"] = package.description_text
                item["content"] = json.dumps(package.to_dict())
            except (json.JSONDecodeError, FrictionlessException):
                continue
            items.append(item)
        print(f"Found items: {len(items)}")
    return items


# General


resource = Resource(search_items())
resource.write("data/packages.raw.csv")
