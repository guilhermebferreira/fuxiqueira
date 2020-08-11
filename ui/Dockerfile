FROM node:12-alpine

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

# install dependencies
RUN yarn install

COPY . .

EXPOSE 8080
