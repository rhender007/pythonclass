'''
Created on Nov 29, 2016

@author: Student

Validation function for US Zip Code
'''
def zip_check(z):
    """
    Validate z as either NNNNN or NNNNN-NNNN
    """
    l = len(z)
    if l not in (5, 10):
        return "Zip codes should be 5 or 10 characters long"
    if (not z[:5].isdigit() or
        l == 10 and not z[6:].isdigit()):
        return "Zip code contains non-numeric characters"
    if l == 10 and z[5] != "-":
        return "Ten-digit zips must have a dash between the two parts"
    return "Zip code is Valid"

print(zip_check("123455"))
        
    