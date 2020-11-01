# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

# Nicoles tests

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "126 * 45"]))

#print(arithmetic_arranger(["320 + 698", "3801 - 2", "45 + 43", "123 + 49", "126666 + 45"]))


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "126 - 45", "7548 - 473"]))

# Run unit tests automatically
main(module='test_module', exit=False)