docker-build:
	docker build --tag risk-simulator -f ./container/Dockerfile .

docker-run:
	docker run -d -p 5050:5000 --name risk risk-sim

flask-run:
	python -m flask run