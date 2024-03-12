import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const authApi = {
  socialSignIn: async (provider, token) => {
    try {
      const response = await axios.post(`${BASE_URL}/auth/social`, {
        provider,
        token,
      });
      return response.data;
    } catch (error) {
      console.error('Error during social sign-in:', error);
      throw error;
    }
  },
  emailRegistration: async (email, password) => {
    try {
      const response = await axios.post(`${BASE_URL}/auth/register`, {
        email,
        password,
      });
      return response.data;
    } catch (error) {
      console.error('Error during email registration:', error);
      throw error;
    }
  },
  verifyEmail: async (email, otp) => {
    try {
      const response = await axios.post(`${BASE_URL}/auth/verify`, {
        email,
        otp,
      });
      return response.data;
    } catch (error) {
      console.error('Error during email verification:', error);
      throw error;
    }
  },
};

export default authApi;