# Ping-Scanner
An ping-scanner that use threading. It's really fast. Tested on Linux

## How to use it?
You have to type first 3 octets of IP (e.g. 192.168.1) as argument

Example:
python3 ping-scanner.py 192.168.1
or
python ping-scanner.py 192.168.1

## How does it work?
First it checks if you typed IP address. If no ends program, else program is making for loop in range(1, 255). 
Every iteration is making thread THAT makes ping() function, changes IP (e.g. from 192.168.1.23 to 192.168.1.24).

ping() function code

os.system("ping -c 1 %s | grep '64 bytes' | cut -d' ' -f4 | sed 's/.$//'" % host)

It sends ping (-c 1 means that we want to ping once, by default it pings forever)

" cut -d' ' -f4 " cuts rest of informations (icmp_seq=1 ttl=128 time=1.18 ms)

" sed 's/.$//' " cuts double dot from the end

## Known Bugs
I don't know any bugs.
