FROM brunozaccariello/sgehookah

ENV PYTHONBUFFERED 1

RUN apk add postgresql-dev python3-dev gcc musl-dev

WORKDIR /SGEHookah

COPY ./SGEHookah .
RUN pip install --no-cache-dir -r requirements.txt