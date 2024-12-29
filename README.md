**TTL Modifier Using PyDivert**
This repository contains a Python script to intercept and modify the TTL (Time to Live) value of network packets. The script utilizes the pydivert library and is specifically designed to run on Windows with WinDivert installed.

Features
Intercept inbound network packets based on a filter rule.
Modify the TTL value of packets.
Reinject modified packets into the network seamlessly.
Prerequisites
Python 3.6+
pydivert library
Install it via pip:
bash
Copy code
pip install pydivert
WinDivert
Download and install WinDivert from official website.
How It Works
The script uses a filter rule to capture packets and changes their TTL value to a specified target. The modified packets are then reinjected into the network.

Usage
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/ttl-modifier.git
cd ttl-modifier
Update the filter rule and target TTL in the script or read them from an external file.

Run the script:

bash
Copy code
python ttl_modifier.py
Configuration Example
To customize the filter rule and TTL, you can edit the FILTER_RULE and TARGET_TTL variables in the script, or use an external configuration file.

Example filter rule:

python
Copy code
FILTER_RULE = "inbound && ip.TTL == 1"
TARGET_TTL = 32
Disclaimer
This script is intended for educational and research purposes only. Ensure compliance with network policies and laws before using it.

License
This project is licensed under the MIT License. See the LICENSE file for details.
