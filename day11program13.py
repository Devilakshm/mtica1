sample_dict={
    'physics':87,
    'Math':64,
    'History':76
    }
print(max(sample_dict,key=sample_dict.get))
print(min(sample_dict,key=sample_dict.get))
print(count(sample_dict,key=sample_dict.get))

