# Usa una imagen Node.js más liviana
FROM node:14-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY package.json package-lock.json /app/

# Instala las dependencias
RUN npm install
RUN npm install axios
RUN npm install ejs
RUN npm install bootstrap
RUN npm install express

# Copia el resto de los archivos
COPY . /app/

# Expón el puerto en el que se ejecutará la aplicación
EXPOSE 3001

# Comando para iniciar la aplicación
CMD ["npm", "start"]
