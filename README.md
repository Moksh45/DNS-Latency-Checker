# DNS Latency Checker

This Python script measures the latency of the top 5 popular DNS servers by sending ICMP ping requests and sorts them in ascending order of latency.

![Visitor Badge](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/moksh45/dns-latency-checker&title=Visitors)

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
   git clone https://github.com/moksh45/dns-latency-checker.git
   cd dns-latency-checker
   ```

2. Run the script:
   ```bash
   python dns_latency_checker.py
   ```

3. The output will display the DNS servers sorted by their average latency in milliseconds:
   ```
   DNS Server Latencies (in ms):
   Cloudflare (1.1.1.1): 12.45 ms
   Google (8.8.8.8): 14.67 ms
   Quad9 (9.9.9.9): 18.34 ms
   OpenDNS (208.67.222.222): 20.56 ms
   Comodo (8.26.56.26): 25.78 ms
   ```

## DNS Servers Tested
- **Google Public DNS**: `8.8.8.8`
- **Cloudflare DNS**: `1.1.1.1`
- **OpenDNS**: `208.67.222.222`
- **Quad9 DNS**: `9.9.9.9`
- **Comodo Secure DNS**: `8.26.56.26`

## Notes
- The script uses the `ping` command to test latency. Ensure you have the necessary permissions to execute it.
- The script has been tested on Linux and macOS. For Windows, minor adjustments may be required.

## License
This project is licensed under the MIT License.

Let me know if you need help with any of the steps!
