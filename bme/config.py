import os

class Config:
    # Oracle Database configuration
    ORACLE_USER = "system"
    ORACLE_PASSWORD = "your_password"
    ORACLE_DSN = "localhost/XEPDB1"  # Change "XEPDB1" to your DB service name
    ORACLE_PORT = 1521
    ORACLE_HOST = "localhost"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
