# Nmap NSE Scripts Cheat Sheet

## Introduction
This cheat sheet provides a quick reference to various Nmap NSE scripts, helping users effectively utilize Nmap in their security assessments and audits.

## Installation
To install Nmap and its NSE scripts, follow the installation instructions on the official Nmap website.

## Common Scripts
Here is a list of commonly used Nmap NSE scripts:

- **http-enum**: Enumerates directories and files on web servers.
- **smb-vuln-ms17-010**: Checks for the EternalBlue vulnerability.
- **dns-brute**: Performs brute force DNS enumeration.

## Usage Examples
- To scan a target with the http-enum script:
  ```bash
  nmap --script http-enum <target>
  ```

- To scan for SMB vulnerabilities:
  ```bash
  nmap --script smb-vuln-ms17-010 <target>
  ```

## Conclusion
This cheat sheet is continually updated, so please check back for the latest scripts and usage examples.