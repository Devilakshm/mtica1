sample_dict={
    "name":"kelly",
    "age":24,
    "salary":8000,
    "city":"Newyork"}
sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)
