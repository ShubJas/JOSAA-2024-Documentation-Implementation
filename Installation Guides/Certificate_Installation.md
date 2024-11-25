# Installation and Configuration Guide for NIC VPN Client on Windows

This guide provides step-by-step instructions for installing and configuring the NIC VPN client on Windows 8 and Windows 10. For more details, refer to the official [Manual for Configuring VPN Client in Windows 8 & 10](https://vpn.nic.in/resources/manuals/Manual%20for%20Configuring%20VPN%20Client%20in%20Windows%208%20&%2010.pdf).

---

## Step 1: Prerequisites

1. Ensure you have the following:
   - A valid VPN username and password provided by NIC.
   - The VPN server address.
   - Administrative privileges on your computer.

2. Ensure your system is connected to the internet.

---

## Step 2: Install NIC VPN Client

1. Download the NIC VPN Client from the official VPN portal:
   - Visit [NIC VPN Resources](https://vpn.nic.in/resources/).
   - Select the appropriate VPN client version for your operating system.

2. Run the downloaded installer:
   - Double-click the installer file.
   - Follow the on-screen instructions to complete the installation.

---

## Step 3: Configure the VPN Connection

### 3.1 Open the VPN Settings

1. Press `Win + I` to open **Settings**.
2. Navigate to **Network & Internet** → **VPN**.

### 3.2 Add a VPN Connection

1. Click on **Add a VPN connection**.
2. Fill in the following details:
   - **VPN Provider**: Select **Windows (built-in)**.
   - **Connection Name**: Enter a name (e.g., NIC VPN).
   - **Server Name or Address**: Enter the VPN server address provided by NIC.
   - **VPN Type**: Select **L2TP/IPSec with pre-shared key**.
   - **Pre-shared Key**: Enter the key provided by NIC.
   - **Type of Sign-in Info**: Select **Username and Password**.

3. Click **Save**.

---

## Step 4: Connect to the VPN

1. In the VPN settings window, select the newly created connection (e.g., NIC VPN).
2. Click **Connect**.
3. Enter your username and password provided by NIC.
4. Click **OK** to establish the connection.

---

## Step 5: Verify the VPN Connection

1. Once connected, verify the VPN status:
   - Open **Network & Internet Settings** → **VPN**.
   - Ensure the connection status shows as **Connected**.

2. Check your IP address to confirm that your traffic is routed through the VPN:
   - Visit an IP address checking website (e.g., [WhatIsMyIP](https://whatismyipaddress.com/)).
   - The displayed IP should match the NIC-provided IP range.

---

## Troubleshooting

1. **Connection Fails**:
   - Double-check the server address and pre-shared key.
   - Verify your username and password.

2. **Authentication Errors**:
   - Ensure the username and password are correct.
   - Contact NIC support if credentials are not working.

3. **VPN Not Listed in Network Settings**:
   - Restart your system and check again.
   - Reinstall the NIC VPN client.

4. **Firewall Issues**:
   - Ensure your firewall or antivirus is not blocking VPN traffic.
   - Allow the VPN client through the firewall:
     - Open **Control Panel** → **System and Security** → **Windows Defender Firewall** → **Allow an app or feature through Windows Defender Firewall**.
     - Add the NIC VPN client to the list of allowed apps.

---

## Notes

- Ensure your VPN credentials are kept secure and not shared with unauthorized users.
- Disconnect from the VPN when not in use to conserve bandwidth and resources.

For further assistance, contact the NIC support team or refer to the official [VPN Resources](https://vpn.nic.in/resources/).

---
