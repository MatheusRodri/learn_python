# Instructions

# pow() takes three arguments: base, exp, and mod. Without mod, the function will return an error. - Incorrect
# pow() takes three required arguments: base, exp, and None. - Incorrect
# pow() requires base and exp arguments; mod is optional. - Correct
# pow() takes two arguments: exp and mod. Missing exp results in an error. - Incorrect

# Exercise

help(pow)

# Output:
# Help on built-in function pow in module builtins:
# pow(base, exp, mod=None)
#     Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

#     Some types, such as ints, are able to use a more efficient algorithm when
#     invoked using the three argument form.