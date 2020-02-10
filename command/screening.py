import datetime
from dataclasses import dataclass

class v1():

  @dataclass
  class schedule_screening():
    movie_id: str
    screening_id: str
    starts_at: datetime.datetime
    theater_id: str

  @dataclass
  class reserve_seat():
    screening_id: str
    row: int
    seat: int
