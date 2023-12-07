#!/bin/ash

url="https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat"
current_file="$1"

if [ -z "$current_file" ]; then
    echo "Usage: $0 </path/to/iran.dat>"
    exit 1
fi

if [ -f "$current_file" ]; then
    new_checksum=$(curl -L "$url.sha256" | cut -d " " -f 1)
    current_checksum=$(sha256sum "$current_file" | cut -d " " -f 1)

    # Compare the two checksums
    if [ "$new_checksum" != "$current_checksum" ]; then
        curl -L "$url" -o "$current_file.temp"
        # Replace the current file with the new file only if the new one is valid
        if [ "$(sha256sum "$current_file.temp" | cut -d " " -f 1)" == "$new_checksum" ]; then
            mv "$current_file.temp" "$current_file"
            echo "Domains file updated successfully."
        else
            rm "$current_file.temp"
            echo "Domains file is invalid."
        fi
    else
        echo "Domains file is already up to date."
    fi
else
    curl -L "$url" -o "$current_file"
    echo "Domains file downloaded successfully."
fi
