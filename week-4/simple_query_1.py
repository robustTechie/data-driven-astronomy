# Write your query function here
import numpy as np

def query(fName):
  data = np.loadtxt(fName, delimiter=',', usecols=(0, 2))
  result = []
  for star in data:
    if star[1] > 1.0:
      result.append(star)
  
  return np.array(result)



# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
