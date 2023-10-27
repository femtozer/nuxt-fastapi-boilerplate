FROM node:20-alpine3.18
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable
WORKDIR /code
COPY ./.npmrc /code/
COPY ./package.json /code/
COPY ./pnpm-lock.yaml /code/
RUN pnpm install
COPY . /code
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
EXPOSE 3000
CMD ["pnpm", "run", "dev"]
