Miscreants racked up a $64,000 bill on DXC Technologies' tab after a techie accidentally uploaded the outsourcing firm's private AWS key to a public GitHub repo.
It was red faces all round as the business opened up on the classic crypto key fumble in a PDF memo to staff, the contents of which were seen by The Register.
"Various secure variables (cryptographic keys that allowed access to DXC procured Amazon Web Services resources) were hardcoded into a piece of work being shared between multiple teams and with the project architect."
Then on September 27, a member of the technical team created a personal space on the public Github, and the code was loaded to this unsecured repository that allowed individuals as yet unknown to access and use it.
"Over a period of four days, the private keys were used to start 244 AWS virtual machines. The cost incurred was $64k (£48,799)."
DXC's own monitoring tool, Cloud Checker, indicated most of the VMs were stood up within 24 hours of the unwitting publication of the keys. The code was in the public space for less than 24 hours before DXC realised it was "unsecured and removed". So that's fine then.
The cost to rectify – in addition to the AWS bill racked up – was related to "having to change all the variables, username and passwords. Rotate the keys and create secure areas to store these details means the project lost two to four weeks delivery time". The customer project was unspecified.
The remedy involved removing private keys from the repo; all existing keys were recycled and secured; and the code changed to use a vault to "secure... variables needed".
Incredibly, DXC admitted a full probe had revealed some in the team were "not briefed on the compliance standards and have not received adequate security training".
It added: "A security incident exposure matrix was established, security breach possibilities were discussed along with preventative measures put in place."
The cost of time lost due to resource reallocation to work on these corrections and improvements was yet to be calculated in monetary terms. But culturally there was an impact.
"Legacy CSC colleagues lost confidence in our ability as a team to maintain secure information and even complete the work required. This also resulted in difficult interactions between colleagues on calls."
DXC reminded staff they are "one of the first lines of defense" [sic], or at least they are supposed to be. The 12-point list of common-sense advice to the troops is listed below.
- Understand and follow DXC security policies and procedures
- Physically secure your PCs, laptop, USB memory devices, credentials, etc.
- Encrypt sensitive data on all devices and secure them from theft
- Screen-lock your device when you walk away from it
- Use strong passwords; never share or disclose them; create a unique password for each site and application
- Ensure you have approved anti-malware software running on your PC
- Accept PC-COE updates and apply security patches; download only approved software
- Protect sensitive information in all forms
- Use collaboration tools securely
- Be aware of your surroundings and stay alert (El Reg's favourite)
- Report incidents to the Security Incident Response Centre
- Do not post about the company on social media if you are not authorised to do so
For any employees still in doubt, there is always the Safe and Secure video available on DXC's Cyber Security Awareness Month.
DXC refused to comment. ®