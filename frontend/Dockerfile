FROM node:alpine

WORKDIR /instaclip-frontend

COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]