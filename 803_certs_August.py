#!/bin/python3


aug23_cert = {
    "080323": "Fundamentals of Red Hat Enterprise Linux",
    "Red Hat": "PEJEPJJYUGN9 | https://coursera.org/share/70bc20912b5979c37630a9890bf3a995",

    "081323": "Linux System Administration w/ IBM Power Systems",
    "Red.Hat": "8XZ63BNMAEA2 | https://coursera.org/share/6318eec2fc18061d9f88d2e2cf41c02f",

    "RedHat": "Private Cloud Mgmt on IBM power sytems",
    "a?-": " | ",

    "082023": "Network Security Fundamentals",
    "Palo Alto": " | ",

    "081423": "Machine Learning Operations MLOps -limited event",
    "Microsoft": "badge | event071723-081423 at learn.microsoft.com",

}

for aa, bb in aug23_cert.items():
    print("{}: {}".format(aa, bb))

print("\n<----------------->")


"""
Linux and Private Cloud Administration on IBM Power Systems Specialization
    |-----> Fundamentals of Red Hat Enterprise Linux            # 080323' 
    |-----> Linux System Administration w/ IBM Power Systems    # 081323'
    |_____> Private Cloud Management on IBM Power Systems       # X
"""
