.PHONY: clean-dist docker

clean-dist:
	rm -rf dist/

docker:
	docker build -t ulope/rocketchat-webhook-proxy -f docker/Dockerfile .
