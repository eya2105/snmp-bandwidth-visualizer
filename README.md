# SNMP Bandwidth Monitor

This project is a simple SNMP-based bandwidth monitoring tool implemented in Python using the `pysnmp` library. It uses the `ifInOctets` SNMP OID to calculate inbound bandwidth (in bits per second) on a given interface of a local SNMP agent.

## Features

- Interrogates SNMP agent using SNMPv1 protocol
- Measures incoming traffic on a specific interface (default: index 22)
- Live real-time plotting with `matplotlib`
- Logs bandwidth data to a file `debit.txt`

---

## Requirements

- Python **3.9.13**
- Virtual environment named `snmp-env` (recommended)
- **ManageEngine MIB Browser** (used to inspect/check SNMP OIDs)
- SNMP agent running locally (e.g., `snmpd` or Windows SNMP service)

---

## Requirements
pysnmp
pysnmp-apps
pyasn1
matplotlib
time

---

## Notes
You can adjust the SNMP interface index in get_octets(interface_index=22)

If using ManageEngine MIB Browser, ensure:

The SNMP agent is running and reachable

OIDs are valid and walkable in the browser

Run this script while your SNMP agent is generating traffic




