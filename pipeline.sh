echo "Descargando datos..."
URL="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_rade,pl_bmasse+from+ps&format=csv"
wget -O datos_crudos.csv "$URL"
echo "Armando la base de datos..."
python3 constructor_db.py
echo "Analizando..."
python3 analisis_visual.py
echo "Todo listo... se ha generado la imagen resultado.png"
