class Baby:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.activities = []
        
    def add_activity(self, activity):
        self.activities.append(activity)
        
    def display_activities(self):
        print(f"Activities for {self.name}: ")
        for activity in self.activities:
            print(activity)

class Caregiver:
    def __init__(self, name):
        self.name = name
        
    def take_care_of_baby(self, baby, activity):
        baby.add_activity(activity)
        print(f"{self.name} took care of {baby.name} by {activity}")

def main():
    babies = []
    caregivers = []
    
    while True:
        print("\nBaby Care Management System")
        print("1. Add Baby")
        print("2. Add Caregiver")
        print("3. Take Care of Baby")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter baby's name: ")
            age = input("Enter baby's age: ")
            baby = Baby(name, age)
            babies.append(baby)
            print(f"{name} added to the system.")
            
        elif choice == "2":
            name = input("Enter caregiver's name: ")
            caregiver = Caregiver(name)
            caregivers.append(caregiver)
            print(f"{name} added to the system.")
            
        elif choice == "3":
            if not babies:
                print("No babies registered yet.")
                continue
            if not caregivers:
                print("No caregivers registered yet.")
                continue
            
            print("Select a baby: ")
            for i, baby in enumerate(babies):
                print(f"{i + 1}. {baby.name}")
                
            try:
                baby_index = int(input("Enter baby's number: ")) - 1
                if baby_index < 0 or baby_index >= len(babies):
                    print("Invalid baby number. Please try again.")
                    continue
                selected_baby = babies[baby_index]
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            print("Select a caregiver: ")
            for i, caregiver in enumerate(caregivers):
                print(f"{i + 1}. {caregiver.name}")
                
            try:
                caregiver_index = int(input("Enter caregiver's number: ")) - 1
                if caregiver_index < 0 or caregiver_index >= len(caregivers):
                    print("Invalid caregiver number. Please try again.")
                    continue
                selected_caregiver = caregivers[caregiver_index]
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            activity = input("Enter activity: ")
            selected_caregiver.take_care_of_baby(selected_baby, activity)
            
        elif choice == "4":
            print("Exiting the Baby Care Management System.")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
