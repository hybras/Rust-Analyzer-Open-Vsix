from requests import post, get, status_codes
from os import environ
from sys import argv

# make request

output = post(
    url='https://api.github.com/graphql',
    json={
        # read the graphql query from its own file
        "query": open("query.graphql", "r").read()
    },
    # the oauth token is passed in argv
    auth=("hybras", argv[1])
)

if output:
    json = output.json()
    asset_url = json["data"]["repository"]["releases"]["edges"][0]["node"]["releaseAssets"]["edges"][0]["node"]["downloadUrl"]
    with get(url=asset_url, stream=True) as asset:
        asset.raise_for_status()
        with open("rust-analyzer.vsix", "wb") as ext_file:
            for chunk in asset.iter_content(chunk_size=8192):
                ext_file.write(chunk)
