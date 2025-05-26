FROM python:3.12-alpine

LABEL image_name="back-end-api"

WORKDIR /backend

COPY ./requirements.txt /backend/

RUN apk update
RUN python3.12 -m venv .venv

RUN source .venv/bin/activate

RUN pip3 install -r requirements.txt --break-system-packages

COPY . /backend/ 

EXPOSE 4999
EXPOSE 5000
EXPOSE 5001

USER root

RUN chmod +x /backend/compile_proto.sh

RUN sh /backend/compile_proto.sh
# CMD ["python", "-c", "import time; time.sleep(100000)"]
CMD ["python", "-m", "server"]
