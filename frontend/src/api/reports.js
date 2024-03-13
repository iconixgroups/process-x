import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const getDashboardData = async (moduleId) => {
  try {
    const response = await axios.get(`${BASE_URL}/dashboard/${moduleId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching dashboard data:', error);
    throw error;
  }
};

const generateReport = async (moduleId, reportParams) => {
  try {
    const response = await axios.get(`${BASE_URL}/reports/${moduleId}`, { params: reportParams });
    return response.data;
  } catch (error) {
    console.error('Error generating report:', error);
    throw error;
  }
};

export const reportsApi = {
  getDashboardData,
  generateReport,
};