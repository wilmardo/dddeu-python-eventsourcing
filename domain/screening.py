from dataclasses import dataclass
import datetime

from domain import events, movie, theater
from infrastructure import aggregate_root

@dataclass
class screening(aggregate_root.aggregate_root):
  @dataclass
  class state:
    state_id: str = ""

  screening_state: str = state()

  def schedule(screening_id: str, movie: movie, theater: theater,
                starts_at: datetime.datetime):
    if self.version >= 0:
      raise Exception

    event = events.screening_scheduled(
      screening_id=screening_id,
      movie_id=movie.id,
      theater_id=theater.id,
      duration_in_minutes=movie.duration_in_minutes,
      starts_at=starts_at
    )
    self.apply(event)

  # https://github.com/alexeyzimarev/dddeu-es-workshop/blob/master/EventSourcing/Domain/Screening.cs#L35
  # def when(events: event):
  #   if event.isinstance():

  def still_valid() -> bool:
    # Just check if state_id is defined
    return bool(screening_state.state_id)
