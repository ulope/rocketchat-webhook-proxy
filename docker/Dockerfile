FROM python:3.7

ADD dist/rocketchat_webhook_proxy*.whl /

RUN pip install /rocketchat_webhook_proxy*.whl

EXPOSE 8000
ENTRYPOINT ["hypercorn", "--access-log", "-", "--error-log", "-", "--worker-class", "trio", "--bind", "0.0.0.0:8000", "rocketchat_webhook_proxy.app:app"]
