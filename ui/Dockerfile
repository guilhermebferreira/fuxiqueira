FROM node:12-alpine

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

# install dependencies
RUN yarn install

COPY . .

# build application
RUN yarn build

#EXPOSE 3030
EXPOSE 8080

CMD [ "node", "./dist/Main.js" ]