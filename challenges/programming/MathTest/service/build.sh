docker build -t mathtest .
docker run -dit -p 18000:8000 --name prog-mathtest mathtest