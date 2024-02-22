## Increasing Open Files Limit for Web Stack Debugging 🚀

### Description

This repository contains scripts to increase the limit of open files per user in a web stack environment. This is particularly useful for debugging purposes when dealing with a large number of files open simultaneously.

### Instructions

To increase the open files limit, follow the steps below:

1. **Fix for Nginx:**
   - Execute the following command:
     ```
     sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 15000\"/" /etc/default/nginx; sudo service nginx restart
     ```
2. **Change OS Configuration for User:**
   - Execute the following command:
     ```
     sudo sed -i "s/hard nofile 5/hard nofile 50000/" /etc/security/limits.conf; sudo sed -i "s/soft nofile 4/soft nofile 40000/" /etc/security/limits.conf
     ```

### Notes

- Ensure you have necessary permissions to execute these commands.
- Restart services (e.g., Nginx) after applying changes.
- The provided values (15000, 50000, 40000) can be adjusted based on your specific requirements.
- Be cautious while modifying system configurations.

### Author

Aymane Sadiki
