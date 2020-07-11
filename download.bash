# Use the Github v4 Graphql API to fetch the latest ra releases. There are 2: nightly and the latest release weekly.

oauth_pat=$1

curl -X POST\
  'https://api.github.com/graphql'\
  -u "hybras:${oauth_pat}"\
  -H 'Content-Type: application/json; charset=utf-8'\
  -d "$(cat ./query.json)"\
  -o "./output.json"

# Output is saved to a file

apt install jq

# The proper asset url is parsed from the response
lastest_url=$(jq -r ".data.repository.releases.edges[0].node.releaseAssets.edges[0].node.downloadUrl" "./output.json")

# Download .vsix file
wget $lastest_url

