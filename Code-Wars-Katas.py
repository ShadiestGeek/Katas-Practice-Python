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
        
 #Check if a "Product Discount Coupon" is past a set expiration date
    def check_coupon(entered_code, correct_code, current_date, expiration_date):
        from datetime import datetime
        A = str(datetime.strptime(current_date, '%B %d, %Y'))
        B = str(datetime.strptime(expiration_date, '%B %d, %Y'))
        if isinstance(entered_code, str):
          if entered_code != correct_code:
            return False
          if entered_code == correct_code and A <= B:
            return True
        return False