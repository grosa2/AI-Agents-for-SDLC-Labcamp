# Task 1 - Log file Analyzer

## What:
Setup a basic agent able to process data from an input document using the code interpreter tool

## How:
- Setup an agent using OpenAI Assistants playground
- Enable the code interpreter tool
- Use the agent to process data from the input document. Specifically:
    - Extract the response time and timestamp of each request
    - Build an anomaly detection model to identify anomalous requests (based on response time)
    - Generate a plot of the response times over time
    - (Optional) Create a descriptive report of the data contained in the dataset


## Dataset Description:
The dataset comes from Kaggle and contains log files from a web server. The logs are in the Apache Common Log Format. The dataset is available at: https://www.kaggle.com/datasets/vishnu0399/server-logs

### Dataset Columns:
- **IP of client**: This refers to the IP address of the client that sent the request to the server.
- **Remote Log Name**: Remote name of the User performing the request. In the majority of the applications, this is confidential information and is hidden or not available.
- **User ID**: The ID of the user performing the request. In the majority of the applications, this is a piece of confidential information and is hidden or not available.
- **Date and Time in UTC format**: The date and time of the request are represented in UTC format as follows: - Day/Month/Year:Hour:Minutes: Seconds +Time-Zone-Correction.
- **Request Type**: The type of request (GET, POST, PUT, DELETE) that the server got. This depends on the operation that the request will do.
- **API**: The API of the website to which the request is related. Example: When a user accesses a carton shopping website, the API comes as /usr/cart.
- **Protocol and Version**: Protocol used for connecting with server and its version.
- **Status Code**: Status code that the server returned for the request. Eg: 404 is sent when a requested resource is not found. 200 is sent when the request was successfully served.
- **Byte**: The amount of data in bytes that was sent back to the client.
- **Referrer**: The websites/source from where the user was directed to the current website. If none it is represented by “-“.
- **UA String**: The user agent string contains details of the browser and the host device (like the name, version, device type etc.).
- **Response Time**: The response time the server took to serve the request. This is the difference between the timestamps when the request was received and when the request was served.
