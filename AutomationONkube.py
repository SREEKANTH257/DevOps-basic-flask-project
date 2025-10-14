import subprocess
import requests

# Configuration
namespace = "default"  # Change if using a different namespace
app_label = "flask-app"
app_url = "http://<LOAD_BALANCER_IP_OR_DNS>"  # Replace with your service external URL

def check_pods():
    cmd = f"kubectl get pods -n {namespace} -l app={app_label} -o jsonpath='{{.items[*].status.containerStatuses[*].ready}}'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    all_ready = all(status == "true" for status in result.stdout.split())
    return all_ready

def check_app():
    try:
        response = requests.get(app_url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

if __name__ == "__main__":
    pods_ready = check_pods()
    app_healthy = check_app()

    if pods_ready and app_healthy:
        print("Health Check Passed: All pods ready and app reachable.")
    else:
        print("Health Check Failed:")
        if not pods_ready:
            print("- Some pods are not ready.")
        if not app_healthy:
            print("- Flask app is not reachable or responding with error.")
