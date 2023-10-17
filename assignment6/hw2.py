hosts = []
try:
    with open("mbox.txt", 'r') as file:
        for line in file:
            if line.startswith("From:"):
                email = line.split()[1]
                parts = email.split('@')
                if len(parts) == 2:
                    host_name = parts[1]
                    hosts.append(host_name)

except FileNotFoundError:
    print("Error: The 'mbox.txt' file does not exist.")
for host in hosts:
    print(host)
total_hosts = len(hosts)
print(f"Total {total_hosts} hosts printed ")


-------------------------------------------------------------------------
# I didn’t fully understand the condition of the assignment2, so I made two options at once


hosts = set()
with open("mbox.txt", "r") as file:
  for line in file:
    if line.startswith("From:"):
      email = line.split()[1]
      host = email.split("@")[1]
      hosts.add(host)
      
for host in hosts:
  print(host)

print(f"Total {len(hosts)} hosts printed")
