from collections import namedtuple

n = int(input())

# Read the header
columns = input().split()

# Create namedtuple dynamically
Student = namedtuple("Student", columns)

total_marks = 0

for _ in range(n):
    student = Student(*input().split())
    total_marks += int(student.MARKS)

print(total_marks / n)




"""

Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
TESTCASE 02

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00



"""