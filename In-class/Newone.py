def create_variable(parameter):
    variables = {}
    variables[parameter] = "This is a variable created with parameter: " + str(parameter)
    return variables

parameter_value = 42
dynamic_variables = create_variable(parameter_value)

print(dynamic_variables.get(parameter_value, "Variable not found"))
