FROM node:alpine

USER node
WORKDIR /home/node/

COPY package*.json ./
RUN npm install

COPY views/ ./views
COPY app.js ./

EXPOSE 3000
CMD [ "npm", "start" ]