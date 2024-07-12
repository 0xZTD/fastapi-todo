FROM python

WORKDIR /usr/app/src

COPY requirements.txt . 

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi","run", "todo/main.py"]
