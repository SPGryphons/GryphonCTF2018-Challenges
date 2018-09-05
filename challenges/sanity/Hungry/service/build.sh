docker build -t sanity-hungry .
docker run -it -p 5000:5000 -m 64M --name sanity-hungry sanity-hungry
