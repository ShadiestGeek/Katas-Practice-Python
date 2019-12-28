#Solutions to level 8 and 7 Katas
#NOTE: Increasing levels move in Decending Order

#To Convert a Number to a String (8)
    def number_to_string(num):
    x = str(num)
    return x
    
 #Find and remove lowest veriable within a string/list, do not mutate original list (7)
    def remove_smallest(numbers):
        x = list(numbers)
        if not numbers:
            return []
        x.remove(min(x))
        return x