# Raven-Faucet   
Cryptocurrency faucet written in Python/JS  
Developed for Ravencoin, but should work with any Bitcoin based coin with some modification  

Bot protection features:  
reCAPTCHA v3  
Limit claims by address/cookie  
Limit claims by IP  

A determined human could still bypass these, however. Therefore mostly suitable for testnet or low value payouts.  

**Installation**  
Prerequisites:  

Python libs:  
python-ravencoinlib, dataset, requests, aiohttp  

Requires Python 3.6+  
Earlier versions may work if you replace all the f-strings with the older .format()  

**Configuration**  
Edit config.py to taste  
Coin daemon must be running with RPC server enabled (server=1 in raven.conf)  

For reCAPTCHAv3:  
recaptcha_key in config.py is your secret key  
recaptcha_site_key is your site key  
leave blank to disable  

**Running**  
By default serves pages at 127.0.0.1:8086  
Can run as standalone server, but this is not recommended  
For security use a reverse proxy (e.g. nginx)  
