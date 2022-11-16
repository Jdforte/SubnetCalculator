# SubnetCalculator
A standalone program which calculates a valid private IPV4 address range given an IP address and subnet mask. 
This is a work in progess! However the basic program can be tested by running either of the two currently listed programs: SubExperimentTwo.py or classASubB.py.

SubExperimentTwo.py only accepts a class A ip address with the following submasks:

 255.128.0.0
 255.192.0.0
 255.224.0.0
 255.240.0.0
 255.248.0.0
 255.252.0.0
 255.254.0.0
 
 classASubB.py only accepts a class A ip address with the following submasks:
 
 255.255.128.0
 255.255.192.0
 255.255.224.0
 255.255.240.0
 255.255.248.0
 255.255.252.0
 255.255.254.0

The class A private ipv4 address space spans from 10.0.0.0 - 10.255.255.255.
Inputting an address not from this range or a submask that is not recommended for either script will result in errors or inaccurate results. 

Scripts can be tested by comparing results to calcuations made using this website https://www.calculator.net/ip-subnet-calculator.html
 
The ultimate goal for this project is to create a standalone program that evaluates the entire ipv4 address space, can run without the requirement of having python previously installed on the client and handles errors efficiently. 
