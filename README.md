Cryptocurrency faucet written in Python/JS
Developed for Ravencoin, but should work with any Bitcoin based coin with some modification

Bot protection features:
reCAPTCHA v3
Limit claims by address/cookie
Limit claims by IP

A determined human could still bypass these, however. Therefore mostly suitable for testnet or low value payouts.


Prerequisites:

Python libs: 
python-ravencoinlib, dataset, requests, aiohttp, aiohttp_remotes

Requires Python 3.6+
Earlier versions may work if you replace all the f-strings with the older .format()

