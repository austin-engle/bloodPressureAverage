FROM node:lts-alpine3.14

WORKDIR /app

COPY /src .

RUN npm install

# RUN npm test

EXPOSE 8080

# TODO: non-root user
ENTRYPOINT ["npm", "start"]


# docker build -t node-test .
# docker run -p 8080:8080 node-test
