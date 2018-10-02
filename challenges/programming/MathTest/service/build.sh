docker build -t mathtest .
docker run -dit -p 18300:8000 --name prog-mathtest mathtest