# v2rayNG

You can find v2rayNG client for Android from [here](https://github.com/2dust/v2rayNG).

## Routing

> Make sure you have the latest version of v2rayNG installed.

1. Open the menu and go to `Geo asset files`.
2. From top right corner, click on the `+` icon and choose `Add URL`.
3. Add the following and press `🗸` from the top.
    - **remarks**: `iran.dat`
    - **URL**: `https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat`
4. Click on the cloud download icon on top right corner and wait for the download to finish.
5. Go back to the main menu and go to `settings`.
6. Go to the `Custom rules` section in `Settings`.
7. Write the following rules in each tab and press `✓` from the top right corner to save:

-   **Proxy URL OR IP**: `ext:iran.dat:proxy`
-   **DIRECT URL OR IP**: `ext:iran.dat:all,geoip:ir`
-   **BLOCKED URL OR IP**: `ext:iran.dat:ads,geosite:category-ads-all`

8. Hit back, and reconnect.
