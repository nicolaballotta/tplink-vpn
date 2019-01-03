# TPLink VPN

This is a simple script I created to enable/disable L2TP VPN connection from command line on TPLink AC1200 Wireless 
router.

Unfortunately on this router firmware there's no CLI and the web UI is full of JS/Ajax stuff. For that reason, after 
trying with Mechanize/Beautifulsoup, I ended up using Selenium. And I've to say it works pretty well.

## Usage
Install requirements:
```
pip install -r requirements.txt
```
and then run
```
python tplink-vpn.py -on -u username -p 'password'
```
to enable L2TP VPN, or
```
python tplink-vpn.py -off -u username -p 'password'
```
to disable the VPN.