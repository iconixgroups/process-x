import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const addModule = async (moduleName, companyCode, divisionCode) => {
  try {
    const response = await axios.post(`${BASE_URL}/settings/module`, {
      moduleName,
      companyCode,
      divisionCode
    });
    return response.data;
  } catch (error) {
    console.error('Error adding module:', error);
    throw error;
  }
};

const updateModule = async (moduleId, updatedData) => {
  try {
    const response = await axios.put(`${BASE_URL}/settings/module/${moduleId}`, updatedData);
    return response.data;
  } catch (error) {
    console.error('Error updating module:', error);
    throw error;
  }
};

export const settingsApi = {
  addModule,
  updateModule
};