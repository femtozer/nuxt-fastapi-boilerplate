FROM node:20-alpine3.18
WORKDIR /code
COPY ./package*.json /code/
RUN npm install
COPY . /code
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
EXPOSE 3000
CMD ["npm", "run", "dev"]
