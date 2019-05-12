from time import time
import dataset
import config

db = dataset.connect(f'sqlite:///{config.database_fn}')
claim_table = db.create_table('claims')
ip_table = db.create_table('ip_claims')

def check_ip(request_ip):
# count the claims from this ip within claim_timespan
# fail if ip_claims_per exceeded
# note multiple users may share same ip

   now = int(time())
   time_limit = now-config.claim_timespan

   if ip_table.count() == 0:
      print("ip_table empty, ip validation not active")
      return True

   try:
      query_result = db.query(f'SELECT COUNT(ip) FROM ip_claims WHERE claimtime > {time_limit}')
   except Exception as e:
      if config.debug:
         print(e)
      else:
         print("Error querying ip_claims table")
      return True

   for c in query_result:
      count_result = c   
   count_claims = count_result['COUNT(ip)']

   if config.debug:
      print(f'{count_claims} from IP {request_ip} in past {config.claim_timespan/(60*60)} hours')
      
   if count_claims > config.ip_claims_per:
      return False
   else:
      return True

def check_claims(col,key):
# check database for previous claims using address or cookie
   if config.debug: print(f"search by {col}")

   now = int(time())
   
   if col == "address":
      matches = claim_table.find(address=key,order_by='-claimtime')
   else:
      matches = claim_table.find(cookie=key,order_by='-claimtime')
      
   for match in matches:
      if config.debug:
         print(match)
      if int(match['claimtime']) > now-config.claim_wait:
         if config.debug:
            print(f"{int(match['claimtime'])} > {now} - {config.claim_wait}")
         return False
      
   return True

   
def update_claimtime(request_ip,address="",cookie=""):
   try:
      db.begin()
      ip_table.insert(dict(ip=request_ip, claimtime=int(time())),ensure=True)
      claim_table.upsert(dict(address=address, cookie=cookie, claimtime=int(time())), ['address','cookie'],ensure=True)
      db.commit()
      return True
   except Exception as e:
      if config.debug:
         print(e)
      db.rollback()
      return False
