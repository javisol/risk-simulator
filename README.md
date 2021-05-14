# Risk Simulator #

Flask and docker based program to simulate Risk dice rolling.

## Build and run code ##
### Docker building ###
```bash
docker build --tag risk-sim -f ./container/Dockerfile .
```
### Docker run ###
```bash
docker run -d -p 5050:5000 --name risk risk-sim
```
### Flask run ###
```bash
python -m flask run
```