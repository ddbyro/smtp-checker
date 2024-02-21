import time
import smtplib
import yaml

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

# Function to test the reachability of an SMTP server
def test_smtp_server(host, port=25):
    try:
        server = smtplib.SMTP(host, port)  # Connect to the SMTP server
        server.ehlo()  # Send the EHLO command to the SMTP server
        print(f'The SMTP server "{smtp_server}" on port "{smtp_port}" is reachable.')  # Print a success message
    except Exception as e:
        print(f'Could not reach the SMTP server - "{smtp_server}" on port "{smtp_port}".')  # Print an error message
        print("Error:", e)  # Print the exception
    finally:
        try:
            server.quit()  # Close the connection to the SMTP server
        except:
            pass  # If the connection is already closed, do nothing

# Infinite loop to continuously test the SMTP server
while True:
    test_smtp_server(smtp_server, smtp_port)  # Test the SMTP server
    time.sleep(30)  # Wait for 30 seconds before testing again