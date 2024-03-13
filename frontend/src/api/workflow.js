import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const createWorkflow = async (workflowData) => {
  try {
    const response = await axios.post(`${BASE_URL}/design/workflow`, workflowData);
    return response.data;
  } catch (error) {
    console.error('Error creating workflow:', error);
    throw error;
  }
};

const updateWorkflow = async (workflowId, workflowData) => {
  try {
    const response = await axios.put(`${BASE_URL}/design/workflow/${workflowId}`, workflowData);
    return response.data;
  } catch (error) {
    console.error('Error updating workflow:', error);
    throw error;
  }
};

const getWorkflow = async (workflowId) => {
  try {
    const response = await axios.get(`${BASE_URL}/design/workflow/${workflowId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching workflow:', error);
    throw error;
  }
};

const deleteWorkflow = async (workflowId) => {
  try {
    const response = await axios.delete(`${BASE_URL}/design/workflow/${workflowId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting workflow:', error);
    throw error;
  }
};

export const workflowApi = {
  createWorkflow,
  updateWorkflow,
  getWorkflow,
  deleteWorkflow
};