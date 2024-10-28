# data - list or dataset i want to paginate
# current page number i want to access
# page_size - number of items i want to display on each page
data = [1, 2, 3, ..., 100] #list of 100 items
def paginate(data, page, page_size):
    # Calculate the start and end indices for the slice
    start = (page - 1) * page_size # to avoid a 0 offset and shift starting position to the appropriate spot based on the page size 
    end = start + page_size # to get endpoint of the page slice

    # return slice of data for the currrent page
    return data[start:end] 

"""returns the first 10 items"""
page_data = paginate(data, page=1, page_size=10) # gives start = 10
print(page_data)

"""returns items from index 40 to 50 (page 5 items [41, 42, ..., 50])"""
page_date = paginate(data, page=5, page_size=10)
print(page_data)

"""returns items from index 10 to 20[start=10, end=20]"""
page_data = paginate(data, page=2, page_size=10)
print(page_data)
# end - is the index up to (but not including) the last item on the current page