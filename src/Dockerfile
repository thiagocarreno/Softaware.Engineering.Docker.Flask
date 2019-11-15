FROM python:3
WORKDIR /app
ADD requirements.txt requirements.txt
ADD /app/*.* /app
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
CMD ["python", "program.py" ]
EXPOSE 5000
