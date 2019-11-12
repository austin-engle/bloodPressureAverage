import functions

functions.clear() # Clears the console

bp1 = functions.reading('first') # Gathers first blood pressure reading

functions.countdown() # Delays 30 seconds

bp2 = functions.reading('second') # Gathers second blood pressure reading

functions.countdown() # Deplays 30 seconds

bp3 = functions.reading('third') # Gathers third blood pressure reading

AVG_BP = functions.avgBp(bp1, bp2, bp3) # Averages the 3 blood pressure reading

functions.readingOutput(AVG_BP) # returns diagnoses from the calculated average blood pressure