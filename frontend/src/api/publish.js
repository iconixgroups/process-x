import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const publishModule = async (moduleId, publishStatus) => {
  try {
    const response = await axios.post(`${BASE_URL}/publish/module/${moduleId}`, {
      moduleId,
      publish: publishStatus
    });
    return response.data;
  } catch (error) {
    console.error('Error publishing the module:', error);
    throw error;
  }
};

export { publishModule };