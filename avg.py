n=int(input("Enter number of terms"))
total=0
Count=0
for i in range (0, n, 1):

    try:
       num =float (input (f" enter number {i+1}:"))
       total += num 
       Count +=1

    except ValueError:
      print ("Invalid input")

if Count>0:
     avg= total / Count 
     print(" The average is:",avg)