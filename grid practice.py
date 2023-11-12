#grids are just lists of lists

#unsure:

grid = [
  ["3","3", "5", "6"],
  ["4","4", "6", "7"],
  ["5",["5", "4", "4", ["3", "4"], "7", "8"]],
  ["6","6", "7", "9"],
  ["2", "3", "3", "4"]
]

print(grid[2][-1])

#output: ['5', '4', '4', ['3', '4'], '7', '8']

grid = [
  ["3","3", "5", "6"],
  ["4","4", "6", "7"],
  ["5",["5", "4", "4", ["3", "4"], "7", "8"]],
  ["6","6", "7", "9"],
  ["2", "3", "3", "4"]
]

print(grid[2][1])

output: ['5', '4', '4', ['3', '4'], '7', '8']






#-----

#more comfortable with:

grid = [
  ["3","3", "5", "6"],
  ["4","4", "6", "7"],
  ["5","5", "7", "8"],
  ["6","6", "7", "9"],
  ["2", "3", "3", "4"]
]

print(grid[-1])

#output: ['2', '3', '3', '4']



grid = [
  ["3","3", "5", "6"],
  ["4","4", "6", "7"],
  ["5",["5", "4", "4", "3"], "7", "8"],
  ["6","6", "7", "9"],
  ["2", "3", "3", "4"]
]

print(grid[2][1][3])

#output: 3

grid = [
  ["3","3", "5", "6"],
  ["4","4", "6", "7"],
  ["5",["5", "4", "4", ["3", "4"], "7", "8"]],
  ["6","6", "7", "9"],
  ["2", "3", "3", "4"]
]

print(grid[2])

#output: ['5', ['5', '4', '4', ['3', '4'], '7', '8']]

grid = [
  ["3","3", "5", "6"],
  ["4","4", "6", "7"],
  ["5",["5", "4", "4", ["3", "4"], "7", "8"]],
  ["6","6", "7", "9"],
  ["2", "3", "3", "4"]
]

print(grid[-2][-2])

#output: 7

