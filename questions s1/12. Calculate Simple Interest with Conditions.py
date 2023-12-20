"""
	Write a program to print the following patterns:
	  a)
	           1
	          2, 3
	         4, 5, 6
	       7, 8, 9, 10
	    11, 12, 13, 14, 15
	  b)
	     * * * * * * * * *
	       * * * * * * *
	        * * * * * * 
              * * * *
                * *
                 *
"""


# a) Number pattern
print("\n --- Number pattern --- \n")
rows = 5
count = 1
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(i):
        print(count, end=" ")
        count += 1
    print() # for new line (\n)

# b) Asterisk pattern
print("\n --- Asterisk pattern ---\n")
rows = 9
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(0, i):
        print("*", end=" ")
    print() # for new line (\n)
    
"""
	------- output --------
    --- Number pattern ---

        1
       2 3
      4 5 6
     7 8 9 10
    11 12 13 14 15

    --- Asterisk pattern ---

    * * * * * * * * *
     * * * * * * * *
      * * * * * * *
       * * * * * *
        * * * * *
         * * * *
          * * *
           * *
            *

"""