import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const designApi = {
  designProcess: (moduleId, processDetails) => {
    return axios.post(`${BASE_URL}/design/process`, {
      moduleId,
      ...processDetails
    });
  },
  createForm: (processId, formDetails) => {
    return axios.post(`${BASE_URL}/design/form`, {
      processId,
      ...formDetails
    });
  },
  createWorkflow: (formId, workflowDetails) => {
    return axios.post(`${BASE_URL}/design/workflow`, {
      formId,
      ...workflowDetails
    });
  }
};

export default designApi;