import sys

# Initializing variables to track statistics
total_runners = 0
total_time = 0
fastest_time = float('inf')
fastest_runner = None
slowest_time = 0

# Reading input from the user
print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")
while True:
  line = input("> ")
  if line.upper() == "END":
    break

  # Spliting the line into the runner number and time
  parts = line.split("::")
  if len(parts) != 2:
    print("Error in data stream. Ignorning. Carry on.")
    continue

  # Trying to parse the runner number and time
  try:
    runner_number = int(parts[0])
    time = int(parts[1])
  except ValueError:
    print("Error in data stream. Ignorning. Carry on.")
    continue

  # Updating statistics
  total_runners += 1
  total_time += time
  if time < fastest_time:
    fastest_time = time
    fastest_runner = runner_number
  if time > slowest_time:
    slowest_time = time

# Calculating average time
if total_runners == 0:
  print("No data found. Nothing to do. What a pity.")
  sys.exit()
else:
  average_time = total_time // total_runners

# Converting times to minutes and seconds
def to_minutes_seconds(time):
    minutes, seconds = divmod(time, 60)
    if minutes <= 1:
        minutes_label = "minute"
    else:
        minutes_label = "minutes"
    if seconds <= 1:
        seconds_label = "second"
    else:
        seconds_label = "seconds"
    if minutes == 0:
        return f"{seconds} {seconds_label}"
    else:
        return f"{minutes} {minutes_label}, {seconds} {seconds_label}"

fastest_time = to_minutes_seconds(fastest_time)
slowest_time = to_minutes_seconds(slowest_time)
average_time = to_minutes_seconds(average_time)

# Printing results
print(f"\nTotal Runners: {total_runners}")
print(f"Average Time:  {average_time}")
print(f"Fastest Time:  {fastest_time}")
print(f"Slowest Time:  {slowest_time}")
print(f"Best Time Here: Runner #{fastest_runner}")