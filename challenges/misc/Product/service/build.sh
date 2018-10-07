docker build -t web-product .
docker run -d -p 18710:8080 --name web-product web-product
