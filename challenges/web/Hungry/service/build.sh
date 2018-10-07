docker build -t hungry .
docker run -dit -p 18705:5000 -m 64M --name sanity-hungry hungry
