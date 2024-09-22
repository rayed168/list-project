def square_between_ranges(start,end):
    squares_list=[i**2 for i in range(start,end+1)]
    return squares_list
start_range=int(input("Enter the start of the range : "))
end_range=int(input("Enter the end of the range : "))
squares=square_between_ranges(start_range,end_range)
print("Squares of numbers between",start_range,"and",end_range,"is : ",squares )