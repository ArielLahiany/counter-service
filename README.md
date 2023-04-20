# Counter-Service

## Description

A simple web application that counts the number of POST requests it served.

### Endpoints

1. Root ("/"): Listens to GET and POST requests and responses accordingly.

2. Health ("/health"): Listens to GET requests and replies with a static OK HTTP response (status code 200).

## Prerequisites

1. Docker: a working station with Docker and Docker-Compose pre-installed.

## Usage

1. Add the following entry to the hosts file of your working station:

   ```txt
   127.0.1.1 counter.harmony.local
   ```

2. Build the service Docker image:

   ```bash
   make docker/build
   ```

3. Spin up the stack:

   ```bash
   make docker-compose/up
   ```

4. In order to see the amount of served POST requests, send a GET request to the server using cURL (ignoring the self-signed certificate):

   ```bash
   curl -X GET -k https://counter.harmony.local
   ```

5. In order to increase the counter, send a POST request to the server using cURL (ignoring the self-signed certificate):

   ```bash
   curl -x POST -k https://counter.harmony.local
   ```
