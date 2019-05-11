import requests
from config import cookie_re,faucet_address,recaptcha_key,debug,recaptcha_threshold
from ravencoin.wallet import CRavencoinAddress

def validate_recaptcha(key):
   if recaptcha_key == "":
      return True

   r = requests.post("https://www.google.com/recaptcha/api/siteverify", data={'secret':recaptcha_key,'response':key})
   if debug:
      print(r.json())
      
   if r.json().get('action') != "claim": return False # verify action name matches JS
   if not r.json().get('success'): return False
   
   score = float(r.json().get('score'))

   return(score >= recaptcha_threshold) # decline as bot claim if score < threshold
   
def validate_address(addr):
   try:
      CRavencoinAddress(addr)
      result = True
   except Exception:
      result = False
   return result
   
def validate_cookie(cookie):
   return cookie_re.match(cookie)
   
if not validate_address(faucet_address):
   print(f"Warning: Faucet address {faucet_address} is invalid")
