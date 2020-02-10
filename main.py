import dateutil.parser
import asyncio
import photonpump.connect

import domain.events, domain.movie, domain.reservation, domain.screening, domain.theater, domain.ticket
import command.screening
import infrastructure.aggregate_store

def main():
  # init connection
  loop = asyncio.get_event_loop()
  async with connect(loop=loop) as c:
    await c.ping()
    # init aggregate store
    store = infrastructure.aggregate_store(connection=c)

  print(command.screening.v1.schedule_screening(
    movie_id="thor",
    screening_id="123",
    starts_at=dateutil.parser.parse("1 Jan 1970"),
    theater_id="vue",
  ))

  await _app_service(

  )

def async handle()


if __name__== "__main__":
  main()
