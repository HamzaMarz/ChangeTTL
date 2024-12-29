# TTL Modifier Using PyDivert

A Python script to intercept and modify the **TTL (Time to Live)** value of network packets using the **pydivert** library.

## Features
- Capture inbound packets with a filter rule.
- Modify TTL values and reinject packets.

## Prerequisites
1. Python 3.6+  
2. Install pydivert: `pip install pydivert`  
3. Install [WinDivert](https://reqrypt.org/windivert.html).

## Usage
1. Clone this repo:  
   ```bash
   git clone https://github.com/HamzaMarz/ChangeTTL.git
   cd ChangeTTL
