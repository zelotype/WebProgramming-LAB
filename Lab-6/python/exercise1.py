#############################
#### FUNCTION EXERCISES #####
#############################

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# ใช้ indexing เพื่อ print out ให้ได้ผลดังต่อไปนี้:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[4:])
# Bonus: ลองใช้ index จากท้าย
print(s[-2:])

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# จงแก้ค่า hello เป็น goodbye
l[2][2] = 'goodbye'

###############
## Problem 3 ##
###############

# จง print out ค่า hello ออกมาจาก dicitionry ด้านล่าง:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
#####################
## -- PROBLEM 4 -- ##
#####################

# เขียนฟังก์ชั่นที่รับ list ของเลข integer โดยจะ return True ถ้ามี list ของเลข 1, 2, 3 อยู่ใน list ที่รับเข้ามา

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    # CODE GOES HERE
    # check_1 = False
    # check_2 = False
    # check_3 = False
    # for i in nums:
    #   if i == 1:
    #     check_1 = True
    #   elif i == 2:
    #     check_2 = True
    #   elif i == 3:
    #     check_3 = True
    # if check_1 and check_2 and check_3:
    #   return True
    # else:
    #   return False

    for index in range(0, len(nums)-2):
      if nums[index] == 1 and nums[index+1] == 2 and nums[index+2]:
        return True
    return False

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))
#####################
## -- PROBLEM 5 -- ##
#####################

# เขียนฟังก์ชั่นที่รับ string เข้ามา แล้ว return string ที่แสดงตัวอักษร ตัว-เว้น-ตัว จาก string ที่รับเข้ามา

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  # CODE GOES HERE
  return str[::2]
print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))
#####################
## -- PROBLEM 6 -- ##
#####################

# จง return จำนวนเลขคู่ ใน list ที่ส่งเข้ามาในฟังก์ชั่น
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(*args):
  # CODE GOES HERE
  count = 0
  for i in args:
    if i%2 == 0:
      count += 1
  return count
print(count_evens(2, 1, 2, 3, 4))
print(count_evens(2, 2, 0))
print(count_evens(1, 3, 5))

