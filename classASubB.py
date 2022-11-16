# this script will be for class B subnet mask for class A ip address range, so third octet evaluation is
of interest here 
#regex for submask will have 3 possible second octet variations per each 3 third octet evaluation 

import re 

def class AB(ipadd, submask):
    sec_one_a = "[0-1]{2}[.][0-9]{1}[.][0-9]{1}[.][0-9]{1,3}"
    sec_one_b = "[0-1]]{2}[.][0-9]{2}[.][0-9]{1}[.][0-9]{1,3}"
    sec_one_c = "[0-1]]{2}[.][0-9]{3}[.][0-9]{1}[.][0-9]{1,3}"

    sec_two_a = "[0-1]{2}[.][0-9]{1}[.][0-9]{2}[.][0-9]{1,3}"
    sec_two_b = "[0-1]]{2}[.][0-9]{2}[.][0-9]{2}[.][0-9]{1,3}"
    sec_two_c = "[0-1]]{2}[.][0-9]{3}[.][0-9]{2}[.][0-9]{1,3}"

    sec_three_a = "[0-1]{2}[.][0-9]{1}[.][0-9]{3}[.][0-9]{1,3}"
    sec_three_b = "[0-1]]{2}[.][0-9]{2}[.][0-9]{3}[.][0-9]{1,3}"
    sec_three_c = "[0-1]]{2}[.][0-9]{3}[.][0-9]{3}[.][0-9]{1,3}"
    match_one_a = re.findall(sec_one_a, ipadd)
    match_one_b = re.findall(sec_one_b, ipadd)
    match_one_c = re.findall(sec_one_c, ipadd)
    
    match_two_a = re.findall(sec_two_a, ipadd)
    match_two_b = re.findall(sec_two_b, ipadd)
    match_two_c = re.findall(sec_two_c, ipadd)
   
    match_three_a= re.findall(sec_three_a, ipadd)
    match_three_b = re.findall(sec_three_b, ipadd)
    match_three_c = re.findall(sec_three_c, ipadd)

    make_list = []
    make_list.append(ipadd)
    broad_add = '.255'
    last_add = '.254'    
    first_add= '.1'
    net_add = '.0'
    cl = "10."
    oct_2 = ''
    blsz_find = 0 
    oct_bound = 0 
    sub_aa = "255.255.128.0"
    sub_ab = "255.255.192.0"
    sub_ac = "255.255.224.0"
    sub_ad = "255.255.240.0"
    sub_ae = "255.255.248.0"
    sub_af = "255.255.252.0"
    sub_ag = "255.255.254.0"

    
    if match_one_a == make_list: 
        blsz_find = int(ipadd[5:6])
        oct_2 = ipadd[3:5]
    elif match_one_b == make_list:
        blsz_find = int(ipadd[6:7]) 
        oct_2 = ipadd[3:6]
    elif match_one_c == make_list: 
        blsz_find = int(ipadd[7:8])
        oct_2 = ipadd[3:7]
    elif match_two_a == make_list: 
        blsz_find = int(ipadd[5:7])
        oct_2 = ipadd[3:5]
    elif match_two_b == make_list:
        blsz_find = int(ipadd[6:8]) 
        oct_2 = ipadd[3:6]
    elif match_two_c == make_list: 
        blsz_find = int(ipadd[7:9])
        oct_2 = ipadd[3:7]
    elif match_three_a == make_list: 
        blsz_find = int(ipadd[5:8])
        oct_2 = ipadd[3:5]
    elif match_three_b == make_list:
        blsz_find = int(ipadd[6:9]) 
        oct_2 = ipadd[3:6]
    elif match_three_c == make_list: 
        blsz_find = int(ipadd[7:10])
        oct_2 = ipadd[3:7]
    else:
        print("Please enter a valid ip address and/ or submask")
   
    if submask == sub_aa:
        oct_bound = 128
    elif submask == sub_ab:
        oct_bound = 64
    elif submask == sub_ac:
        oct_bound = 32
    elif submask == sub_ad:
        oct_bound = 16
    elif submask == sub_ae:
        oct_bound = 8
    elif submask == sub_af:
        oct_bound = 4
    else:
        print("Please enter a valid submask")
    
    if blsz_find // oct_bound == 0:
        begin_octet = str(blsz_find // oct_bound)
        end_octet = str((blsz_find // oct_bound) + oct_bound - 1)
        broad_octet = end_octet
    else:
        octet_count = blsz_find // oct_bound + 1
        begin_octet = str(blsz_find // oct_bound * oct_bound)   
        end_octet = str((octet_count * oct_bound) -1)
        broad_octet = end_octet

    
 
    print(oct_2)
    print(oct_bound)
    print(submask)       
    print(ipadd + " belongs to a class A private address space ranging from " + cl + oct_2 + begin_octet + first_add + " to " + cl + oct_2 + end_octet + last_add + " with a Network address of " + cl + oct_2 + begin_octet + net_add + " and a broadcast address of " + cl + oct_2 + broad_octet + broad_add +".")

classAB('10.2.3.4','255.255.128.0')
classAB('10.234.4.16','255.255.192.0')
classAB('10.55.12.188','255.255.224.0')
classAB('10.0.245.34','255.255.240.0')
classAB('10.240.78.1', '255.255.248.0')
classAB('10.45.80.90', '255.255.252.0')
#classAB('10.78.90.23', 'not a valid submask')
classAB('not a valid ip', '255.255.224.0')
    