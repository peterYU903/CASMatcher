FROM python:3.11.7-slim-bullseye

WORKDIR /casmatcher

RUN mkdir -p /casmatcher/standards
RUN mkdir -p /casmatcher/outputs

COPY .env .
COPY ./sources ./sources
COPY ./pages ./pages
COPY requirements.txt .
COPY Login.py .

RUN pip install -r requirements.txt --trusted-host pypi.org

EXPOSE 8501

CMD streamlit run Login.py --browser.gatherUsageStats False