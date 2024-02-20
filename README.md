# Data Processing API

This project is a backend application implemented in Python, utilizing Flask as the web framework. The primary goal is to process data from a provided JSON file representing assets, energy demands, energy outputs, energy systems, and their relationships. The application exposes an API endpoint to retrieve processed data based on specific queries.

## Table of Contents
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Key Features](#key-features)
- [Documentation](#documentation)
- [Error Handling](#error-handling)
- [License](#license)

## Project Structure

The project is organized into several modules to enhance modularity and maintainability:

- **app.py:** The main application file containing the Flask web framework setup, API endpoint definition, and execution logic.
  
- **processor.py:** Defines the `EnergyProcessor` class responsible for calculating energy-related metrics, including reduced energy demand.

- **data.py:** Implements the `DataAccessObject` class, handling the loading and structuring of data from the provided JSON file.

- **templates/index.html:** HTML Front-end to display processed data.

- **json_database.json:** Sample JSON data file

- **README.md:** This documentation file

- **requirements.txt:** File listing required libraries

## Requirements
### Software:
- Python 3.8+
- Flask - Since it's a small and rather simple project, the chosen framework was Flask due to being lightweight, fast and flexible

### Libraries:
 - Flask 
- json
- logging
### Data:
 - JSON file representing assets, energy demands, outputs, and systems (example provided in data.json)
### Hardware:
 - Any computer with the above software installed


## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/henriqueleote/Data-Processing-API.git

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

3. Navigate to the project directory:
   ```bash
   cd Data-Processing-API

## Usage

 - Ensure you have Python installed on your machine.
 - Follow the installation steps mentioned above.
 - Run the application:

   ```bash
   python app.py

- Open in browser the route in console (Example: http://127.0.0.1:5000/asset/2)

## API Endpoint

 - The API endpoint is defined as follows:

   ```bash
   GET /asset/<int:asset_id>
   
This endpoint retrieves processed energy data for a specific asset based on its ID. The response is in JSON format, containing the asset's name, energy types, total energy demand, and energy output reduction.

## Key Features
 - Calculates reduced energy demand for assets, considering available energy output.
 - Provides an API endpoint (/asset/<asset_id>) to retrieve processed data in JSON format.
 - Adheres to best practices for code organization, documentation, and maintainability

## Documentation
 - Detailed instructions on code structure and functionality are provided within the code's comments.
 - Refer to this README for information on running the application, using the API, and understanding the output data.

## Error Handling
In case of errors, the API returns a JSON response with a 400 status code and an error message. Common errors include invalid asset ID or data format.

## License
This project is licensed under the MIT License. Check LICENSE from more informations.