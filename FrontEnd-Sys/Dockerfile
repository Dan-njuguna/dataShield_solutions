
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY ds-react/package.json /app/
RUN npm install

# Copy the rest of the application code
COPY ./ds-react /app

# Installing react-scripts
RUN npm install react-scripts@4.0.3 -g

# Build the app
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Serve the app
CMD ["npm", "start"]
