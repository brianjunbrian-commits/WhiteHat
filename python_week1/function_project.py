def analyze_threat_level(detected_threats):
    if detected_threats >= 8:
        return "Critical"
    elif detected_threats >= 4:
        return "Dangerous"
    elif detected_threats >= 1:
        return "Suspicious"
    else: 
        return "Clean"

def review_event_id(start_event, end_event):
    for event in range(start_event, end_event + 1):
        print("Reviewing event", event)

def start_isolation_countdown(seconds):
    while seconds >= 1:
        print("System isolation in:", seconds)
        seconds = seconds - 1

    print("System isolated")

while True:
    print("\n=== Threat Monitoring Console ===")
    print("1. Analyze threat level")
    print("2. Review event IDs")
    print("3. Start isolation countdown")
    print("q. Quit")

    option = input("Enter your operator: ")

    if option == "1":
        detected_threats = int(input("Enter your threats: "))
        status = analyze_threat_level(detected_threats)
        print("Threat level:", status)

    elif option == "2":
        start_event = int(input("Enter first event: "))
        end_event = int(input("Enter second event: "))
        review_event_id(start_event, end_event)

    elif option == "3":
        seconds = int(input("Enter your seconds: "))
        start_isolation_countdown(seconds)

    elif option == "q":
        print("Threat console closed")
        break

    else:
        print("Invalid option")
        
        