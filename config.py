import argparse
import ravencoin
import re
from ravencoin.core import COIN

# faucet server listen host and port
listen_host = "127.0.0.1"
listen_port = 8086

# coin daemon url
# specify as 'http://user:pass@host:port'
# or leave as None to autodetect
coin_daemon_url = None

# amount to send per claim (in sats)
claim_amount = 1000*COIN

# the base duration for limiting claims in seconds
claim_timespan = 60*60 # default 1 hour

ip_claims_per = 14 # limit claims by ip to this many per claim_timespan

x_real_ip = True # use cloudflare X-Real-IP header for IP

claim_wait = 300 # wait time between claims in seconds (per user - enforced with address/cookie check)

recaptcha_key = "" # recaptcha3 secret key, leave blank to disable
recaptcha_site_key = "" # public site key
recaptcha_threshold = 0.5 # recaptcha score threshold for bot detection

static_files_max_age = 86400 # maximum amount of time (in seconds) a client should cache static files (index.html, faucet.js)

coin_info = {

   'testnet': {
      'name': 'Ravencoin Testnet',
      'ticker': 'tRVN',
      'address': 'ms8T9r69qqdtxmotDioLVgeV9GH4XQgDEi'
   },

   'mainnet': {
      'name': 'Ravencoin',
      'ticker': 'RVN',
      'address': 'R9TehGensN1CNkAXZbVgtYzPovE3FXC1Qu'
   }

}

# database used to track claims
database_fn = "./faucet.db"

# maximum address length in requests (sanity check / DoS)
maxAddressLen = 50

cookie_name = 'faucet' # name of cookie used to identify user
cookie_regex = "[0-9a-z]{32}" # regular expression used to validate cookie
cookie_re = re.compile(cookie_regex)

parser = argparse.ArgumentParser(description='Ravencoin faucet server backend')
parser.add_argument("--datadir", help="Path to Raven config directory")
parser.add_argument("--network",default="testnet",choices=['testnet', 'mainnet'])
parser.add_argument("--debug",help="Enable debug output",action='store_true')
args=parser.parse_args()

debug = args.debug

coin_name = coin_info[args.network]['name']
denom = coin_info[args.network]['ticker']
faucet_address = coin_info[args.network]['address']

ravencoin.SelectParams(args.network)

print(f"Faucet config: Listen host={listen_host}:{listen_port}, debug={debug}, Claim amount={claim_amount/COIN} {denom}, IP claim limit {ip_claims_per}/{claim_timespan/(60*60)} hr, wait between claims {claim_wait}s")



