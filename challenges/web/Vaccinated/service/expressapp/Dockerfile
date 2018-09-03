FROM node:alpine

WORKDIR /home/node/

COPY package*.json ./
RUN npm install

COPY . ./

RUN rm -f Dockerfile .dockerignore

EXPOSE 3000
CMD [ "npm", "start" ]
