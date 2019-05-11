import argparse
import ravencoin
import re
from ravencoin.core import COIN

# faucet server listen host and port
listen_host = "127.0.0.1"
listen_port = 8080 

# coin daemon url
# specify as 'http://user:pass@host:port'
# or leave as None to autodetect
coin_daemon_url = None

# amount to send per claim (in sats)
claim_amount = 1000*COIN

# the base duration for limiting claims in seconds
claim_timespan = 60*60 # default 1 hour

ip_claims_per = 14 # limit claims by ip to this many per claim_timespan

claim_wait = 300 # wait time between claims in seconds (per user - enforced with address/cookie check)

recaptcha_key = "" # recaptcha3 secret key, leave blank to disable
recaptcha_threshold = 0.5 # recaptcha score threshold for bot detection

# mainnet coin name
coin_name_mainnet = "RVN"

# testnet coin name
coin_name_testnet = "tRVN"

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

if args.network == 'testnet':
   denom = coin_name_testnet
else:
   denom = coin_name_mainnet

ravencoin.SelectParams(args.network)

faucet_address = "mfXKamgjfpJzd6Wu6pWWnvpeBv7yU43T67"

print(f"Faucet config: Listen host={listen_host}:{listen_port}, debug={debug}, Claim amount={claim_amount/COIN} {denom}, IP claim limit {ip_claims_per}/{claim_timespan/(60*60)} hr, wait between claims {claim_wait}s")



