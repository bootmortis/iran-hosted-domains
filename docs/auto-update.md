# Automatically Updating the `iran.dat` File

Ensuring that you have the latest version of the `iran.dat` file is crucial for accurate filtering of Iranian domains. This section will guide you on how to set up an automated process to update the file on a regular basis.

The scripts handle the process of updating the `iran.dat` file. They check if the file already exists and compare the checksum of the existing file with the latest version available on the repository. If a new version is available, they download the updated file and replace the existing one. If the local file doesn't exist, they simply download the latest version and save it to the specified path.

?> **Note:** The script assumes that you have the necessary permissions to write to the directory where the `iran.dat` file is located. If you encounter any issues, ensure that the script has appropriate write permissions or modify the script accordingly.

It is recommended to test the script manually before setting up the cron job or SCHTASK to ensure it executes correctly.

## Linux

### Prerequisites

-   You should have `curl` and `shasum` installed on your system.

### Usage

1. Download the [update_iran_dat.sh](https://github.com/bootmortis/iran-hosted-domains/blob/main/scripts/update_iran_dat.sh) script from this repository. (if you use ash, like OpenWrt, download [update_iran_dat.ash](https://github.com/bootmortis/iran-hosted-domains/blob/main/scripts/update_iran_dat.ash)

```shell
curl -LO https://raw.githubusercontent.com/bootmortis/iran-hosted-domains/main/scripts/update_iran_dat.sh
```

2. Make the script executable by running the following command in the terminal:

```shell
chmod +x update_iran_dat.sh
```

3. Open your crontab file by running the following command:

```shell
crontab -e
```

4. In the crontab editor, add the following line to schedule the script to run every Tuesday (a day after we update `iran.dat`):

```shell
0 0 * * 2 /path/to/update_iran_dat.sh /path/to/iran.dat
```

Make sure to replace `/path/to/update_iran_dat.sh` with the actual path to the script on your system and `/path/to/iran.dat` with the actual path to the `iran.dat` file that you want to update. 5. Save the crontab file and exit the editor.

## Windows

### Prerequisites

-   Since the script is not signed, you must have the appropriate execution policy to run it.
-   This can be achieved by running the following command in a Powershell window with administrative rights:

```powershell
Set-ExecutionPolicy unrestricted
```

### Usage

1. Download the [update_iran_dat.ps1](https://github.com/bootmortis/iran-hosted-domains/blob/main/scripts/update_iran_dat.ps1) script from this repository and move it to your preferred location (next to `iran.dat` file should be good).

2. Run the Windows command prompt as Administrator and execute the following command:

```cmd
SCHTASKS /CREATE /SC WEEKLY /D TUE /TN "UPDATE IRAN.DAT" /TR "powershell -File '<path\to\update_iran_dat.ps1>' '<path\to\iran.dat>'" /ST 19:00
```

Make sure to replace `<path\to\update_iran_dat.ps1>` with the actual path to the script on your system and `<path\to\iran.dat>` with the actual path to the `iran.dat` file that you want to update.
