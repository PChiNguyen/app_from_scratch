# ==========================================
# STAGE 1: BUILDER
# ==========================================
FROM python:3.12-slim AS builder

WORKDIR /ieltsapp

COPY requirements.txt .

# Install dependencies into a temporary prefix directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ==========================================
# STAGE 2: FINAL RUNNER
# ==========================================
FROM python:3.12-slim

WORKDIR /ieltsapp

# Copy installed dependencies into standard global path
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Create non-root user for security compliance
RUN useradd -m appuser && chown -R appuser:appuser /ieltsapp
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]