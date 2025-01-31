from enum import Enum
from datetime import datetime, timedelta
import re
from typing import Optional, Dict, List


class EventType(Enum):
  FALL_ASLEEP = 1
  BEGIN_SHIFT = 2
  WAKE_UP = 3


class GuardEvent:
  timestamp: datetime
  event_type: EventType
  guard_no: Optional[int]

  def __str__(self):
    return f"{str(self.timestamp)}: {str(self.event_type)} {str(self.guard_no)}"


def parse_file(filename: str):

  def parse_event(line: str) -> GuardEvent:
    event = GuardEvent()

    if "begins shift" in line:
      event.event_type = EventType.BEGIN_SHIFT
      match = re.findall(r"Guard #(\d+)", line)[0]
      if match:
        event.guard_no = int(match)
    elif "falls asleep" in line:
      event.event_type = EventType.FALL_ASLEEP
    elif "wakes up" in line:
      event.event_type = EventType.WAKE_UP

    matches = re.findall(r"^\[(\d+-\d+-\d+ \d+:\d+)]", line)
    event.timestamp = datetime.strptime(matches[0], "%Y-%m-%d %H:%M")

    return event

  # ^\[\d+-\d+-\d+ \d+:\d+
  #^\[(\d+)-(\d+)-(\d+) (\d+):(\d+)]
  # Guard #(\d+)
  h = open(filename, "r")
  lines = h.readlines()
  h.close()

  guard_events = [parse_event(line) for line in lines]
  guard_events = sorted(guard_events, key=lambda guard: guard.timestamp)

  timestamps = {}
  for event in guard_events:
    timestamps[event.timestamp] = timestamps.get(event.timestamp, 0) + 1

  current_guard_id = None
  for guard_event in guard_events:
    if guard_event.event_type == EventType.BEGIN_SHIFT:
      current_guard_id = guard_event.guard_no
    else:
      guard_event.guard_no = current_guard_id

  return guard_events


def part1(events: List[GuardEvent]):
  guards = {}

  last_sleep_time = datetime(1500, 1, 1)
  for event in events:
    if event.event_type == EventType.FALL_ASLEEP:
      last_sleep_time = event.timestamp
    elif event.event_type == EventType.WAKE_UP:
      if event.guard_no not in guards:
        guards[event.guard_no] = {}

      # beginning_minute = last_sleep_time.minute
      time_elapsed = event.timestamp - last_sleep_time
      time_elapsed_int: int = int(time_elapsed.total_seconds() // 60)

      for i in range(0, time_elapsed_int + 1):
        time_elapsed_minute = (last_sleep_time + timedelta(minutes=i)).minute
        guards[
            event.guard_no][time_elapsed_minute] = guards[event.guard_no].get(
                time_elapsed_minute, 0) + 1

  # for (guard, sleep_times) in guards.items():
  #   print(f"""{guard}: {sum(sleep_times.values())} {str(sleep_times)}""")

  most_sleepy_guard = max(guards, key=lambda key: sum(guards[key].values()))
  most_sleepy_minute = max(
      guards[most_sleepy_guard],
      key=lambda minute: guards[most_sleepy_guard][minute])
  return (most_sleepy_minute * most_sleepy_guard)


def part2(fuck):
  return None


tests = {"example.txt": [240, None]}
