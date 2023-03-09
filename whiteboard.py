
# Create a function that given a list which represents street lights given as a parameter(l_street),
# determine if an outage has occurred.
# A street light is represented as a “T” or “F”.

# A street with a total number of “F” greater than or equal to
# 2 returns “Outage”, anything below returns “Power”

# Example Input
[ "T", "F", "F", "F" ]
#
# Example Output:
# “Outage”


# ******** OPTION 1 ********

#def lights(l_street):
 #   x = l_street.count("F")
  #  if x >= 2:
  #      return "Outage"
  #  else:
  #      return "Power"
    
# print(lights([ "T", "F", "F", "F" ]))

#******** OPTION 2 ********

# def lights(a_list):
#     effs = 0

#     for light in a_list:
#        if light == 'F':
#            effs += 1
#        if effs >= 2:
#           return "Outage"
#     return "Power"

# print(lights([ "T", "F", "F", "F" ]))

#     ******  OPTION 3  ******

def one_liner(a_list):
   return "power" if a_list.count('F') < 2 else "outage"

print(one_liner([ "T", "F", "F", "F"]))