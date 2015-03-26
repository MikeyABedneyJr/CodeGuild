#GIVEN THE FOLLOWING LIST OF LIST
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

#CREATE TWO NEW LISTS ONE FOR EACH 
#STOCK TICKER SYMBOL e.g. APPL and MSFT

stocks = {}

#Loop through current entries in test_data
for index in test_data:

  #If stock is not currently in stocks dictionary, add name
  # as the key with date and stock worth as values
  if index[1] not in stocks:
    stocks.update({index[1]: [index[0], index[2]]})

  #If stock is IN stocks dictionary, add the entry
  if index[1] in stocks:
    new_values = [index[0], index[2]]
    stocks.update(new_values)

print stocks