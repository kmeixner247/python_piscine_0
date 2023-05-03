import time
print("Seconds since January 1, 1970:", '{:,}'.format(time.time()),
      "or", '{:.2e}'.format(time.time()), "in scientific notation")
print(time.strftime("%b %d %Y"))
