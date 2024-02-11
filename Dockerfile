# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# for Amplify 
# https://docs.amplify.aws/cli/usage/containers#deploy-a-single-container
EXPOSE 80

COPY ./* /app
