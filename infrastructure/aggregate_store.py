import asyncio
import photonpump.connect

import infrastructure.aggregate_root


class aggregate_store():
  connection: photonpump.connect

  def load(aggregate_id: str) -> infrastructure.aggregate_root:
    if aggregate_id == None:
      raise Exception

    event = await self.connection.get_event('pony_stream', 1)
    return event



  async def save(self, c):
      result = await self.connection.publish_event('pony_stream', 'pony.jumped', body={
                  'name': 'Applejack',
                  'height_m': 0.6
              })
      print(result)
