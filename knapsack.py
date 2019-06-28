v_list = input("enter a list of values(Please provide space between valuse) : ")
w_list = input("enter a list of weights (Please provide space between valuse): ")
W = int(input("Enter the Maximum weight :"))
import sys
def convertToList(string):
    string = string.split(" ")
    temp = [int(i) for i in string] 
    return temp
if len(v_list) == len(w_list):
    v_lis = convertToList(v_list)
    w_lis = convertToList(w_list)
else: 
    sys.exit("Enter the same Number of valuse and weights!!!!")
    
inti_w,inti_v = 0,0
used_w,used_v = [],[]
while inti_w <W:
    temp_v,indx = max(v_lis),v_list.index(max(v_lis))
    temp_w = w_lis[indx]
    used_v.append(temp_v)
    used_w.append(temp_w)

    inti_v = inti_v + temp_v
    inti_w = inti_w + temp_w

    v_list.remove(temp_v)
    w_list.remove(temp_w)
    print(v_list, w_list)
print("The Total weight is" + str(inti_w) + "and Max value is " + str(inti_v) + "for the Knapsack")
print("The List of Used values is :", used_v)
print("The List of Used weights is :", used_w)

















 



