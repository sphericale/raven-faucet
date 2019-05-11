from aiohttp import web

async def index(request):
   return web.FileResponse('./faucet.html')
   
async def claim(request):
   data = await request.post()
   claim_address = data['_address']
   return web.Response(text=f"Claimed {claim_address}")