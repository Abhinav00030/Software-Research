class RequisitionSystem:
    counter = 10000

    def __init__(self):
        self.requisitions = []

    def staff_info(self):
        staff_id = input('Enter the staff id: ')
        staff_name = input('Enter the staff name: ')
        date = input('Enter the date (dd/mm/yyyy): ')
        RequisitionSystem.counter += 1
        requisition_id = RequisitionSystem.counter
        return staff_id, staff_name, date, requisition_id

    def requisitions_details(self):
        total_cost = 0
        print("\nEnter requisitions items (name and price). Enter 'done' to stop.")
        while True:
            item_name = input("Enter item name: ")
            if item_name.lower() == "done":
                break
            item_price = float(input("Enter the price of item: "))
            total_cost += item_price
        return total_cost

    def requisition_approval(self, total_cost, staff_id, requisition_id):
        if total_cost < 500:
            status = "Approved"
            approval_ref_number = f"{staff_id}{str(requisition_id)[-3:]}"
        else:
            status = "Pending"
            approval_ref_number = None
        return status, approval_ref_number

    def respond_requisition(self, requisition_id, response):
        for req in self.requisitions:
            if req['requisition_id'] == requisition_id and req['status'] == "Pending":
                req['status'] = response
                if response == "Approved":
                    req['approval_ref_number'] = f"{req['staff_id']}{str(req['requisition_id'])[-3:]}"
                break

    def display_requisitions(self):
        for req in self.requisitions:
            print("\nPrinting Requisition:")
            print(f"Date: {req['date']}")
            print(f"Requisition ID: {req['requisition_id']}")
            print(f"Staff ID: {req['staff_id']}")
            print(f"Staff Name: {req['staff_name']}")
            print(f"Total: ${req['total']:.2f}")
            print(f"Status: {req['status']}")
            if req['approval_ref_number']:
                print(f"Approval Reference Number: {req['approval_ref_number']}")
            else:
                print("Approval Reference Number: Not available")

    def requisition_statistic(self):
        total = len(self.requisitions)
        approved = sum(1 for req in self.requisitions if req['status'] == "Approved")
        pending = sum(1 for req in self.requisitions if req['status'] == "Pending")
        not_approved = sum(1 for req in self.requisitions if req['status'] == "Not approved")
        
        print("\nDisplaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {total}")
        print(f"The total number of approved requisitions: {approved}")
        print(f"The total number of pending requisitions: {pending}")
        print(f"The total number of not approved requisitions: {not_approved}")

    def submit_requisition(self):
        staff_id, staff_name, date, requisition_id = self.staff_info()
        total_cost = self.requisitions_details()
        status, approval_ref_number = self.requisition_approval(total_cost, staff_id, requisition_id)
        
        requisition = {
            'date': date,
            'staff_id': staff_id,
            'staff_name': staff_name,
            'requisition_id': requisition_id,
            'total': total_cost,
            'status': status,
            'approval_ref_number': approval_ref_number
        }
        self.requisitions.append(requisition)

# Test the program
rs = RequisitionSystem()

# Submit 5 requisitions
for _ in range(5):
    rs.submit_requisition()

# Display all requisitions
rs.display_requisitions()

# Display statistics
rs.requisition_statistic()

# Respond to pending requisitions
for req in rs.requisitions:
    if req['status'] == "Pending":
        response = input(f"Respond to requisition {req['requisition_id']} (Approved/Not approved): ")
        rs.respond_requisition(req['requisition_id'], response)

# Display updated requisitions and statistics
rs.display_requisitions()
rs.requisition_statistic()