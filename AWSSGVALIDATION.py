from boto import ec2

conn = ec2.connect_to_region("eu-west-2")
#reservations = conn.get_all_instances()
reservations = conn.get_all_reservations()

# security group list
sg_array = []

# instances and security groups:

ins_sg = {}

# go through instance list:
for i in reservations:

# check how many SGs are attached to instance
    group_nums = len(i.instances[0].groups)
    print ("######################\n")
    print ("InstanceID: %s\n" % i.instances[0])
    print ("Number of SGs attached: %s\n" % group_nums)
# go through each SG
    for z in range(group_nums):
        
# find id for each Security Group
        group_id = i.instances[0].groups[z].id
        sg_name = conn.get_all_security_groups(group_ids=group_id)[0]
        
# describe rules for each SG
        sec_rules = conn.get_all_security_groups(group_ids=group_id)[0].rules
        
# calculate number of rules
        rule_nums = len(sec_rules)
        
# print SG name
        print ("%s\n" % sg_name)
        
# print SG Ingress rules
        print ("Ingress Rules:\n\n")
        for g in range(rule_nums):
           
            #print ("Port/protocol: %s" % conn.get_all_security_groups(group_ids=group_id)[0].rules[g])
            print ("Source: %s" % conn.get_all_security_groups(group_ids=group_id)[0].rules[g].grants)
            #sesh  Converted OBJECT into string then compared.
            if (str(conn.get_all_security_groups(group_ids=group_id)[0].rules[g].grants) == "[0.0.0.0/0]"):
                 {
                    print ('Security Group is NOT SECURE : ')
                 }
            else:
                print ('Security Group is SECURE ')
                print ("\n\n")
        print ("\n\n")
