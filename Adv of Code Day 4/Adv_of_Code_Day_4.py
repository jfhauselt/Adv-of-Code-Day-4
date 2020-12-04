valid = 0
invalid = 0

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False 
for line in open(r"C:\Users\jfhau\Documents\#code\Day4.txt"):
    if line == "\n":
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid +=1
        else:
            print(False)
            invalid +=1
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False
    if "byr" in line:
        byr = True
    if "iyr" in line:
        iyr = True
    if "eyr" in line:
        eyr = True
    if "hgt" in line:
        hgt = True
    if "hcl" in line:
        hcl = True
    if "ecl" in line:
        ecl = True
    if  "pid" in line:
        pid = True
if byr and iyr and eyr and hgt and hcl and ecl and pid:
    valid +=1
print(valid)

