from dataclasses import dataclass
import datetime

class screening_events:
  def __str__(self):
    raise NotImplementedError

class v1(screening_events):

  @dataclass
  class screening_scheduled():
    screening_id: str
    movie_id: str
    theatre_id: str
    starts_at: datetime.datetime
    duration_in_minutes: int
    end_time: datetime.datetime

    def __str__(self):
      return f"Screening {screening_id} scheduled for {start_at}"

  @dataclass
  class screening_cancelled():
    screening_id: str
    reason: str

    def __str__(self):
      return f"Screening {screening_id} cancelled because {reason}"

  @dataclass
  class seat_reserverd():
    screening_id: str
    row: int
    seat: int

  @dataclass
  class seat_released():
    screening_id: str
    row: int
    seat: int
