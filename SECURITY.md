Security Policy
We take the security of the NOVEYA FDL API and all related services very seriously. This policy outlines the practices we follow to safeguard the system and data, and provides guidance for responsible disclosure of potential security vulnerabilities.
Secure Development Practices
1.	Principle of least privilege: Our systems and services are configured to use the minimal level of access necessary to perform their functions.
2.	Regular dependency updates: We actively monitor and update libraries and frameworks used in our code to mitigate known vulnerabilities.
3.	Code reviews: All changes to production code are peer-reviewed with a focus on security, stability, and compliance with best practices.
4.	Static analysis and linting: Automated tools are used to detect common security issues (such as injection flaws or unsafe function calls) during the development process.
Infrastructure Security
•	Encryption: All communications between clients and our API are protected with TLS encryption.
•	Firewalls and network segmentation: We restrict inbound and outbound network access based on need-to-use principles.
•	Containerization: Service components are containerized to isolate workloads and limit lateral movement in case of compromise.
•	Monitoring and logging: We employ real-time monitoring, intrusion detection, and log aggregation to detect anomalies, performance issues, or unauthorized access attempts.
Access Control
•	Authentication: API access requires API keys or OAuth tokens. Keys are stored securely and should not be shared.
•	Role-based access: Administrative tools and dashboards are restricted to authorized personnel, with roles assigned according to job function.
•	Multi-factor authentication (MFA): MFA is required for all internal administrative accounts.
Vulnerability Management
1.	Patch management: We monitor and promptly apply security patches to operating systems, frameworks, and third-party software.
2.	Penetration testing: Periodic internal and external penetration tests are conducted to identify and remediate potential security issues.
3.	Bug bounty and responsible disclosure: We encourage security researchers to submit vulnerability reports.
Reporting a Vulnerability
If you discover a security vulnerability in our API, please report it responsibly to help us protect our users:
•	Email: security@noveya.com
•	PGP Key: Coming soon. If you need to send sensitive information, please request our PGP key via email.
When reporting a vulnerability, please include:
•	A description of the issue, including steps to reproduce or proof-of-concept code where applicable.
•	Your contact information so we can follow up with any questions.
•	Your public PGP key (if available) so that we can encrypt our communications.
We will acknowledge receipt within three working days and strive to provide a status update within seven days. We request that you do not publicly disclose the vulnerability until we have verified and resolved it.
Incident Response
In case of a security incident:
•	We will quickly assess the scope and impact, contain the incident, and mitigate potential damage.
•	Affected users will be notified if personal data is compromised or at high risk of exposure.
•	A post-incident review will be conducted to identify root causes and corrective actions.
Contact
For any questions about this security policy or concerns regarding the security of the NOVEYA FDL API, please contact us at:
security@noveya.com
________________________________________
