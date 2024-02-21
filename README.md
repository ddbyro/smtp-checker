# SMTP Checker

The overall function of `smtp-checker.py` is to continuously check the reachability of an SMTP (Simple Mail Transfer Protocol) server.
At a a set interval the service will reach out to the configured server via SMTP using the EHLO command.

#### EHLO (Extended Hello)

 - Same as HELO but tells the server that the client may want to use the Extended SMTP (ESMTP) protocol instead.
EHLO can be used although you will not use any ESMTP command.
And servers that do not offer any additional ESMTP commands will normally at least recognize the EHLO command and reply in a proper way.

#### HELO (Hello)

 - The client sends this command to the SMTP server to identify itself and initiate the SMTP conversation.
   The domain name or IP address of the SMTP client is usually sent as an argument together with the command (e.g. “HELO client.example.com”).
   If a domain name is used as an argument with the HELO command, it must be a fully qualified domain name (also called FQDN).

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)

#### Other Documentation Links
- [Helm Chart Documentation](./chart/README.md)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

## Podman

#### Build Image

```bash
podman build . -t <repository name>/smtp-checker:1.0.0
```

#### Push Image
```bash
podman push <repository name>/smtp-checker:1.0.0
```

## Service Documentation

### Prerequisites

You need Python 3 and pip installed on your machine. You also need the `smtplib` and `yaml` libraries. You can install these with pip:

```bash
pip install pyyaml# smtp-checker
```
# SMTP Checker

This Python script checks the reachability of an SMTP server by connecting to it and sending the EHLO command. If the server is reachable, it prints a success message. If not, it prints an error message.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need Python 3 and pip installed on your machine. You also need the smtplib and yaml libraries. You can install these with pip:

```bash
pip install pyyaml
```

### Installation

1. Clone the repo
    ```bash
    git git@github.com:ddbyro/smtp-checker.git
    ```
2. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```   

## Usage

1. Update the config.yaml file with your SMTP server and port.
2. Run the script:
    ```bash
    python smtp-checker.py
    ```
The script will continuously check the reachability of the SMTP server every 30 seconds and print a message indicating whether the server is reachable or not.

## License

Distributed under the MIT License. See LICENSE for more information.

Please replace the placeholders with the actual content relevant to your project.
