import axios from 'axios';

const BASE_URL = 'https://api.processx.com/v1';

const companyApi = {
  registerCompany: (companyData) => axios.post(`${BASE_URL}/company`, companyData),
  addDivision: (divisionData) => axios.post(`${BASE_URL}/company/division`, divisionData),
  addDepartment: (departmentData) => axios.post(`${BASE_URL}/company/department`, departmentData),
  addProject: (projectData) => axios.post(`${BASE_URL}/company/project`, projectData),
  addUser: (userData) => axios.post(`${BASE_URL}/company/user`, userData),
};

export default companyApi;