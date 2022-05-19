FROM python:3.9-slim-buster


ENV  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  # pip
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  # poetry
  PATH=/root/.local/bin:$PATH

# system
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  bash \
  build-essential \
  python3-dev \
  curl \
  libffi-dev \
  libxslt-dev \
  libxml2 \
  libxml2-dev \
  cargo \
  wget \
  # cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# poetry
WORKDIR /code/poetry
COPY poetry/install-poetry.py ./
RUN pip install -U pip &&  \
    python install-poetry.py --version 1.1.13 &&  \
    poetry config virtualenvs.create false
COPY poetry ./
RUN poetry install --no-interaction --no-root

#system
WORKDIR /code
COPY ./src .
COPY start.sh .
RUN mkdir -p /code/logs
VOLUME ["/code/logs"]
RUN sed -i 's/\r//' start.sh
RUN chmod +x start.sh
