marks = { 
    "Vinay" : 100,
    "Shubham": 56,
    "Amit" : 23,
    0: "Vinay"
}

#print(marks.keys())
#print(marks.items())
#print(marks.values())
#marks.update({"Vinay":99, "Jaya": 18})
#print(marks)

print(marks.get("vinay5")) # Prints none
print(marks["Vinay5"]) #Returns an error