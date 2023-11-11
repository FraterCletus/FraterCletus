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


zero_trust_dict = {'Identities': 'A user or device on the network.', 'Devices': 'Hardware assets such as a Mobile Phone, Tablet, Laptop, Desktop, Server or Printer.', 'Applications': 'Software used to process data into more complex or simple documents', 'Data': 'Information represented as a text object', 'Infrastructure': 'Configurations and controls of a network'}
shared_trust_dict = {'On-Premise': 'Managed on site', 'IaaS': 'Networking, Storage, Servers, Virtualization', 'PaaS': 'Operating System, Middleware, Runtime', 'SaaS': 'Data, Applications'}
def_in_depth_dict = {'Physical': 'Physical building security and controlling access to computing hardware within the data center is the first line of defense.', 'Identity Access': 'SSO and MFA', 'Perimeter': 'DDoS and Firewall protection', 'Network': 'Inbound/outbound restrictions and load balancers', 'Compute': 'Secure access to and between VMs', 'Data': 'Valued information'}
cia_dict = {'Confidentiality': 'Information is not for public use', 'Integrity': 'Information is accurately kept', 'Availability': 'Information can be accessed as required on secure platform'}
threats_dict = {'Data Breach': 'Any Data Security Violation', 'Phishing': 'A socially engineered attack designed to get information from someone, usually a scam', 'Spear Phishing': 'Phishing attack directed towards a specific person', 'SQL Injection': 'Code injection to tamper with security or data held in a database', 'ID Attack': 'A breach of ID credentials', 'Brute Force': 'An attack where a list of possible passwords is tested on a specific device', 'Ransomware': 'Malware designed to extort funds or favors from victim', 'Malware': 'Malicious software that is installed onto a device for the benefit of the attacker', 'Disruptive': 'Action designed to disrupt access or normal function of an application or network DDoS', 'Root Kit': 'A collection of software designed to enable access to a network or computer ShadowBrokers!', 'Trojan': 'Malware disguised as software that is designed to bypass user ', 'Worm': 'A malware desiged to replicate itself and be sent to other computers', 'Exploit': 'A chunk of code or data software used to exploit any software', 'Exploit Kit': 'A tool kit of exploits used in conjunction and usually in PHP'}
encrypt_dict = {'Symmetric': 'An algorithm in cryptography that uses a shared secret between sender and receiver', 'Asymmetric': 'An algorithm that uses a public and private key pairs', 'Key Pair': 'Separate keys to encrypt+public and decrypt+private information', 'Public Key': 'Message encryption permissions', 'Private Key': 'Message decryption permissions', 'Encryption at Rest': 'Information is not available on database without private key', 'Encryption in Transit': 'Information being transferred is not available without a private key', 'Hashing': 'Takes a string of any length as input and produce a fixed-length hash value. ', 'Salting': 'A random string used to verify validity of message in transit in conjunction with hashing', 'Signing': 'Mathematical verification of authenticity'}
trust_portal_def = {'Security': "['Administration', 'Authentication', 'Authorization', 'Auditing']", 'Privacy': "['Control', 'Transparency', 'Security', 'Strong Legal Protections', 'No Content-based targeting', 'Benefits to You']", 'Compliance': "['Documentation', 'Region', 'Industry', 'Regulation', 'Audit']"}
print('The Zero Trust Model:')
print(zero_trust_dict)
print('The Shared Trust Model:')
print(shared_trust_dict)
print('Defense in Depth:')
print(def_in_depth_dict)
print('The CIA Triad:')
print(cia_dict)
print('Threats to your network')
print(threats_dict)
print('Basic Encryption:')
print(encrypt_dict)
print('The Azure Trust Portal:')
print(trust_portal_def)
print()
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
}

print('zero_trust, shared_trust, def_in_depth, cia, threats , encrypt, trust_portal, privacy, compliance, ids, authentication, AD_IdP, Azure_AD, azure_version, user, service_principal, managed_id, device, Azure_MFA')
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
print('zero_trust, shared_trust, def_in_depth, cia, threats , encrypt, trust_portal, privacy, compliance, ids, authentication, AD_IdP, Azure_AD, azure_version, user, service_principal, managed_id, device, Azure_MFA')
print('Feel free to reference more dictionaries as needed by usint print() function')
