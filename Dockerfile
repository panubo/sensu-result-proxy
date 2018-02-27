FROM python:2.7-slim

EXPOSE 8080

ADD requirements.txt /usr/src/
RUN pip install --no-cache-dir -r /usr/src/requirements.txt
ADD *.py /usr/src/

CMD ["/usr/src/entry.py", "/usr/src/app.py", "8080"]
