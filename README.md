# TransplantNet
### A Distributed Organ Matching and Allocation System

## About

Organ transplantation faces a shortage of available organs and requires effective coordination to identify suitable recipients and arrange timely delivery (Ashlagi & Roth, 2026). TransplantNet will address this coordination challenge through a Python-based distributed application that simulates organ registration, recipient matching, and notifications. The system will use a client-server architecture with Remote Procedure Calls (RPC) through RPyC, multithreading to handle concurrent client requests, and a publish-subscribe mechanism to notify hospitals when potentially compatible organs become available. A greedy matching algorithm will identify potential matches based on organ type, blood type compatibility, and recipient urgency.

## System Architecture

- **Central Server:** Manages organ inventory, recipient requests, matching, and notifications.
- **Harvest Center Client:** Registers available organs with the central server.
- **Hospital Client:** Submits recipient requests and receives matching notifications.
