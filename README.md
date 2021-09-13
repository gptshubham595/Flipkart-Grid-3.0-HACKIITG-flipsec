# HACKIITG

- Asset discovery and monitoring tool 

## PROBLEM 

- Network Scanning Porbe Tool 

## SOLUTION
- Using python and Linux packages developed a scanning probe that scans over a remote subnet and local network while detecting open ports, IPs, DNS information and displayed using Kibana from ELK Stack

## VIDEO

[![Watch the video](https://img.youtube.com/vi/Im2FVyLLxZ0/maxresdefault.jpg)](https://youtu.be/Im2FVyLLxZ0)


3 CSV's are generated

## SUBDOMAIN.CSV

| Source        | Subdomain     | http/https   | DNS RESOLUTION/IP(CLICKABLE)|
| ------------- |:-------------:| ------------:| ---------------------------:|


## TOPOLOGY.CSV

| HopNo         | RT1           | RT2   | RT3 | IP ADDRESS (CLICKABLE)|
| ------------- |:-------------:| -----:|:---:| ---------------------:|
| 10            |     81ms      |  74ms | 74ms|    127.0.0.1          |

## NMAP.CSV

nmap.nmap_version_detection("your-host.com")

nmap.nmap_os_detection("192.168.178.2") # MOST BE ROOT

accuracy Name osclass_osfamily osclass_osgen osclass_vendor CPE  PORT  PROTOCOL  service_conf service_extrainfo service_method service_name service_ostype service_product service_version



