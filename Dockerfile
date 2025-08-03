# Použijeme oficiální Python runtime jako základ
FROM python:3.9-slim

# Nastavíme pracovní adresář v kontejneru
WORKDIR /app

# Zkopírujeme Python soubory do kontejneru
COPY calculator.py .
COPY test_calculator.py .

# Spustíme testy při buildu (volitelné)
RUN python -m unittest test_calculator.py -v

# Nastavíme příkaz, který se spustí při startu kontejneru
CMD ["python", "calculator.py"]
CMD ["python", "-m", "unittest", "test_calculator.py"]