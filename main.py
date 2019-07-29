digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

transform = {} 
for i in range(len(digits)): 
    transform[i+1] = {'French': fr[i], 'English':en[i] }


print(transform)





# to_ten = range(1, 11) 
# numbers = []
# for num in to_ten: 
#     numbers.append(num) 

# print(numbers) 


# dict_of_words = { i : {'french': fr , 'english': en} for i in numbers}

# # print(dict_of_words) 

# zip_dict_en = zip(digits, en) 
# zip_dict_fr = zip(digits, fr) 

# dict_of_en = dict(zip_dict_en)
# dict_of_fr = dict(zip_dict_fr) 



# # print(dict_of_en)
# # print(dict_of_fr)



