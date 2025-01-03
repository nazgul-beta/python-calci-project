
def validate_number(num):
    # Basic validation without proper type checking
    try:
        float(num)
        return True
    except:
        return False

def format_result(result):
    # Simple formatting without proper rounding or precision handling
    return str(result)

def parse_input(input_str):
    # Basic parsing without proper error handling
    parts = input_str.split()
    return float(parts[0]), parts[1], float(parts[2])
