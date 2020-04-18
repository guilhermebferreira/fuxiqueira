# nodejs base image
FROM node:current-alpine

# setup work directory
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

# install dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install -g @vue/cli

# start app
CMD ["npm", "run", "serve"]