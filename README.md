# vehicle_simulation


## Hypothesis ##
Does the use of secure, multi-factor authentication (MFA) in a distributed communication network reduce the risk of unauthorized access compared to centralized authentication models in IoT-enabled smart vehicle systems?
## Overview ##
This project simulates communication between IoT-enabled smart vehicles using multi-factor authentication (MFA) to enhance security. It aims to compare distributed MFA models with centralized authentication, focusing on their ability to prevent unauthorized access within a network of smart vehicles.

## Objective ##
The primary goal is to determine if distributed MFA provides better protection than centralized models. The simulation tests whether distributing authentication responsibilities across multiple vehicles reduces vulnerabilities compared to relying on a single central hub.

## Program Simulation ##
The simulation involves multiple vehicles attempting to connect to a network either through a central hub or by authenticating with other vehicles directly. Each vehicle in the simulation has a unique ID, password, and digital certificate, which are used for MFA. 

The central hub manages connections, but for specific cases like Vehicle V20, the hub will be busy, forcing the vehicle to connect with another already-connected vehicle in the network. This simulates real-world scenarios where hubs may face congestion or targeted attacks. 

The program handles authentication processes for both centralized and distributed models:
Centralized Mode: Vehicles first attempt to authenticate through the central hub. If successful, they gain access to the network.
Distributed MFA Model: Vehicles authenticate with each other by verifying both passwords and certificates. The simulation shows whether MFA can enhance security by requiring successful verification on multiple factors before a connection is established.

## Simulation Structure ##
The program is structured into four main modules:
1. **Vehicle Module (`vehicle.py`)**: This module defines the attributes of each vehicle, including its ID, password, and certificate.
2. **Controller Module (`controller.py`)**: It manages the central hub's behavior, simulating scenarios where the hub can be busy and redirecting connections to other vehicles.
3. **Database Module (`database.py`)**: This module maintains a list of all vehicles, storing their credentials and connection status.
4. **Network Simulation Module (`network_simulation.py`)**: This module handles the simulation of connection attempts, authentication processes, and the redirection of vehicles to other nodes if needed.

## Evaluation Metrics ##
The program uses three key metrics to compare authentication models:
1. Unauthorized Access Attempts: Measures the success rate of authentication attempts in centralized vs. distributed models.
2. Attack Impact: Assesses how a breach at a single point (like the hub) affects the network compared to a breach in a distributed system.
3. System Latency: Compares how long it takes for vehicles to authenticate and connect in centralized versus distributed models.

## Installation and Requirements ##
To run the simulation, you need:
- **Python 3.x** installed
- Required libraries such as `random` for simulating connections

Clone the repository, navigate to the project directory, and run `network_simulation.py` to start the simulation.

## Limitations ##
While distributed MFA increases security, it also introduces computational overhead and potential latency during authentication, impacting system performance in real-time environments. Additionally, sensitive data exchanged during authentication is not encrypted due to word limitations within this simulation. Encryption of sensitive data should be implemented in a practical deployment to ensure full security.

## Conclusion ##
The simulation demonstrates that distributed MFA enhances the security of IoT-enabled smart vehicle networks compared to centralized models. It decentralizes the authentication process, thereby reducing single points of failure and improving overall network resilience. However, this approach may increase latency, which requires further optimization for practical deployment.


