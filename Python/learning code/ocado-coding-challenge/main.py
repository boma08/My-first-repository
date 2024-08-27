# # Task 1
# print("******** Start of task 1 ********")
#
# days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# day = input("Enter a day of the week: ").title()
# try:
#     index = days_of_week.index(day)
# except ValueError:
#     while day not in days_of_week:
#         print("Please ensure to enter only the first 3 characters of a day of the week")
#         day = input("Enter a day of the week: ").title()
#
# else:
#     num_of_days_later = int(input("Enter the number of days apart from 0 - 500: "))
#
# def solution(S, K):
#     mod_day = K % 7
#     day_output = days_of_week.index(S) + mod_day
#     day_index = day_output % 7
#     new_day = days_of_week[day_index]
#     return new_day
#
# print(solution(day, num_of_days_later))

# ********ALTERNATE SOLUTION********
#def day_after_k_days(s, k):
    # Define the days of the week in a cyclic manner
#    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Find the index of the given day in the days_of_week list
#    current_day_index = days_of_week.index(s)

    # Calculate the index of the resulting day after adding k days
#    resulting_day_index = (current_day_index + k) % 7

    # Return the resulting day
#    return days_of_week[resulting_day_index]
#print("\n******** End of task 1 ********\n")

print("\n******** start of task 2 ********")
def min_num (*args):
    min_numb = min(args) + 1
    while min_numb in args:
        min_numb += 1
    print(f"\nSmallest number not in list is {min_numb}")



min_num(5, 4, 3, 36, 7, 11, 9, 12, 30, 21, 7)





