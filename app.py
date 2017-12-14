from flask import Flask, render_template, json, request, flash, redirect, url_for
from geopy.geocoders import Nominatim
from flask.ext.mysql import MySQL
import numpy as np
import math
mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'random string'


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Insurance'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
@app.route("/")
def main():
    return render_template('index.html')
@app.route('/carRepair')
def carRepair():
    return render_template('signup.html')
@app.route('/otherFeatures')
def otherFeatures():
    return render_template('details.html')
@app.route("/success")
def success():
    return render_template('success.html')
@app.route('/submit',methods=['POST','GET'])
def submit():
    make=request.form['make']

    area=request.form['area']
    sex=request.form['sex']
    marital=request.form['maritalStatus']
    age=request.form['age']
    fault=request.form['fault']
    policyType=request.form['policyType']
    vehicleCategory=request.form['vehicleCategory']
    vehiclePrice=request.form['vehiclePrice']
    pastClaims=request.form['noOfClaims']
    policeReport=request.form['policeReport']
    witnessPresent=request.form['policeReport']
    noOfCars=request.form['noOfCars']
    basePolicy=request.form['basePolicy']

    f = open("details.txt","w")
    f.write(make+","+ area+","+ sex+","+ marital+","+ age+","+ fault+","+ policyType+","+ vehicleCategory+","+ vehiclePrice+","+ pastClaims+","+ policeReport+","+ witnessPresent+","+ noOfCars+","+ basePolicy+ "\n")
    f.close()

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO details(make,area,sex,marital_status,age,fault,policyType,vehicleCategory,vehiclePrice,pastClaims,policeReport,witnessPresent,noOfCars,basePolicy) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (make,area,sex,marital,age,fault,policyType,vehicleCategory,vehiclePrice,pastClaims,policeReport,witnessPresent,noOfCars,basePolicy))
    conn.commit()
    cursor.close()
    conn.close()

    total_fraud_prob = float(923)/15420

    file_name = open("details.txt","r")
    elems = file_name.readline()
    elems = elems.split(',')

    if elems[4] == 'No':
        weight_police_report = 0.6 #to be determined
        probab_police_report = (weight_police_report * total_fraud_prob)/0.9722
    else:
        weight_police_report = 0.4
        probab_police_report = (weight_police_report * total_fraud_prob)/(0.0277)

    if elems[11] == 'No':
        weight_witness_present = 0.6#to be determined
        probab_witness_present = (weight_witness_present * total_fraud_prob)/0.9943
    else:
        weight_witness_present = 0.4
        probab_witness_present = (weight_witness_present * total_fraud_prob)/0.0056

    if int(elems[4])<18:
        weight_age = 0.1369 #to be determined
        probab_age = (weight_age*total_fraud_prob)/0.0217
    elif int(elems[4])<=20:
        weight_age = 0.1917
        probab_age = (weight_age*total_fraud_prob)/0.0070
    elif int(elems[4])<=25:
        weight_age = 0.2054
        probab_age = (weight_age*total_fraud_prob)/0.0397
    elif int(elems[4])<=30:
        weight_age = 0.0684
        probab_age = (weight_age*total_fraud_prob)/0.1804
    elif int(elems[4])<=35:
        weight_age = 0.0958
        probab_age = (weight_age*total_fraud_prob)/0.1822
    elif int(elems[4])<=40:
        weight_age = 0.0821
        probab_age = (weight_age*total_fraud_prob)/0.1308
    elif int(elems[4])<=50:
        weight_age = 0.0682
        probab_age = (weight_age*total_fraud_prob)/0.2253
    elif int(elems[4])<=65:
        weight_age = 0.0684
        probab_age = (weight_age*total_fraud_prob)/0.1796
    else:
        weight_age = 0.0821
        probab_age = (weight_age*total_fraud_prob)/0.0329


    if elems[5] == 'Policy Holder':
        weight_fault = 0.8823
        probab_fault = (weight_fault*total_fraud_prob)/0.7282
    else:
        weight_fault= 0.1176
        probab_fault = (weight_fault*total_fraud_prob)/0.2717

    if elems[7] == 'Sedan':
        weight_Vedhicle_category = 0.3636#to_be_determined
        probab_VC = (weight_Vedhicle_category*total_fraud_prob)/0.6271
    elif elems[7] == 'Utility':
        weight_Vedhicle_category = 0.0909#to_be_determined
        probab_VC = (weight_Vedhicle_category*total_fraud_prob)/0.3474
    else:
        weight_Vedhicle_category = 0.5454#to_be_determined
        probab_VC = (weight_Vedhicle_category*total_fraud_prob)/0.0253

    if elems[13] == "All perils":
        weight_BasePolicy = 0.5555
        probab_BP = (weight_BasePolicy*total_fraud_prob)/0.2885
    elif elems[13] == "Collision":
        weight_BasePolicy = 0.3888
        probab_BP = (weight_BasePolicy*total_fraud_prob)/0.3866
    else:
        weight_BasePolicy = 0.0555
        probab_BP = (weight_BasePolicy*total_fraud_prob)/0.3248

    if elems[12] == "1 vehicle":
        weight_number_Of_Cars = 0.2553
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.9284
    elif elems[12] == "2 vehicle":
        weight_number_Of_Cars = 0.2553
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.0459
    elif elems[12] == "3 to 4":
        weight_number_Of_Cars = 0.3191
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.0241
    else:
        weight_number_Of_Cars = 0.1702
        probab_NOC = (weight_number_Of_Cars*total_fraud_prob)/0.0014

    if elems[8] == 'less than 20000':
        weight_vehiclePrice = 0.2567
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.0710
    elif elems[8] == '20000 to 29000':
        weight_vehiclePrice = 0.1351
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.5239
    elif elems[8] == '30000 to 39000':
        weight_vehiclePrice = 0.1216
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.2291
    elif elems[8] == '40000 to 59000':
        weight_vehiclePrice = 0.1756
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.0298
    elif elems[8] == '60000 to 69000':
        weight_vehiclePrice = 0.1081
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.0056
    else:
        weight_vehiclePrice = 0.2027
        probab_VP = (weight_vehiclePrice*total_fraud_prob)/0.1403

    if elems[9] == 'none':
        weight_PastnumberOfClaims = 0.3333
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.2822
    elif elems[9] == '1':
        weight_PastnumberOfClaims = 0.2666
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.2317
    elif elems[9] == '2 to 4':
        weight_PastnumberOfClaims = 0.2222
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.3557
    elif elems[9] == 'more than 4':
        weight_PastnumberOfClaims = 0.1777
        probab_PNOC = (weight_PastnumberOfClaims*total_fraud_prob)/0.1303

    if elems[2] == 'Male':
        weight_Sex = 0.60
        probab_sex = (weight_Sex*total_fraud_prob)/0.8430
    elif elems[2] == 'Female':
        weight_Sex = 0.40
        probab_sex = (weight_Sex*total_fraud_prob)/0.1569

    if elems[3] == 'Divorced':
        weight_Marital_Status = 0.16
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.0049
    elif elems[3] == 'Married':
        weight_Marital_Status = 0.26
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.6890
    elif elems[3] == 'Single':
        weight_Marital_Status = 0.26
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.3037
    elif elems[3] == 'Widow':
        weight_Marital_Status = 0.32
        probab_MS = (weight_Marital_Status*total_fraud_prob)/0.0022

    if elems[6] == "Sedan - All Perils":
        weight_PolicyType = 0.1754
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.2650
    elif elems[6] == "Sedan - Collision":
        weight_PolicyType = 0.1228
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.3621
    elif elems[6] == "Sedan - Liability":
        weight_PolicyType = 0.0175
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.3234
    elif elems[6] == "Sport - Collision":
        weight_PolicyType = 0.2456
        probab_PT = (weight_PolicyType*total_fraud_prob)/0.0225
    elif elems[6] == "Utility - Collision":
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

    print ("Probability of Age: "+ str(probab_age))
    print ("Probability of Base Policy: "+ str(probab_BP))
    print ("Probability of Fault: "+ str(probab_fault))

    print ("Probability of Marital Status: "+ str(probab_MS))
    print ("Probability of No of Cars: "+ str(probab_NOC))
    print ("Probability of Past no of Claims: "+ str(probab_PNOC))
    print ("Probability of Police Report: "+ str(probab_police_report))
    print ("Probability of Policy Type: "+ str(probab_PT))
    print ("Probability of Sex: "+ str(probab_sex))
    print ("Probability of Vehicle Category: "+ str(probab_VC))
    print ("Probability of vehicle Price: "+ str(probab_VP))
    print ("Probability of Witness Present: "+ str(probab_witness_present))


    val = probab_age*probab_BP*probab_fault*probab_MS*probab_NOC*probab_PNOC*probab_police_report*probab_PT*probab_sex*probab_VC*probab_VP*probab_witness_present

    #print val

    val = -val
    val = (1/(1+math.exp((val))))
    print("Probability of Fraud is: "+ str(val))

    if output>0.6:
        #print "Fraud Detected"
        var1="Fraud Class"
        return json.dumps({'message':'Fraud Detected'})
    else:
        #print "Not Fraud"
        var1="Not Fraud"
        return json.dumps({'message':'Not Fraud'})
    #return redirect(url_for('success'))

@app.route('/signUp',methods=['POST','GET'])
def signUp():

    price = request.form['inputName']
    #print(price)
    car_model = request.form['inputEmail']
    #print(car_model)
    part = request.form['inputPassword']
    #print(part)
    location = request.form['location']
    #print(location)
    geolocator = Nominatim()
    location = geolocator.geocode(location)
    latitude = location.latitude
    longitude = location.longitude

    f = open("price.txt","w")
    f1 = open("location.txt","w")
    f.write(car_model+" "+ part+" "+ price+ "\n")
    f1.write(str(latitude)+" "+str(longitude)+ "\n")
    f.close()
    f1.close()

    #print(car_model)
    #print(location)
    #print(part)
    conn = mysql.connect()
    cursor = conn.cursor()
    #db = MySQLdb.connect(host="localhost",user="root",passwd="",db="Insurance")
    #cursor = db.cursor()
    cursor.execute("INSERT INTO repair(latitude,longitude,car_model,part,location) VALUES(%s,%s,%s,%s,%s)",(str(latitude),str(longitude),str(car_model),str(part),str(location)))
    conn.commit()
    cursor.close()
    conn.close()
    #print("done")


    data_file = open("Data_set0.txt")
    list_elem = data_file.readlines()
    list_needed = list_elem[3:]
    list_lat = []
    list_lon = []
    for elem in list_needed:
        list_lat.append(float(elem.split()[0]))
        list_lon.append(float(elem.split()[1]))

    list_lat = np.asarray(list_lat)
    list_lon = np.asarray(list_lon)
    mean_lat = np.mean(list_lat)
    mean_lon = np.mean(list_lon)

    ##lat_obj = float(raw_input())#########latitude insted of raw_input#############
    lat_obj = float(latitude)
    lon_obj = float(longitude)###########longitude insted of raw_input##########
    if( math.sqrt( abs(mean_lat - lat_obj)**2 + abs(mean_lon-lon_obj)**2) <= 1):
        val2 =  "inlier"
        #print math.sqrt( abs(mean_lat - lat_obj)**2 + abs(mean_lon-lon_obj)**2)
    else:
        val2 = "outlier"
    data_file = open("Car_Dataset.txt")
    list_elem = data_file.readlines()
    list_needed = list_elem[1:]
    list_name = []
    list_part = []
    list_price = []
    for elem in list_needed:
        list_name.append(str(elem.split()[0]))
        #print (elem.split()[0])
        list_part.append(str(elem.split()[1]))
        #print (elem.split()[1])
        list_price.append(int(elem.split()[2]))
        #print (elem.split()[2])

    list_name = np.asarray(list_name)
    #print list_name
    list_part = np.asarray(list_part)
    #print list_part
    list_price = np.asarray(list_price)
    #print list_price
    name_obj = str(car_model)#########car_model insted of raw_input#############
    part_obj = str(part)#########part insted of raw_input#############
    price_obj  = int(price)#########price insted of raw_input#############

    name_count = 0
    part_count = 0
    price_count = 0
    i=0
    for name in list_name:
        name_count = name_count + 1
        if name == name_obj:
            if list_part[name_count-1] == part_obj and price_obj <= list_price[name_count-1] :
                i = 1
                val1 =  "inlier"
                break



    if i==0:
        val1 = "Outlier"
    #print("done outlier rejection algorithm")

    if val1 == val2 and val1 == "inlier":
        print ("Fraud detection using outlier clustering algorithm: "+ str(val1) +  " detected")
        result="Inlier Detected"
        return json.dumps({'message':'Not Fraud'})
        #flash('You were successfully logged in')
    else:
        print ("Fraud detection using outlier clustering algorithm: "+ str(val1) +  " detected")
        result="Outlier Detected"
        return json.dumps({'message':'Fraud Detected'})
        #flash('You were successfully logged in')

    #return redirect(url_for('main'))



if __name__ == "__main__":
    app.run()
