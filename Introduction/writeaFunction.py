def is_leap(year):
    leap = False
    c = True
    
    # Write your logic here
    if year % 100 != 0 and year % 4 == 0:
    	return c
    elif year % 100 == 0 and year % 400 == 0:
    	return c
    else:
    	return leap

year = int(input())
print(is_leap(year))