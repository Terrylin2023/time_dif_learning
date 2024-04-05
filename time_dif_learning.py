
numsofstate = int (input("Enter the number of states: "))
learning_rate = float(input("Enter the learning rate: "))
discount = float(input("Enter the discount: "))
elapsed_time = [0]*numsofstate
Vold = [0]*numsofstate
Vnew = [0]*numsofstate
for i in range(numsofstate):
    elapsed_time[i] = int(input(f"Enter the time {i}: "))
    Vold[i] = int(input(f"Enter the value of the old state {i}: "))
    
for j in range(numsofstate):
    if j<numsofstate-1:
        Vnew[j] = Vold[j]+ learning_rate*((elapsed_time[j+1]-elapsed_time[j])+discount*Vold[j+1]-Vold[j])
        print(f"Value of the new state {j}: ", Vnew[j])
    else:
        continue
 
