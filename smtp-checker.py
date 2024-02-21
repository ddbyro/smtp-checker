import time
import smtplib
import yaml
import datetime
import json

# Function to load configuration from a YAML file
def load_config():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)  # Load the configuration file
    return config  # Return the configuration

# Load the configuration
config = load_config()

# Extract the SMTP server and port from the configuration
smtp_server = config['smtp_server']
smtp_port = config['smtp_port']
sleep_time = config['sleep_time']

# Function to test the reachability of an SMTP server
def test_smtp_server(host, port=25):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = {}
    try:
        server = smtplib.SMTP(host, port)  # Connect to the SMTP server
        server.ehlo()  # Send the EHLO command to the SMTP server
        output = {
            "timestamp": timestamp,
            "message": f'The SMTP server "{smtp_server}" on port "{smtp_port}" is reachable.',
            "error": None
        }
    except Exception as e:
        output = {
            "timestamp": timestamp,
            "message": f'Could not reach the SMTP server - "{smtp_server}" on port "{smtp_port}".',
            "error": str(e)
        }
    finally:
        try:
            server.quit()  # Close the connection to the SMTP server
        except:
            pass  # If the connection is already closed, do nothing
    print(json.dumps(output))  # Print the output as a JSON string

# Infinite loop to continuously test the SMTP server
while True:
    test_smtp_server(smtp_server, smtp_port)  # Test the SMTP server
    time.sleep(sleep_time)  # Wait for sleep_time seconds before testing again