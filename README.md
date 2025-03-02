# 🌐 WHOIS Lookup Tool - The Ultimate Domain & IP Information Retriever

🚀 **Live Demo:** [Coming Soon]\
📂 **Deploy Your Own Instance** using Python & Docker

## 💀 Overview

The **WHOIS Lookup Tool** is a **powerful, efficient, and user-friendly** Python-based utility designed for retrieving **detailed domain and IP registration information**. Whether you're a **security researcher, system administrator, or domain enthusiast**, this tool provides essential insights into domain ownership, status, and geolocation details.

✔️ **WHOIS Record Lookup** - Fetch domain/IP ownership and registrar details\
✔️ **Geolocation Data** - Identify country, ASN, and ISP of an IP address\
✔️ **Domain Availability Check** - Instantly verify if a domain is available for registration\
✔️ **Formatted Output** - Displays results in a structured and easy-to-read format\
✔️ **Fast & Lightweight** - Minimal dependencies ensure quick execution\
✔️ **Error Handling** - Intelligent mechanisms to manage rate limits and invalid lookups

## 🌟 Key Features

- 🔍 **WHOIS Lookup:** Retrieve domain/IP registration details and owner information.
- 🌎 **Geolocation Information:** Identify the country, region, and ASN of an IP address.
- 🏠 **Domain Availability Check:** Verify if a domain is available for registration.
- 👑 **Formatted Data Output:** Displays results in a well-structured table format.
- ⚡ **Fast & Lightweight:** Minimal dependencies for quick lookups.
- 🚦 **Rate Limit Handling:** Prevents excessive queries with intelligent error handling.
- 🛡️ **Dependency Checks:** Ensures the `whois` command is installed before execution.
- 🖥️ **Command-Line Tool:** Run directly from the terminal with ease.

## 🎨 Additional Features

- 🌗 **Dark Mode Support:** Optimized for both light and dark terminal themes.
- 📋 **Log File Support:** Save WHOIS lookup results for future reference.
- 🛠️ **Custom WHOIS Servers:** Ability to query different WHOIS servers.
- 🌍 **Multi-language Support:** Future plans for translations in multiple languages.

## 🛠️ Installation

### **Python Setup**

Ensure you have Python installed, then:

```bash
git clone https://github.com/YOUR_USERNAME/whois-lookup-tool.git
cd whois-lookup-tool
pip install -r r
```

### requirements.txt**Docker Deployment**

Deploy via Docker with:

```bash
docker run -d -p 8080:8080 --name whois-lookup YOUR_DOCKER_IMAGE
```

## ⚙️ Usage

Run the script with a domain name or IP address as an argument:

```bash
python whois_lookup.py example.com
```

### Example Output:

```
=============================================
        WHOIS Lookup Tool
        Version: v-1.3
        Owner: Yash Tiwari
=============================================
[*] Performing WHOIS lookup for domain: example.com

+---------------------+----------------------------------------------------+
| Key                | Value                                              |
+---------------------+----------------------------------------------------+
| Domain Name        | EXAMPLE.COM                                        |
| Registry Domain ID | 1234567_DOMAIN_COM-VRSN                            |
| Registrar WHOIS    | whois.example-registrar.com                        |
| Registrar URL      | http://www.example-registrar.com                   |
| Updated Date       | 2024-08-02T02:17:33+0000                           |
| Creation Date      | 2020-05-10                                         |
| Expiry Date        | 2025-05-10                                         |
| Registrar         | Example Registrar Inc.                              |
| Registrar IANA ID  | 292                                               |
| Name Servers       | ns1.example.com, ns2.example.com                  |
| Domain Status      | active                                            |
| DNSSEC            | unsigned                                          |
+---------------------+----------------------------------------------------+

[*] WHOIS lookup completed.
```

## 🛠️ Advanced Configuration

Customize features using environment variables:

| Variable              | Default | Description                               |
| --------------------- | ------- | ----------------------------------------- |
| `WHOIS_TIMEOUT`       | `30s`   | Max time to wait for a WHOIS response.    |
| `WHOIS_SERVER`        | `auto`  | Specify a custom WHOIS server.            |
| `LOG_FILE_PATH`       | `logs/` | Path to store lookup results.             |
| `SECURITY_RATE_LIMIT` | `0`     | Restrict queries per hour (0 = no limit). |

Example usage in Docker:

```bash
docker run -d -p 8080:8080 \
  -e WHOIS_TIMEOUT=30s \
  -e WHOIS_SERVER="whois.verisign-grs.com" \
  --name whois-lookup \
  YOUR_DOCKER_IMAGE
```

## 🤖 AI-Assisted Development

With **version 2.0**, AI-assisted coding helped improve error handling and output formatting. By **version 3.0+,** AI assistance was optimized to streamline performance and enhance usability.

## ⭐ Future Enhancements

🔹 API Integration for WHOIS lookups (e.g., `whoisxmlapi`).\
🔹 Multi-threaded lookups for bulk domain analysis.\
🔹 Web-based interface for easier use.\
🔹 Browser extension for quick WHOIS lookups.

---

📌 **Like this project?** Give it a ⭐ on GitHub!\
👣 **Suggestions?** Open an issue or contribute!\
📨 **Follow for updates!** [GitHub](https://github.com/hackerattack99)

