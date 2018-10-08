docker build -t misc-product .
docker run -d -p 18201:8080 --name misc-product misc-product
