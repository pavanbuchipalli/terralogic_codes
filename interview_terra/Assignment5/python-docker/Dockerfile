
FROM ubuntu:latest
FROM python:3


WORKDIR /C:/Users/PavanB-3247/.jenkins/jobs/code


RUN apt-get update && apt-get install -y git

RUN  git clone   https://github.com/pavanbuchipalli/complete_task.git



WORKDIR /C:/Users/PavanB-3247/.jenkins/jobs/code/complete_task

CMD ["python","count_s.py"]