FROM node:20-alpine
WORKDIR /app
COPY package.json ./
RUN npm install --production
COPY . .
EXPOSE 5173
ENV PORT=5173
CMD ["node", "local-token-server/token-server.js"]
