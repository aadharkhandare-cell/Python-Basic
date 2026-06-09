#Q1 Print the following paterns using for looping statement
#1   print:- 1
#            1 2
#            1 2 3 
#            1 2 3 4 
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#2 print:- 1
#          2 3
#          4 5 6
#          7 8 9 10
c=1
for i in range(1,5):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()


#3 print:- * * * *
#          * * *
#          * *
#          *
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()


#4#1 1 1 1 
  #2 2 2 
  #3 3 
  #4
for i in range(1,5):
	for j in range(5,i,-1):
		print(i,end=" ")
	print()


#5#1 2 3 4 
  #1 2 3 
  #1 2 
  #1
for i in range(5,0,-1):
	for j in range(1,i):
		print(j,end="")
	print()
    
    
#6#1
  #2 2
  #3 3 3 
  #4 4 4 4
for i in range(1,5):
	for j in range(i):
		print(i,end=" ")
	print()
    
    
#7#A
  #B B
  #C C C
  #D D D D
c=65
for i in range(1,5):
	for j in range(i):
		print(chr(c),end=" ")
	c+=1
	print()
    
    
#8  #A
    #B C
    #D E F
    #G H I J
c = 65
for i in range(1, 5):
    for j in range(i):
        print(chr(c), end=" ")
        c += 1
    print()
    
    
#9  #C C C 
    #B B 
    #A
c=67
for i in range(1,4):
	for j in range(1,5-i):
		print(chr(c),end=" ")
	c-=1
	print()
    
    
#10#     *
   #   * *
   # * * *
for i in range(1,4):
	for k in range(3-i):
		print(" ",end=" ")
	for j in range(i):
		print("*",end=" ")
	print()
    
#11#           *
#     		*  *
#	     *  *  *
#     *  *  *  *
#for n=5 
n=int(input("Enter a number : "))
for i in range(1,n):
	for k in range(n-i):
		print(" ",end=" ")
	for j in range(i):
		print("*",end=" ")
	print()
    
    
#12# * * * *
  #   * * * 
#      * * 
#       *
n=5
for i in range(1,n):
	for k in range(i):
		print(" ",end=" ")
	for j in range(n-i):
		print("*",end=" ")
	print()
    
    
#13#  		*
#		*	*	*
#  *	*	*	*	*
#* *    *   *   *   *  *
n=5
for i in range(1,n):
	for k in range(n-i):
		print(" ",end=" ")
	for j in range(2*i-1):
		print("*",end=" ")
	print()
    
#14#                     *
#                      * * *
#                    * * * * *
#                  * * * * * * *
#                    * * * * * 
#                      * * * 
#                        *
n = 4  # number of rows (top half)
for i in range(1, n + 1):
    print("  " * (n - i), end="")        # spaces
    print("* " * (2 * i - 1))            # stars
    
for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")        # spaces
    print("* " * (2 * i - 1))            # stars
    

#15#  * * * * * 
#         *
#         *
#         * 
#         *
n = 5
print("* " * n)
for i in range(n - 1):
    print("  " * (n // 2) + "*")


#16# *
#    *
#    *
#    *
#    * * * *
n=5
for i in range(n-1):
    print("*")
print("*"*n)

