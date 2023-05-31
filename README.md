# PacamaraScan

![8-3d1CFxyN8qw3enw](https://github.com/Pacamaraprogress/PACAMARA/assets/97394243/d8508a3c-7765-4d99-804f-af69b0c9ac5c)

PacamaraScan is a lightweight and efficient Python-based network scanner. Named after the robust and resilient Pacamara coffee variety, our tool aims to bring the same spirit to the cybersecurity world. Just as the Pacamara coffee bean is known for its unique size and extraordinary flavor profile, PacamaraScan stands out in the cybersecurity landscape for its ease of use, efficiency, and adaptability.

## Introduction

In the vast, ever-changing landscape of cybersecurity, quick and reliable tools are essential. PacamaraScan is a tool designed to assist cybersecurity professionals in assessing network security and host availability. It efficiently scans for open ports, allowing users to identify potential vulnerabilities in their network setup.

## Features

- **Network Scanning**: PacamaraScan can identify whether a particular host is up and which ports are open on that host. This feature is useful for checking the availability of services on a network and identifying potential security vulnerabilities.

- **Flexibility**: Users can specify which ports to scan, allowing for flexibility in meeting specific use cases.

- **Ease of Use**: Written in Python, PacamaraScan is designed to be straightforward to use, with clear output and simple command-line usage.

## Usage

```python
target_host = "example.com" # Domain only
common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 443, 445, 1433, 1521, 3306, 3389]
is_host_up(target_host, common_ports)

