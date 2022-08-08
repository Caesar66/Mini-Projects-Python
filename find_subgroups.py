import math
    
def getGroup(n):
    mdc_list = []
    for i in range(1, n):
        if math.gcd(n,i) == 1:
            mdc_list.append(i)
    return mdc_list

def getSubGroup(main_group, main_subgroup):
    subgroup = [main_subgroup]
    
    actual_number = 0
    while actual_number < len(subgroup):
        index = 0
        while index < len(subgroup):
            #print("Actual_number: {} | Index: {} | First: {} | Second: {} | Result: {}".format(actual_number, index, subgroup[actual_number], subgroup[index], (subgroup[actual_number]*subgroup[index])%main_group))
            result = (subgroup[actual_number]*subgroup[index])%main_group
            if result not in subgroup:
                subgroup.append(result)
            index += 1
        actual_number += 1   
    subgroup = list(subgroup)
    return main_subgroup, subgroup
    
def main(number):
    group = getGroup(number)
    for n in group:
        print(getSubGroup(number, n))
    return None 
    
print(main(21))
#print(getGroup(21))
#print(getSubGroup(21,4))
