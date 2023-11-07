Param(
    $current_file
)
$url = "https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat"

if ($current_file -eq "") {
    "Usage: update_iran.dat.ps1 </path/to/iran.dat>"
    Exit
}

if (Test-Path $current_file -PathType Leaf) {
    $tmpfile = New-TemporaryFile
    Start-BitsTransfer -Source "$url.sha256" -Destination $tmpfile
    $new_checksum = (Get-Content -Path $tmpfile).Substring(0, 64).ToUpper()
    if ($new_checksum -eq (Get-FileHash -Path $current_file).Hash) {
        "Domains file is already up to date."
    }
    else {
        Start-BitsTransfer -Source $url -Destination $tmpfile
        if ($new_checksum -eq (Get-FileHash -Path $tmpfile).Hash) {
            Copy-Item -Path $tmpfile -Destination $current_file
            "Domains file updated successfully."
        }
        else {
            "Domains file is invalid."
        }
    }
}
else {
    Start-BitsTransfer -Source $url -Destination $current_file
    "Domains file downloaded successfully."
}