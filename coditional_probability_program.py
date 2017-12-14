#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:58:11 2017

"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:24:45 2017

"""

import math

def outlier(file_path):
#    file_name = open(file_path)
#    elems = file_name.readlines()
#    elems_useful = elems[1:]
#    file_write = open("Address of the csv file",'w')
#    val = 0
    total_fraud_prob = float(923)/15420
    
    file_name = open(file_path,'r')
    elems = file_name.readline()
    elems = elems.split(',')
    
    if elems[25] == 'No':
        weight_police_report = 0.6 #to be determined
        probab_police_report = (weight_police_report * total_fraud_prob)/0.9722
    else:
        weight_police_report = 0.4
        probab_police_report = (weight_police_report * total_fraud_prob)/(0.0277)

    
    
    
    
    if elems[26] == 'No':
        weight_witness_present = 0.6#to be determined
        probab_witness_present = (weight_witness_present * total_fraud_prob)/0.9943
    else:
        weight_witness_present = 0.4
        probab_witness_present = (weight_witness_present * total_fraud_prob)/0.0056
    
    if int(elems[10])<18:
        weight_age = 0.1369 #to be determined
        probab_age = (weight_age*total_fraud_prob)/0.0217
    elif int(elems[10])<=20:
        weight_age = 0.1917
        probab_age = (weight_age*total_fraud_prob)/0.0070
    elif int(elems[10])<=25:
        weight_age = 0.2054
        probab_age = (weight_age*total_fraud_prob)/0.0397
    elif int(elems[10])<=30:
        weight_age = 0.0684
        probab_age = (weight_age*total_fraud_prob)/0.1804
    elif int(elems[10])<=35:
        weight_age = 0.0958
        probab_age = (weight_age*total_fraud_prob)/0.1822
    elif int(elems[10])<=40:
        weight_age = 0.0821
        probab_age = (weight_age*total_fraud_prob)/0.1308
    elif int(elems[10])<=50:
        weight_age = 0.0682
        probab_age = (weight_age*total_fraud_prob)/0.2253
    elif int(elems[10])<=65:
        weight_age = 0.0684
        probab_age = (weight_age*total_fraud_prob)/0.1796
    else:
        weight_age = 0.0821
        probab_age = (weight_age*total_fraud_prob)/0.0329
        
    
    if elems[11] == 'Policy Holder':
        weight_fault = 0.8823
        probab_fault = (weight_fault*total_fraud_prob)/0.7282
    else:
        weight_fault= 0.1176
        probab_fault = (weight_fault*total_fraud_prob)/0.2717
        
    if elems[13] == 'Sedan':
        weight_Vedhicle_category = 0.3636#to_be_determined
        probab_VC = (weight_Vedhicle_category*total_fraud_prob)/0.6271
    elif elems[13] == 'Utility':
        weight_Vedhicle_category = 0.0909#to_be_determined
        probab_VC = (weight_Vedhicle_category*total_fraud_prob)/0.3474
    else:
        weight_Vedhicle_category = 0.5454#to_be_determined
        probab_VC = (weight_Vedhicle_category*total_fraud_prob)/0.0253
        
    if elems[32] == "All perils":
        weight_BasePolicy = 0.5555
        probab_BP = (weight_BasePolicy*total_fraud_prob)/0.2885
    elif elems[32] == "Collision":
        weight_BasePolicy = 0.3888
        probab_BP = (weight_BasePolicy*total_fraud_prob)/0.3866
    else:
        weight_BasePolicy = 0.0555
        probab_BP = (weight_BasePolicy*total_fraud_prob)/0.3248
        
    if elems[30] == "1 vehicle":
        weight_number_Of_Cars = 0.2553
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.9284
    elif elems[30] == "2 vehicle":
        weight_number_Of_Cars = 0.2553
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.0459
    elif elems[30] == "3 to 4":
        weight_number_Of_Cars = 0.3191
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.0241
    else:
        weight_number_Of_Cars = 0.1702
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.0014
        
    if elems[14] == 'less than 20000':
        weight_vehiclePrice = 0.2567
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.0710
    elif elems[14] == '20000 to 29000':
        weight_vehiclePrice = 0.1351
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.5239
    elif elems[14] == '30000 to 39000':
        weight_vehiclePrice = 0.1216
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.2291
    elif elems[14] == '40000 to 59000':
        weight_vehiclePrice = 0.1756
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.0298
    elif elems[14] == '60000 to 69000':
        weight_vehiclePrice = 0.1081
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.0056
    else:
        weight_vehiclePrice = 0.2027
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.1403
        
    if elems[22] == 'none':
        weight_PastnumberOfClaims = 0.3333
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.2822
    elif elems[22] == '1':
        weight_PastnumberOfClaims = 0.2666
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.2317
    elif elems[22] == '2 to 4':
        weight_PastnumberOfClaims = 0.2222
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.3557
    elif elems[22] == 'more than 4':
        weight_PastnumberOfClaims = 0.1777
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.1303
    
    if elems[8] == 'Male':
        weight_Sex = 0.60
        probab_sex = (weight_Sex*total_fraud_prob)/0.8430
    elif elems[8] == 'Female':
        weight_Sex = 0.40
        probab_sex = (weight_Sex*total_fraud_prob)/0.1569
        
    if elems[9] == 'Divorced':
        weight_Marital_Status = 0.16
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.0049
    elif elems[9] == 'Married':    
        weight_Marital_Status = 0.26
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.6890
    elif elems[9] == 'Single':    
        weight_Marital_Status = 0.26
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.3037
    elif elems[9] == 'Widow':    
        weight_Marital_Status = 0.32
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.0022
        
    if elems[12] == "Sedan - All Perils":
        weight_PolicyType = 0.1754
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.2650
    elif elems[12] == "Sedan - Collision":
        weight_PolicyType = 0.1228
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.3621
    elif elems[12] == "Sedan - Liability":
        weight_PolicyType = 0.0175
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.3234
    elif elems[12] == "Sport - Collision":
        weight_PolicyType = 0.2456
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.0225
    elif elems[12] == "Utility - Collision":
        weight_PolicyType = 0.2280
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.0019
    else:
        weight_PolicyType =0.2105
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.0249
        
    final_output = weight_PolicyType + weight_Marital_Status + weight_Sex + weight_PastnumberOfClaims +  weight_vehiclePrice + weight_number_Of_Cars + weight_BasePolicy + weight_Vedhicle_category + weight_fault + weight_age + weight_witness_present + weight_police_report / 12

    #print final_output
    
    model = - math.log(final_output)
    
    output = 1 / (1 + math.exp(model))
    
    #print output
    
    print probab_age
    print probab_BP
    print probab_fault
    print probab_MS
    print probab_NOC
    print probab_PNOC
    print probab_police_report
    print probab_PT
    print probab_sex
    print probab_VC
    print probab_VP
    print probab_witness_present
    
    
    val = probab_age+probab_BP+probab_fault+probab_MS+probab_NOC+probab_PNOC+probab_police_report+probab_PT+probab_sex+probab_VC+probab_VP+probab_witness_present
    
    print val
    
    val = -val
    print (1/(1+math.exp((val))))
    
    if output>0.6:
        print "fraud_class"
    else:
        print "Not_a_fraud"

outlier ('Address of the test file')