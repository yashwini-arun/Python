from expense_module import init_file, add_expense, total_expenses

init_file()
add_expense("Food", 150)
add_expense("Travel", 300)
print("Total Expenses:", total_expenses())
