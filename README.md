# Prerequisites & Setup

    Create a Virtual Environment: Set up and activate a Python virtual environment.

    Install Python Dependencies: Navigate to the scripts directory and install the required packages.

```Bash
pip install -r requirements.txt
```

Install Aircrack-ng:  The Wi-Fi scanning script requires airmon-ng. This tool comes pre-installed on Kali Linux. For other Debian-based systems, install it via your package manager:


    sudo apt install aircrack-ng

## How to Run the Scripts
**wifi_scanner.py**

    Disclaimer: This script is designed specifically for Linux-based machines.

Step 1: Identify your Network Interface Run the following command in your terminal to find your wireless interface name (it will look something like wlp0s20f3):

```
ifconfig
```
Step 2: Enable Monitor Mode Execute the following commands to put your network card into monitor mode. Be sure to replace wlp0s20f3 with your actual interface name if it differs:
```
sudo airmon-ng check kill
sudo ip link set wlp0s20f3 up
sudo airmon-ng start wlp0s20f3 
```
**Note: Depending on your system, starting airmon-ng may append a mon suffix to your interface name (e.g., wlp0s20f3mon).**

Step 3: Open a separate terminal window, navigate to the directory where wifi_scanner.py is located, and run the script as root user:

```
sudo $(which python) wifi_scanner.py <- if executing from a virtual environment
sudo wifi_scanner.py <- not in a virtual environment
```
**port_scanner.py**

To run the port scanner, simply navigate to the script's directory and execute it using this command:

```
python3 port_scanner.py
```

**ensemble.py**

This script is a combination of the two scripts above. Hence the name 'ensemble'. 
To run this script use the following command.

```
sudo $(which python) ensemble.py <- if executing from a virtual environment
sudo ensemble.py <- not in a virtual environment
```
