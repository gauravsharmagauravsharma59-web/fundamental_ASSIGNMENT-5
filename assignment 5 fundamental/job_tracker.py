job_list = {}

while True:
    print("\n--- Job Application Tracker ---")
    print("1. Add Job Application")
    print("2. Update Status")
    print("3. Show All Applications")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        company = input("Enter company name: ")
        role = input("Enter job role: ")
        job_list[company] = {"Role": role, "Status": "Applied"}
        print("Application Added Successfully!")

    elif choice == "2":
        company = input("Enter company name to update: ")
        if company in job_list:
            status = input("Enter new status (Interviewed/Selected/Rejected): ")
            job_list[company]["Status"] = status
            print("Status Updated!")
        else:
            print("Record Not Found!")

    elif choice == "3":
        print("\nYour Applications:")
        for company, details in job_list.items():
            print(company, "→", details)

    elif choice == "4":
        print("Thank you for using the Tracker!")
        break

    else:
        print("Invalid Input!")