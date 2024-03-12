import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const userApi = {
  socialSignIn: async (provider, token) => {
    try {
      const response = await axios.post(`${BASE_URL}/auth/social`, {
        provider,
        token,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  emailRegister: async (email, password) => {
    try {
      const response = await axios.post(`${BASE_URL}/auth/register`, {
        email,
        password,
      });
      return response.data;
    } catch (error) {
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
      throw error;
    }
  },
  addCompany: async (companyData) => {
    try {
      const response = await axios.post(`${BASE_URL}/company`, companyData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  addDivision: async (divisionData) => {
    try {
      const response = await axios.post(`${BASE_URL}/company/division`, divisionData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  addDepartment: async (departmentData) => {
    try {
      const response = await axios.post(`${BASE_URL}/company/department`, departmentData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  addProject: async (projectData) => {
    try {
      const response = await axios.post(`${BASE_URL}/company/project`, projectData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  addUser: async (userData) => {
    try {
      const response = await axios.post(`${BASE_URL}/company/user`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default userApi;