#!/usr/bin/env python
import socket
import subprocess

def get_hostname():
    return socket.gethostname()

def get_top_10_cpu_processes():
    # Run ps command
    command = "ps -eo user,comm,%cpu --sort=-%cpu | head -n 11"
    output = subprocess.check_output(command, shell=True).decode('utf-8').strip().split("\n")
    process_lines = output[1:]  # Skip the header

    processes = []
    for line in process_lines:
        parts = line.split(None, 2)  # Split into user, command, and CPU
        if len(parts) == 3:
            user, command, cpu = parts
            processes.append({
                "user": user,
                "command": command,
                "cpu": cpu
            })

    return processes

def main():
    # Get hostname
    hostname = get_hostname().split(".")[0]
    
    # Get top 10 processes
    top_processes = get_top_10_cpu_processes()
    
    # Format the output as plain text
    formatted_output = ("{}\n".format(hostname))
    for process in top_processes:
        formatted_output += "{:8} {:15} {}\n".format(process['user'], process['command'], process['cpu'])
    
    # Print the formatted output
    print(formatted_output.strip())

if __name__ == "__main__":
    main()
