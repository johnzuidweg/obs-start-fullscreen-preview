import asyncio
import simpleobsws
import time
import json

with open('config.json') as config_file:
    config = json.load(config_file)

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host=config["ip_addr"], password=config["password"], port=config["port"], loop=loop)

async def make_request():
    await ws.connect()
    
    data = {'geometry':config["geometry"], 'type':config["type"]} # For finding the appropriate (base64 encoded) geometry string, I exported the scene collection in OBS while the fullscreen projector preview was active. The resulting .json-file then contained the appropriate geometry string. Type for instance is empty, Multiview or StudioProgram
    result = await ws.call('OpenProjector', data)
  
    await ws.disconnect()

time.sleep(config["prestart_delay"]) # wait two seconds to make sure OBS has been started appropriately
loop.run_until_complete(make_request())