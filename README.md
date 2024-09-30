# Traktor-social-net
A social network with intentional vulnerabilities

This project is an entry to HackAtom 2024 hackathon by team Traktor

## Docs
- .env file contains password for admin panel
- /traktor_sn/posts/views.py get_image view uses unsanitized user input which makes path traversal vuln possible
