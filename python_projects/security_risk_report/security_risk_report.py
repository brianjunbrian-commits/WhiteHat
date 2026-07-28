def risk_score(failed_login_attempts, open_ports, malware_alerts):
    login_score = failed_login_attempts * 2
    port_score = open_ports
    malware_score = malware_alerts * 5

    total_score = login_score + port_score + malware_score
    return total_score

def risk_level(score):
    if score >= 30:
        return "Critical"
    elif score >= 15:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"

def event_review(start_event, end_event):
    for event in range(start_event, end_event + 1):
        print("Reviewing event", event)

def response_countdown(seconds):
    while seconds >= 1:
        print("Response begins in:", seconds)
        seconds = seconds - 1

    print("Incident response started")

failed_logins = int(input("Failed login attempts: "))
open_ports = int(input("Open ports: "))
malware_alerts = int(input("Malware alerts: "))

print("\n=== Security Risk Report ===")

score = risk_score(failed_logins, open_ports, malware_alerts)
print("Risk score:", score)

level = risk_level(score)
print("Risk level", level)

start_event = int(input("Enter the start event: "))
end_event = int(input("Enter the end event: "))
event_review(start_event, end_event)

seconds = int(input("Enter countdown seconds: "))
response_countdown(seconds)


