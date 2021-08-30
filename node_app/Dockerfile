FROM node:lts-alpine3.14

WORKDIR /app

COPY /src .

RUN yarn install

# RUN npm test

EXPOSE 8080

# TODO: non-root user
ENTRYPOINT ["yarn", "start"]


# docker build -t bpa .
# docker run -d -p 8100:8080 --name bpa bpa
