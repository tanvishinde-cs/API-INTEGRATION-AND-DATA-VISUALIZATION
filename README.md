# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMAPANY*: CODTECH IT SOLUTIONS

*NAME*: TANVI SHINDE

*INTERN ID*: CTIS1805

*DOMAIN*: Python Programming

*DURATION*: 4 WEEKS

*MENTOR*: Neela Santhosh

# API Integration and Data Visualization – Task Description
The API Integration and Data Visualization task was carried out to understand how external data sources can be integrated into a Python application and how the collected data can be represented visually for better interpretation. This task plays an important role in modern software development, as many real-world applications depend on real-time data fetched from public or private APIs. The objective of this task was to fetch live weather data from a public API and visualize the data using Python libraries.

For this task, Python was used as the primary programming language due to its simplicity, flexibility, and strong support for data handling and visualization. The development was performed using Python IDLE (Python 3.13), which is the default Integrated Development Environment (IDE) that comes bundled with Python. Python IDLE was selected because it is beginner-friendly and suitable for understanding the fundamental concepts of API integration, JSON data processing, and graphical representation of data.

Development Environment and Tools Used

The entire task was implemented on a Windows operating system using Python IDLE as the editor platform. Python IDLE provides a simple interface where Python scripts can be written, executed, and debugged easily. This made it convenient to test the API integration and visualization output step by step.

The following tools and technologies were used during the implementation of this task:

-Programming Language: Python

-Editor / IDE: Python IDLE

-API Used: OpenWeatherMap Public API

-Libraries Used:

urllib.request for sending HTTP requests to the API

json for parsing and handling API responses

matplotlib for creating data visualizations

-Version Control Platform: GitHub

GitHub was used to store the project files, including the Python script, visualization output, and documentation. This ensures that the project is accessible, well-documented, and can be shared easily as part of the internship deliverables.

API Key Configuration and Integration Process

To access data from the OpenWeatherMap API, an API key is required. The API key serves as an authentication token that allows users to securely access the API services. The following steps were followed to generate and use the API key:

1.An account was created on the OpenWeatherMap website.

2.After logging in, a free API key was generated from the user dashboard.

3.The generated API key was copied and stored securely.

4.In the Python script, a variable named API_KEY was created to store the API key.

5.The API key was then appended to the API request URL along with the city name and unit parameters.

This method ensures that the API key can be easily modified or replaced without affecting the core logic of the program. It also follows good coding practices by keeping configuration details separate from application logic.

Data Fetching and Processing

Once the API request URL was constructed, the Python script sent an HTTP request to the OpenWeatherMap API. The API responded with weather data in JSON format, which is commonly used for data exchange due to its lightweight structure and readability. The response included multiple weather parameters such as temperature, humidity, atmospheric pressure, and other related information.

Using Python’s built-in json module, the response data was parsed and specific values were extracted. The extracted weather parameters included:

-Temperature (measured in degrees Celsius)

-Humidity (measured in percentage)

-Atmospheric pressure (measured in hPa)

These values were stored in Python variables for further processing and visualization.

Data Visualization

The Matplotlib library was used to visualize the extracted weather data. A bar chart was created to represent temperature, humidity, and pressure values in a clear and visually understandable format. Data visualization plays a key role in converting raw numerical data into meaningful insights. The graph included proper labels, a title, and well-defined axes, making the output easy to interpret.

This visualization acts as a simple dashboard that allows users to quickly analyze weather conditions for a selected city.

Applications and Use Cases

The concepts implemented in this task have wide real-world applications, including:

-Weather monitoring systems

-Data analytics and reporting dashboards

-Smart city and IoT-based applications

-Educational and research projects

-Business intelligence tools

API integration and data visualization are widely used in industries such as software development, data science, healthcare, finance, and environmental monitoring.

*Conclusion*:

In conclusion, this task successfully demonstrates the use of Python for API integration and data visualization. By using Python IDLE, OpenWeatherMap API, and Matplotlib, real-time data was fetched, processed, and visualized effectively. This task helped in developing practical skills related to API handling, data processing, and visualization, which are essential for modern software and data-driven applications.
