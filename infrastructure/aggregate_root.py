from typing import List
from dataclasses import dataclass, field

import domain.events

@dataclass
class aggregate_root:
  version: int = -1
  _changes: list = field(default_factory=list)

  def apply(self, event):
    if event.when():
      self._changes.append(event)

    if not event.still_valid:
      raise Exception("cannot apply")

  def clear_changes():
    self._changes.clear()

  def load(events: List[domain.events.screening_events]):
    for e in events:
      e.when()
      self.version = self.version +1
