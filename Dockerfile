FROM python:3.12-slim

# Copy the uv binary directly from the official distroless image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# Set environment variables to place the virtual environment on the system PATH
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY uv.lock pyproject.toml /app/

RUN uv sync 

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "line_bot.handler:app", "--host", "0.0.0.0", "--port", "8000"]





