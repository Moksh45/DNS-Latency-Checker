# DNS Latency Checker

This Python script measures the latency of the top 5 popular DNS servers by sending ICMP ping requests and sorts them in ascending order of latency.

## Features
- Pings top DNS servers like Google, Cloudflare, OpenDNS, Quad9, and Comodo.
- Measures the average latency of each DNS server.
- Sorts and displays the servers by latency.

## Requirements
- Python 3.x
- The `ping` command must be available on your system (default on most Linux and macOS systems).

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/dns-latency-checker.git
   cd dns-latency-checker
