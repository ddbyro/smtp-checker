import time
import smtplib
import yaml

def load_config():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config

config = load_config()
smtp_server = config['smtp_server']
smtp_port = config['smtp_port']

def test_smtp_server(host, port=25):
    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        print(f'The SMTP server "{smtp_server}" on port "{smtp_port}" is reachable.')
    except Exception as e:
        print(f'Could not reach the SMTP server - "{smtp_server}" on port "{smtp_port}".')
        print("Error:", e)
    finally:
        try:
            server.quit()
        except:
            pass

while True:
    test_smtp_server(smtp_server, smtp_port)
    time.sleep(30)  # Wait for 5 minutes