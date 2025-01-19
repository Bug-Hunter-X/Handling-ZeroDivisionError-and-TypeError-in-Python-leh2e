def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s)")
        return None

# Example usage 
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: Error: Unsupported operand type(s)

#Enhanced solution with more specific error handling and logging
import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def improved_function(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError occurred: {e}")
        return None
    except TypeError as e:
        logging.error(f"TypeError occurred: {e}")
        return None
    except Exception as e:  #Catches other potential errors
        logging.exception(f"An unexpected error occurred: {e}")
        return None