# Borro la base de datos si existe
DROP DATABASE IF EXISTS visa_hb1_certified;

# Creo la base de datos
CREATE DATABASE visa_hb1_certified;

# La utilizo
USE visa_hb1_certified;

# Consulto sobre las primeras 5
SELECT * FROM certified LIMIT 5;