## Sensory API

## Introduction
The Sensory API provides access to sensory data and statistics. This API is built using Flask and uses a MySQL database for data storage.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Example Requests](#example-requests)
- [Dependencies](#dependencies)
- [Contributors](#contributors)
- [License](#license)

## Installation
To run the Sensory API using Docker, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set up environment variables:**
    Create a `.env` file in the root directory and add the following:
    ```sh
    DB_HOST=your_db_host
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_NAME=your_db_name
    ```

3. **Build the Docker image:**
    ```sh
    docker build -t sensory-api .
    ```

4. **Run the Docker container:**
    ```sh
    docker run -d -p 5000:5000 --env-file .env sensory-api
    ```

## Usage
To use the Sensory API, you need to send HTTP requests to the specified endpoints. Replace `http://localhost:5000` with the actual URL of your API if it's hosted elsewhere.

## Endpoints

### `/senzory`
- **Method:** GET
- **Description:** Retrieves a list of all sensors in the system.
- **Response:** A JSON array of objects, each representing a sensor. Each object contains the following properties:
    - `id`: The unique identifier of the sensor.
    - `nazev`: The name of the sensor.
    - `typ`: The type of the sensor.
    - `misto`: The location of the sensor.
    - `frekvence`: The frequency of the sensor.
    - `stav`: The status of the sensor.
    - `count_records`: The number of records for the sensor.

### `/pocetzaminutu`
- **Method:** GET
- **Description:** Retrieves the number of records in the last minute.
- **Response:** A JSON object with a single property:
    - `count`: The number of records in the last minute.

### `/pocetsenzoru`
- **Method:** GET
- **Description:** Retrieves the total number of sensors in the system.
- **Response:** A JSON object with a single property:
    - `count`: The total number of sensors.

## Example Requests

### `/senzory`
**GET** `/senzory`

**Response:**
```json
[
    {
        "id": 1,
        "nazev": "Sensor 1",
        "typ": "Temperature",
        "misto": "Office",
        "frekvence": "1 minute",
        "stav": "Online",
        "count_records": 100
    },
    {
        "id": 2,
        "nazev": "Sensor 2",
        "typ": "Humidity",
        "misto": "Living Room",
        "frekvence": "5 minutes",
        "stav": "Offline",
        "count_records": 50
    }
]
```

### `/pocetzaminutu`
**GET** `/pocetzaminutu`

**Response:**
```json
{
    "count": 50
}
```

### `/pocetsenzoru`
**GET** `/pocetsenzoru`

**Response:**
```json
{
    "count": 10
}
```

## Dependencies
- Flask
- Flask-CORS
- mysql-connector-python
- Docker

## Contributors
- [Aroteo](https://github.com/JP1Q)

## License
This project is licensed under the MIT License.