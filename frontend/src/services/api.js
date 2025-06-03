import axios from 'axios';

const API_GATEWAY = process.env.REACT_APP_API_URL;

export const analyzeText = async (text, token) => {
  return axios.post(`${API_GATEWAY}/analyze`, { text }, {
    headers: { Authorization: `Bearer ${token}` }
  });
};

export const sendNotification = async (phone, message, token) => {
  return axios.post(`${API_GATEWAY}/notify`, { phone, message }, {
    headers: { Authorization: `Bearer ${token}` }
  });
};