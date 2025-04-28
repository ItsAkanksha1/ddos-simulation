# DDoS Simulation Project

This project simulates a basic **Distributed Denial of Service (DDoS)** attack on a target server using Python. It creates multiple threads to send HTTP requests to the target, simulating a high volume of traffic. This script is intended for educational purposes only and should be used in controlled environments with permission.

## Requirements

- **Python 3.x**
- **Kali Linux** (or any Linux distribution)
- **VS Code** (optional but recommended)
- **Virtual Environment** (recommended for isolating dependencies)

## Setup

### 1. Clone this repository (if applicable)

```bash
git clone https://github.com/yourusername/ddos-simulation.git
cd ddos-simulation
```

### 2. Install required Python packages

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the necessary dependencies (if any, otherwise proceed with the script):

```bash
pip install -r requirements.txt
```

### 3. Set up the script

Modify the script to specify the target IP address and port:

```python
target = '223.235.184.7'  # Change to your target IP
port = 80  # Set the target port, default HTTP is 80
fake_ip = '182.162.20.32'  # You can change this to simulate traffic from another IP
```

### 4. Run the simulation

Execute the script:

```bash
python ddos_simulation.py
```

The script will start multiple threads to simulate the DDoS attack.

### 5. Stopping the Attack

You can stop the attack by simply **pressing `CTRL+C`** in your terminal.

## Code Explanation

- **Socket Connection**: The script creates socket connections to the target using `socket.socket()`.
- **HTTP Requests**: It sends HTTP `GET` requests to the target server to simulate traffic.
- **Threading**: Multiple threads are created to simulate a high volume of requests from different sources.
  
## Legal Disclaimer

This script is intended **only for educational purposes** and should not be used to attack unauthorized servers. Running DDoS attacks on any server without permission is **illegal** and may lead to serious legal consequences. Always ensure you have explicit permission from the server owner before conducting any tests.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.
