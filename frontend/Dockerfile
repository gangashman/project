FROM node:12-alpine

WORKDIR /app
RUN apk add --no-cache tzdata
COPY package.json package-lock.json ./

RUN npm install

ADD . .
