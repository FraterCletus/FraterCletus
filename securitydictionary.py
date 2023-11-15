#!/usr/bin/python3
zero_trust = ['Identities', 'Devices', 'Applications', 'Data', 'Infrastructure']
shared_trust = ['On-Premise', 'IaaS', 'PaaS', 'SaaS']
def_in_depth = ['Physical', 'Identity Access', 'Perimeter', 'Network', 'Compute', 'Data']
cia = ['Confidentiality', 'Integrity', 'Availability']
threats = ['Data Breach', 'Phishing', 'Spear Phishing', 'SQL Injection', 'ID Attack', 'Brute Force', 'Ransomware', 'Malware', 'Disruptive', 'Root Kit', 'Trojan', 'Worm', 'Exploit', 'Exploit Kit']
encrypt = ['Symmetric', 'Asymmetric', 'Key Pair', 'Public Key', 'Private Key', 'Encryption at Rest', 'Encryption in Transit', 'Hashing', 'Salting', 'Signing',]
trust_portal = ['Security', 'Privacy', 'Compliance']
privacy = ['Control', 'Transparency', 'Security', 'Strong Legal Protections', 'No Content-based targeting', 'Benefits to You']
compliance = ['Documentation', 'Region', 'Industry', 'Regulation', 'Audit']
ids = ['Administration', 'Authentication', 'Authorization', 'Auditing']
authentication = ['Identity Provider IdP','Single-Sign-On', 'Federation', 'Token', 'Resources']
AD_IdP = ['Users', 'Service Principals', 'Managed Identities', 'Devices', 'Credentials', 'Access Rights', 'Domain Controller DC']
Azure_AD = ['Resources', 'MFA', 'Office 365', 'Tools']
azure_version = ['Free', 'Office 365 Apps', 'P1', 'P2']
user = ['Managed by Azure AD', 'Form Groups', 'B2B', 'B2C', 'Guest User']
service_principal = ['AD ID', 'Application Used', 'ID Permissions', 'Device Permissions']
managed_id = ['System Assigned', 'User Assigned']
device = ['Mobile Device', 'Laptop', 'Desktop', 'Server', 'Printer']
Azure_MFA = ['Password', 'Additional Verification', 'Open Authentication', 'Time-based one time passwords', 'hardware token', 'Passwordless Authentication', 'Biometrics']
tools = contents = ['Active Directory', 'Virtual Network', 'Firewall', 'Network Security Group', 'Key Vault', 'Customer Lockbox', 'Security Center', 'Sentinel', 'Defender', 'DDoS Protection', 'enter For Information Security ', 'XDR', 'SIEM', 'SOAr', 'eDiscovery']
nsg_rules = ['Name', 'Priority', 'Source or Destination', 'Protocol', 'Direction', 'Port Range', 'Action']


zero_trust_dict = {'Identities': 'A user or device on the network.', 'Devices': 'Hardware assets such as a Mobile Phone, Tablet, Laptop, Desktop, Server or Printer.', 'Applications': 'Software used to process data into more complex or simple documents', 'Data': 'Information represented as a text object', 'Infrastructure': 'Configurations and controls of a network'}
shared_trust_dict = {'On-Premise': 'Managed on site', 'IaaS': 'Networking, Storage, Servers, Virtualization', 'PaaS': 'Operating System, Middleware, Runtime', 'SaaS': 'Data, Applications'}
def_in_depth_dict = {'Physical': 'Physical building security and controlling access to computing hardware within the data center is the first line of defense.', 'Identity Access': 'SSO and MFA', 'Perimeter': 'DDoS and Firewall protection', 'Network': 'Inbound/outbound restrictions and load balancers', 'Compute': 'Secure access to and between VMs', 'Data': 'Valued information'}
cia_dict = {'Confidentiality': 'Information is not for public use', 'Integrity': 'Information is accurately kept', 'Availability': 'Information can be accessed as required on secure platform'}
threats_dict = {'Data Breach': 'Any Data Security Violation', 'Phishing': 'A socially engineered attack designed to get information from someone, usually a scam', 'Spear Phishing': 'Phishing attack directed towards a specific person', 'SQL Injection': 'Code injection to tamper with security or data held in a database', 'ID Attack': 'A breach of ID credentials', 'Brute Force': 'An attack where a list of possible passwords is tested on a specific device', 'Ransomware': 'Malware designed to extort funds or favors from victim', 'Malware': 'Malicious software that is installed onto a device for the benefit of the attacker', 'Disruptive': 'Action designed to disrupt access or normal function of an application or network DDoS', 'Root Kit': 'A collection of software designed to enable access to a network or computer ShadowBrokers!', 'Trojan': 'Malware disguised as software that is designed to bypass user ', 'Worm': 'A malware desiged to replicate itself and be sent to other computers', 'Exploit': 'A chunk of code or data software used to exploit any software', 'Exploit Kit': 'A tool kit of exploits used in conjunction and usually in PHP'}
encrypt_dict = {'Symmetric': 'An algorithm in cryptography that uses a shared secret between sender and receiver', 'Asymmetric': 'An algorithm that uses a public and private key pairs', 'Key Pair': 'Separate keys to encrypt+public and decrypt+private information', 'Public Key': 'Message encryption permissions', 'Private Key': 'Message decryption permissions', 'Encryption at Rest': 'Information is not available on database without private key', 'Encryption in Transit': 'Information being transferred is not available without a private key', 'Hashing': 'Takes a string of any length as input and produce a fixed-length hash value. ', 'Salting': 'A random string used to verify validity of message in transit in conjunction with hashing', 'Signing': 'Mathematical verification of authenticity'}
trust_portal_def = {'Security': "['Administration', 'Authentication', 'Authorization', 'Auditing']", 'Privacy': "['Control', 'Transparency', 'Security', 'Strong Legal Protections', 'No Content-based targeting', 'Benefits to You']", 'Compliance': "['Documentation', 'Region', 'Industry', 'Regulation', 'Audit']"}
tools_dict = {'Active Directory': 'Identity Provider Tool', 'Virtual Network': 'Network of computers in cloud', 'Firewall': 'Defends azure resources and provisions NSG', 'Network Security Group': 'Network Security Group', 'Key Vault': 'Repository for API keys and certificates', 'Customer Lockbox': 'Keeps B2C information secure while investigations take place', 'Security Center': 'A part of portal where all security related issues can be monitored and resolved', 'Sentinel': 'SIEM engine that monitors security incidences', 'Defender': 'A blue team tool for detection of security breaches', 'DDoS Protection': 'Free service that protects your network against disruptive DoS', 'enter For Information Security ': 'An organization that provides default standard benchmarks for network applications and security', 'XDR': 'Security intelligence log', 'SIEM': 'XDR based threat detection', 'SOAR': 'Security orchestration automation and response', 'eDiscovery': 'The process of audit for privacy and compliance reasons'}
dictitle = ('The Zero Trust Model:', 'The Shared Trust Model:', 'Defense in Depth:', 'The CIA Triad:', "Common Threats", 'Basic Encryption:', 'The Azure Trust Portal:', 'Azure tools')
details = (zero_trust_dict, shared_trust_dict, def_in_depth_dict, cia_dict, threats_dict, encrypt_dict, trust_portal_def, tools_dict)
x = 0

for detail in details:
    print(f'************{dictitle[x]}*****************')
    keys = detail.keys()
    values = detail.values()
    items = detail.items()
    x += 1
    for key, value in detail.items():
        print(f"{key}: {value}")
        print('')

lists = {
    'zero_trust': ['Identities', 'Devices', 'Applications', 'Data', 'Infrastructure'],
    'shared_trust': ['On-Premise', 'IaaS', 'PaaS', 'SaaS'],
    'def_in_depth': ['Physical', 'Identity Access', 'Perimeter', 'Network', 'Compute', 'Data'],
    'cia': ['Confidentiality', 'Integrity', 'Availability'],
    'threats': ['Data Breach', 'Phishing', 'Spear Phishing', 'SQL Injection', 'ID Attack', 'Brute Force', 'Ransomware', 'Malware', 'Disruptive', 'Root Kit', 'Trojan', 'Worm', 'Exploit', 'Exploit Kit'],
    'encrypt': ['Symmetric', 'Asymmetric', 'Key Pair', 'Public Key', 'Private Key', 'Encryption at Rest', 'Encryption in Transit', 'Hashing', 'Salting', 'Signing',],
    'trust_portal': ['Security', 'Privacy', 'Compliance'],
    'privacy': ['Control', 'Transparency', 'Security', 'Strong Legal Protections', 'No Content-based targeting', 'Benefits to You'],
    'compliance': ['Documentation', 'Region', 'Industry', 'Regulation', 'Audit'],
    'ids': ['Administration', 'Authentication', 'Authorization', 'Auditing'],
    'authentication': ['Identity Provider IdP','Single-Sign-On', 'Federation', 'Token', 'Resources'],
    'AD_IdP': ['Users', 'Service Principals', 'Managed Identities', 'Devices', 'Credentials', 'Access Rights', 'Domain Controller DC'],
    'Azure_AD': ['Resources', 'MFA', 'Office 365', 'Tools'],
    'azure_version': ['Free', 'Office 365 Apps', 'P1', 'P2'],
    'user': ['Managed by Azure AD', 'Form Groups', 'B2B', 'B2C', 'Guest User'],
    'service_principal': ['AD ID', 'Application Used', 'ID Permissions', 'Device Permissions'],
    'managed_id': ['System Assigned', 'User Assigned'],
    'device': ['Mobile Device', 'Laptop', 'Desktop', 'Server', 'Printer'],
    'Azure_MFA': ['Password', 'Additional Verification', 'Open Authentication', 'Time-based one time passwords', 'hardware token', 'Passwordless Authentication', 'Biometrics'],
    'tools': ['Active Directory', 'Virtual Network', 'Firewall', 'Network Security Group', 'Key Vault', 'Customer Lockbox', 'Security Center', 'Sentinel', 'Defender', 'DDoS Protection', 'Center For Information Security ', 'XDR', 'SIEM', 'SOAR', 'eDiscovery'],
    'nsg_rules': ['Name', 'Priority', 'Source or Destination', 'Protocol', 'Direction', 'Port Range', 'Action']
}
print("******Let's build a document outline that will help you understand your network better.-----")
print('zero_trust, shared_trust, def_in_depth, cia, threats , encrypt, trust_portal, privacy, compliance, ids, authentication, AD_IdP, Azure_AD, azure_version, user, service_principal, managed_id, device, Azure_MFA', 'tools', 'nsg_rules')
lista = input('Please name the first list that you would like to use: ')
listb = input('Please name the second list that you would like to use: ')

if lista in lists and listb in lists:
    for item_a in lists[lista]:
        print(item_a)
        for item_b in lists[listb]:
            print('    ' + item_b)
        print()
else:
    print('Invalid list names provided')

#!/usr/bin/python3
zero_trust = ['Identities', 'Devices', 'Applications', 'Data', 'Infrastructure']
shared_trust = ['On-Premise', 'IaaS', 'PaaS', 'SaaS']
def_in_depth = ['Physical', 'Identity Access', 'Perimeter', 'Network', 'Compute', 'Data']
cia = ['Confidentiality', 'Integrity', 'Availability']
threats = ['Data Breach', 'Phishing', 'Spear Phishing', 'SQL Injection', 'ID Attack', 'Brute Force', 'Ransomware', 'Malware', 'Disruptive', 'Root Kit', 'Trojan', 'Worm', 'Exploit', 'Exploit Kit']
encrypt = ['Symmetric', 'Asymmetric', 'Key Pair', 'Public Key', 'Private Key', 'Encryption at Rest', 'Encryption in Transit', 'Hashing', 'Salting', 'Signing',]
trust_portal = ['Security', 'Privacy', 'Compliance']
privacy = ['Control', 'Transparency', 'Security', 'Strong Legal Protections', 'No Content-based targeting', 'Benefits to You']
compliance = ['Documentation', 'Region', 'Industry', 'Regulation', 'Audit']
ids = ['Administration', 'Authentication', 'Authorization', 'Auditing']
authentication = ['Identity Provider IdP','Single-Sign-On', 'Federation', 'Token', 'Resources']
AD_IdP = ['Users', 'Service Principals', 'Managed Identities', 'Devices', 'Credentials', 'Access Rights', 'Domain Controller DC']
Azure_AD = ['Resources', 'MFA', 'Office 365', 'Tools']
azure_version = ['Free', 'Office 365 Apps', 'P1', 'P2']
user = ['Managed by Azure AD', 'Form Groups', 'B2B', 'B2C', 'Guest User']
service_principal = ['AD ID', 'Application Used', 'ID Permissions', 'Device Permissions']
managed_id = ['System Assigned', 'User Assigned']
device = ['Mobile Device', 'Laptop', 'Desktop', 'Server', 'Printer']
Azure_MFA = ['Password', 'Additional Verification', 'Open Authentication', 'Time-based one time passwords', 'hardware token', 'Passwordless Authentication', 'Biometrics']
tools = contents = ['Active Directory', 'Virtual Network', 'Firewall', 'Network Security Group', 'Key Vault', 'Customer Lockbox', 'Security Center', 'Sentinel', 'Defender', 'DDoS Protection', 'enter For Information Security ', 'XDR', 'SIEM', 'SOAr', 'eDiscovery']

zero_trust_dict = {'Identities': 'A user or device on the network.', 'Devices': 'Hardware assets such as a Mobile Phone, Tablet, Laptop, Desktop, Server or Printer.', 'Applications': 'Software used to process data into more complex or simple documents', 'Data': 'Information represented as a text object', 'Infrastructure': 'Configurations and controls of a network'}
shared_trust_dict = {'On-Premise': 'Managed on site', 'IaaS': 'Networking, Storage, Servers, Virtualization', 'PaaS': 'Operating System, Middleware, Runtime', 'SaaS': 'Data, Applications'}
def_in_depth_dict = {'Physical': 'Physical building security and controlling access to computing hardware within the data center is the first line of defense.', 'Identity Access': 'SSO and MFA', 'Perimeter': 'DDoS and Firewall protection', 'Network': 'Inbound/outbound restrictions and load balancers', 'Compute': 'Secure access to and between VMs', 'Data': 'Valued information'}
cia_dict = {'Confidentiality': 'Information is not for public use', 'Integrity': 'Information is accurately kept', 'Availability': 'Information can be accessed as required on secure platform'}
threats_dict = {'Data Breach': 'Any Data Security Violation', 'Phishing': 'A socially engineered attack designed to get information from someone, usually a scam', 'Spear Phishing': 'Phishing attack directed towards a specific person', 'SQL Injection': 'Code injection to tamper with security or data held in a database', 'ID Attack': 'A breach of ID credentials', 'Brute Force': 'An attack where a list of possible passwords is tested on a specific device', 'Ransomware': 'Malware designed to extort funds or favors from victim', 'Malware': 'Malicious software that is installed onto a device for the benefit of the attacker', 'Disruptive': 'Action designed to disrupt access or normal function of an application or network DDoS', 'Root Kit': 'A collection of software designed to enable access to a network or computer ShadowBrokers!', 'Trojan': 'Malware disguised as software that is designed to bypass user ', 'Worm': 'A malware desiged to replicate itself and be sent to other computers', 'Exploit': 'A chunk of code or data software used to exploit any software', 'Exploit Kit': 'A tool kit of exploits used in conjunction and usually in PHP'}
encrypt_dict = {'Symmetric': 'An algorithm in cryptography that uses a shared secret between sender and receiver', 'Asymmetric': 'An algorithm that uses a public and private key pairs', 'Key Pair': 'Separate keys to encrypt+public and decrypt+private information', 'Public Key': 'Message encryption permissions', 'Private Key': 'Message decryption permissions', 'Encryption at Rest': 'Information is not available on database without private key', 'Encryption in Transit': 'Information being transferred is not available without a private key', 'Hashing': 'Takes a string of any length as input and produce a fixed-length hash value. ', 'Salting': 'A random string used to verify validity of message in transit in conjunction with hashing', 'Signing': 'Mathematical verification of authenticity'}
trust_portal_def = {'Security': "['Administration', 'Authentication', 'Authorization', 'Auditing']", 'Privacy': "['Control', 'Transparency', 'Security', 'Strong Legal Protections', 'No Content-based targeting', 'Benefits to You']", 'Compliance': "['Documentation', 'Region', 'Industry', 'Regulation', 'Audit']"}
tools_dict = {'Active Directory': 'Identity Provider Tool', 'Virtual Network': 'Network of computers in cloud', 'Firewall': 'Defends azure resources and provisions NSG', 'Network Security Group': 'Network Security Group', 'Key Vault': 'Repository for API keys and certificates', 'Customer Lockbox': 'Keeps B2C information secure while investigations take place', 'Security Center': 'A part of portal where all security related issues can be monitored and resolved', 'Sentinel': 'SIEM engine that monitors security incidences', 'Defender': 'A blue team tool for detection of security breaches', 'DDoS Protection': 'Free service that protects your network against disruptive DoS', 'enter For Information Security ': 'An organization that provides default standard benchmarks for network applications and security', 'XDR': 'Security intelligence log', 'SIEM': 'XDR based threat detection', 'SOAR': 'Security orchestration automation and response', 'eDiscovery': 'The process of audit for privacy and compliance reasons'}
dictitle = ('The Zero Trust Model:', 'The Shared Trust Model:', 'Defense in Depth:', 'The CIA Triad:', "Common Threats", 'Basic Encryption:', 'The Azure Trust Portal:', 'Azure tools')
details = (zero_trust_dict, shared_trust_dict, def_in_depth_dict, cia_dict, threats_dict, encrypt_dict, trust_portal_def, tools_dict)
x = 0

for detail in details:
    print(f'**{dictitle[x]}**')
    keys = detail.keys()
    values = detail.values()
    items = detail.items() 
    for key, value in detail.items():
        print(f"{key}: {value}")
        print('')
    x =+ 1
lists = {
    'zero_trust': ['Identities', 'Devices', 'Applications', 'Data', 'Infrastructure'],
    'shared_trust': ['On-Premise', 'IaaS', 'PaaS', 'SaaS'],
    'def_in_depth': ['Physical', 'Identity Access', 'Perimeter', 'Network', 'Compute', 'Data'],
    'cia': ['Confidentiality', 'Integrity', 'Availability'],
    'threats': ['Data Breach', 'Phishing', 'Spear Phishing', 'SQL Injection', 'ID Attack', 'Brute Force', 'Ransomware', 'Malware', 'Disruptive', 'Root Kit', 'Trojan', 'Worm', 'Exploit', 'Exploit Kit'],
    'encrypt': ['Symmetric', 'Asymmetric', 'Key Pair', 'Public Key', 'Private Key', 'Encryption at Rest', 'Encryption in Transit', 'Hashing', 'Salting', 'Signing',],
    'trust_portal': ['Security', 'Privacy', 'Compliance'],
    'privacy': ['Control', 'Transparency', 'Security', 'Strong Legal Protections', 'No Content-based targeting', 'Benefits to You'],
    'compliance': ['Documentation', 'Region', 'Industry', 'Regulation', 'Audit'],
    'ids': ['Administration', 'Authentication', 'Authorization', 'Auditing'],
    'authentication': ['Identity Provider IdP','Single-Sign-On', 'Federation', 'Token', 'Resources'],
    'AD_IdP': ['Users', 'Service Principals', 'Managed Identities', 'Devices', 'Credentials', 'Access Rights', 'Domain Controller DC'],
    'Azure_AD': ['Resources', 'MFA', 'Office 365', 'Tools'],
    'azure_version': ['Free', 'Office 365 Apps', 'P1', 'P2'],
    'user': ['Managed by Azure AD', 'Form Groups', 'B2B', 'B2C', 'Guest User'],
    'service_principal': ['AD ID', 'Application Used', 'ID Permissions', 'Device Permissions'],
    'managed_id': ['System Assigned', 'User Assigned'],
    'device': ['Mobile Device', 'Laptop', 'Desktop', 'Server', 'Printer'],
    'Azure_MFA': ['Password', 'Additional Verification', 'Open Authentication', 'Time-based one time passwords', 'hardware token', 'Passwordless Authentication', 'Biometrics'],
    'tools': ['Active Directory', 'Virtual Network', 'Firewall', 'Network Security Group', 'Key Vault', 'Customer Lockbox', 'Security Center', 'Sentinel', 'Defender', 'DDoS Protection', 'enter For Information Security ', 'XDR', 'SIEM', 'SOAR', 'eDiscovery']
}
print("******Let's build a document outline that will help you understand your network better.-----")
print('zero_trust, shared_trust, def_in_depth, cia, threats , encrypt, trust_portal, privacy, compliance, ids, authentication, AD_IdP, Azure_AD, azure_version, user, service_principal, managed_id, device, Azure_MFA', 'tools')
lista = input('Please name the first list that you would like to use: ')
listb = input('Please name the second list that you would like to use: ')

if lista in lists and listb in lists:
    for item_a in lists[lista]:
        print(item_a)
        for item_b in lists[listb]:
            print('    ' + item_b)
        print()
else:
    print('Invalid list names provided')
