import subprocess

# Define the DNS servers to test
dns_servers = {
    "Google": "8.8.8.8",
    "Cloudflare": "1.1.1.1",
    "OpenDNS": "208.67.222.222",
    "Quad9": "9.9.9.9",
    "Comodo": "8.26.56.26",
}

def ping_server(server_ip):
    try:
        # Ping the server (4 packets, 1-second timeout)
        result = subprocess.run(
            ["ping", "-c", "4", "-W", "1", server_ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        
        # Process the output line by line
        for line in result.stdout.splitlines():
            if "round-trip" in line:  # Find the line containing latency info
                parts = line.split("=")[-1].strip().split("/")  # Split by '=' and '/'
                avg_latency = float(parts[1])  # The average is the second value
                return avg_latency
        return None  # Latency not found
    except Exception as e:
        print(f"Error pinging {server_ip}: {e}")
        return None

# Test each DNS server and store the latencies
latencies = []
for name, ip in dns_servers.items():
    print(f"Pinging {name} ({ip})...")
    latency = ping_server(ip)
    if latency is not None:
        latencies.append((name, ip, latency))
    else:
        print(f"Failed to get latency for {name} ({ip}).")

# Sort the servers by latency
latencies.sort(key=lambda x: x[2])

# Print the results
print("\nDNS Server Latencies (in ms):")
for name, ip, latency in latencies:
    print(f"{name} ({ip}): {latency:.2f} ms")
