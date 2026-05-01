#!/bin/bash

# Script para generar certificados auto-firmados para HTTPS

CERT_DIR="certs"
DAYS=365

# Crear directorio si no existe
mkdir -p $CERT_DIR

# Generar certificado auto-firmado (válido por 365 días)
openssl req -x509 -newkey rsa:4096 -nodes \
    -out "$CERT_DIR/cert.pem" \
    -keyout "$CERT_DIR/key.pem" \
    -days $DAYS \
    -subj "/C=MX/ST=Mexico/L=Mexico/O=Mecate/OU=IT/CN=localhost"

echo "✓ Certificados generados en $CERT_DIR/"
echo "  - Certificado: $CERT_DIR/cert.pem"
echo "  - Clave privada: $CERT_DIR/key.pem"
echo "  - Válidos por: $DAYS días"
