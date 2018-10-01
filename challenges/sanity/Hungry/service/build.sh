docker build -t hungry .
docker run -it -p 5000:5000 -m 64M --name sanity-hungry hungry
