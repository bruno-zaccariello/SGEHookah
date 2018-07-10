FROM brunozaccariello/sgehookah

ENV PYTHONBUFFERED 1

RUN mkdir /SGEHookah

WORKDIR /SGEHookah

COPY ./SGEHookah .
RUN pip install --no-cache-dir -r requirements.txt