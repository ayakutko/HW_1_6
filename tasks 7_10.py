#7
date_us = "05.17.2016"
def date_eu(date_us):
    day = date_us[3:6]
    month = date_us[:3]
    year = date_us[6:10]
    return day + month + year
print(date_eu(date_us))
#8
string1 = "love"
string2 = "python"
def task8(s1, s2):
    half_length1 = int(len(s1)/2)
    half_length2 = int(len(s2)/2)
    first_result = s2[:half_length2] + s1 + s2[half_length2:]
    final_result = s1[:half_length1] + first_result + s1[half_length1:]
    return final_result
print(task8(string1, string2))
#9
s = "abc def ghj"
def second_word(string):
    list = string.split()
    list[1] = list[1].upper()
    return ' '.join(list)
print(second_word(s))
#10
s = "Leo Tolstoy*1828-08-28*1910-11-20"
length = len(s)
death_date = s[length - 10:length]
birth_date = s[length - 21:length - 11]
name = s[0: length - 22]
result_task = int(death_date[0:4]) - int(birth_date[0:4])
print(name, ",", result_task)