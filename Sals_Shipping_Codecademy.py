weight = 41.5

#Ground Shipping
if weight <= 2:
  groundcost = 20 + weight * 1.5
elif weight <=6:
  groundcost = 20 + weight * 3
elif weight <=10:
  groundcost = 20 + weight * 4
elif weight > 10:
  groundcost = 20 + weight * 4.75

print ("Posting by Ground Shipping would cost: £" + str(groundcost))

#Premium Ground Shipping - flat rate only
premium_ground_shipping = 125.00
print("Posting by Ground Shipping Premium would cost: £" + str(premium_ground_shipping))

#Drone Shipping
if weight <=2:
  dronecost = weight * 4.5
elif weight <=6:
  dronecost = weight * 9
elif weight <=10:
  dronecost = weight * 12
elif weight >10:
  dronecost = weight * 14.25

print("Posting by Drone Shipping would cost £" + str(dronecost))