def evaluate_expression(expression):
    parts = expression.split()
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Ділення на нуль!"
    else:
        return "Невідома операція!"
    
    return result

expression = "15 + 20"
print(evaluate_expression(expression))
