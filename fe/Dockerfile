FROM node:18.14.2-alpine3.16

WORKDIR /app

COPY ./app/package*.json ./
RUN npm install

CMD ["npm", "run", "dev"]
