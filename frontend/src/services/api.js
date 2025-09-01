import axios from "axios";

// Crear una instancia de axios
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL, // usa la variable de entorno
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
