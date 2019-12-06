import functions

# Clears the console
functions.clear()

# Gathers first blood pressure reading
bp1 = functions.reading('first')

# Delays 30 seconds
functions.countdown()

# Gathers second blood pressure reading
bp2 = functions.reading('second')

# Deplays 30 seconds
functions.countdown()

# Gathers third blood pressure reading
bp3 = functions.reading('third')

# Averages the 3 blood pressure reading
avg_bp = functions.avgbp(bp1, bp2, bp3)

# returns diagnoses from the calculated average blood pressure
functions.reading_output(avg_bp)
