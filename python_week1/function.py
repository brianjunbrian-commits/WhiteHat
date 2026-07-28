def check_traffic_status(packet_count):
    if packet_count >= 1000:
        return "High risk"
    elif packet_count >= 400:
        return "Suspicious"
    else:
        return "Normal"

def inspect_hosts(start_host, end_host):
    for host in range(start_host, end_host + 1):
        print("Inspecting host:", host)

def activate_firewall(seconds):
    while seconds >= 1:
        print("Firewall activates in:", seconds)
        seconds = seconds - 1

    print("Firewall activated")

while True:
    print("\n=== Firewall Control Console ===")
    print("1. Check traffic status")
    print("2. Inspect network hosts")
    print("3. Activate firewall")
    print("q. Quit")

    option = input("Enter your options: ")

    if option == "1":
        packet_count = int(input("Enter packet count: "))
        status = check_traffic_status(packet_count)
        print("Traffic status:", status)

    elif option == "2":
        start_host = int(input("Enter first number: "))
        end_host = int(input("Enter second number: "))
        inspect_hosts(start_host, end_host)

    elif option == "3":
        seconds = int(input("Enter seconds: "))
        activate_firewall(seconds)

    elif option == "q":
        print("Firewall console closed")
        break

    else: 
        print("Invalid option")

