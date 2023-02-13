# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/


# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
# Example 2:

# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000


#need to  round(number, digits)

salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
salary.sort()
l=len(salary)-1
x=0
n=0
for i in range(1,l):
    x=x+salary[i]
    n=n+1

print(x/n)
print(round(x/n, 5))


# Accepted

# salary.sort()
# salary[0], salary[-1] = 0, 0
# return float((sum(salary)*1.0) / (len(salary) - 2))


