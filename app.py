import functions

"""
    I created this app to help gather and average blood pressure. 

    This app will walk someone through taking their 
        blood pressure three times and will find the 
        average of the following: SYS, DIA, PUL. 

    All of the code lives in funcitions.py and is called from app.py.

    This was done as a way to practice importing libraries and passing 
        in variable values. 
"""

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
diagnosis = functions.reading_output(avg_bp)

functions.push_to_github()