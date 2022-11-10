"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
age = float(input('Please enter your age: '))
max_heart_rate = (220 - age)
exersise_max = (max_heart_rate * 0.85)
exersise_min = (max_heart_rate * 0.65)
print(f'when you exercise to strengthen your heart, you should\nkeep your heart rate between {exersise_min:.0f} and {exersise_max:.0f} beats per minute')