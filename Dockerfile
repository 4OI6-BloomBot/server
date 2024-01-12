# Base image
FROM python:3.12.1-alpine3.19

# Configure dir and install requirements
WORKDIR /app
COPY    bloombot_server/requirements.txt .

# Add dep.
RUN set -ex \
  && apk add --no-cache --virtual build-base \
  && python -m venv /env                                    \
  && pip install --upgrade pip                              \
  && pip install -v --no-cache-dir -r requirements.txt

# Copy the start script and make it executable
COPY start.sh .
RUN  chmod +x /app/start.sh

# Copy all of the project files to the app dir
ADD bloombot_server .

# Open port 8000
EXPOSE 8000

# Run the start script and then start the server
ENTRYPOINT ["/app/start.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]