FROM node:12-alpine as dev

WORKDIR /app
RUN apk add --no-cache tzdata
COPY package.json package-lock.json ./

RUN npm install

ADD . .
