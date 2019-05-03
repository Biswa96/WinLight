#! /bin/bash

# Set environment variables
set -e
HttpHeader="Accept-Language:en-US,en;q=0.9"
ImageUrl="https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData"
JsonFile="cache.json"
JsonUrl="https://arc.msn.com/v3/Delivery/Placement?&pid=338387&fmt=json&cdm=1&ctry=US"
SearchPattern="(?<=imageFileData/).*?(?=\?ver)"
UserAgent="WindowsShellClient/9.0.40929.0 (Windows)"

# Download JSON file
wget \
--no-check-certificate \
--no-hsts \
--no-verbose \
--header $HttpHeader \
--user-agent="$UserAgent" \
$JsonUrl \
--output-document=$JsonFile

# Remove back slashes
sed --in-place 's/\\//g' $JsonFile

# Remove opening quotes
sed --in-place 's/\"{/{/g' $JsonFile

# Remove closing quotes
sed --in-place 's/}\"/}/g' $JsonFile

# Get the hashes from links and download
grep --only-matching --perl-regexp $SearchPattern $JsonFile | while read -r hash
do
    wget \
    --no-check-certificate \
    --no-hsts \
    --no-verbose \
    --continue \
    --header $HttpHeader \
    --user-agent="$UserAgent" \
    $ImageUrl/$hash \
    --output-document=$hash.jpg
done

# Delete files less that 2 KB which are blank
find . -name "*.jpg" -size -2k -delete
