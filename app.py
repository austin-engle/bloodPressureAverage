import functions

"""
    I created this app to help gather and average blood pressure.

    This app will walk someone through taking their blood pressure three times and will find the average of the following: SYS, DIA, PUL.

    All of the code lives in funcitions.py and is called from app.py.

    This was done as a way to practice importing libraries and passing in variable values.
"""

# Clears the console
functions.clear()

# Gets tags for reading
tags = functions.tags()

# Gathers first blood pressure reading
bp1 = functions.reading('first')

# Delays 30 seconds
functions.countdown()

# Gathers second blood pressure reading
bp2 = functions.reading('second')

# Delays 30 seconds
functions.countdown()

# Gathers third blood pressure reading
bp3 = functions.reading('third')

# Averages the 3 blood pressure reading
avg_bp = functions.avgbp(bp1, bp2, bp3)

# returns diagnoses from the calculated average blood pressure
diagnosis = functions.diagnosis_output(avg_bp)

# Write data to csv for keeping
functions.write_to_csv(avg_bp, diagnosis, tags)

# Calculate average for last 7 days
seven_day_average = functions.average_over_time(7)

# Calculate average for last 30 days
thirty_day_average = functions.average_over_time(30)

# Calculate average for last 90 days
ninty_day_average = functions.average_over_time(90)

# Calculate average for all inputs
all_time_average = functions.all_time_average()

# Save all averages calculated to a file
functions.write_averages_to_file(seven_day_average, thirty_day_average, ninty_day_average, all_time_average)

# Push all updates to GitHub
functions.push_to_github()
