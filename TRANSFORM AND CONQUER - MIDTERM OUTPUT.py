def min_lateness_schedule(consultations):
    if not consultations:
        return 0
    
    def max_subarray_lateness(consultations, low, mid, high):
        def convert_to_seconds(time):
            return time * 60  # 1 minute = 60 seconds
        
        left = float('inf')
        temp = 0
        for i in range(mid, low - 1, -1):
            lateness = consultations[i][1]
            temp += convert_to_seconds(lateness)
            if temp < left:
                left = temp
        
        right = float('inf')
        temp = 0
        for i in range(mid + 1, high + 1):
            lateness = consultations[i][1]
            temp += convert_to_seconds(lateness)
            if temp < right:
                right = temp
        
        return left + right
    
    def min_lateness_schedule_recursive(consultations, low, high):
        if low == high:
            return consultations[low][1]
        
        mid = (low + high) // 2
        
        return min(min_lateness_schedule_recursive(consultations, low, mid),
                   min_lateness_schedule_recursive(consultations, mid + 1, high),
                   max_subarray_lateness(consultations, low, mid, high))
    
    return min_lateness_schedule_recursive(consultations, 0, len(consultations) - 1)

def get_consultations():
    consultations = []
    
    num_patients = 0
    while True:
        try:
            num_patients = int(input("Enter the number of patients: "))
            break
        except ValueError:
            print("Please enter an integer value for the number of patients.")
    
    for i in range(1, num_patients + 1):
        name = ""
        while not name:
            name = input(f"Enter the name of Patient {i}: ")
            if name.isdigit():
                print("Please enter a valid name (string).")
                name = ""
    
    num_staff = 0
    while True:
        try:
            num_staff = int(input("Enter the number of hospital staff: "))
            break
        except ValueError:
            print("Please enter an integer value for the number of hospital staff.")
    
    for i in range(1, num_staff + 1):
        name = ""
        while not name:
            name = input(f"Enter the name of Staff {i}: ")
            if name.isdigit():
                print("Please enter a valid name (string).")
                name = ""
        
        lateness = 0
        while True:
            try:
                lateness = int(input(f"Enter the lateness duration for {name} (in minutes): "))
                break
            except ValueError:
                print("Please enter an integer value for lateness.")
        
        consultations.append((name, lateness))
    
    return consultations

# Example usage:
consultations = get_consultations()
print("JK Hospital Time Checker")
min_lateness = min_lateness_schedule(consultations)
print("Minimum lateness in schedule:", min_lateness, "minutes")
print("Patient and Staff Consultations:")
for item in consultations:
    print(f"Staff: {item[0]}, Lateness: {item[1]} minutes")
