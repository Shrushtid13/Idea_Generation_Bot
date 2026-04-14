# Base image

FROM python:3.12


# Set timezone
ENV TZ="Asia/Kolkata"


#  Set working directory

WORKDIR /app


#  Copy all project files

COPY . /app


#  Install dependencies

RUN pip install --upgrade pip && pip install -r requirements.txt


#  Expose Flask port

EXPOSE 5000

ENTRYPOINT ["sh", "run.sh"]
