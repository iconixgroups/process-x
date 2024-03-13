import { api } from '@/api/company.js';
import Vue from 'vue';

const state = {
  companies: [],
  divisions: [],
  departments: [],
  projects: [],
  users: []
};

const getters = {
  getCompanies: state => state.companies,
  getDivisions: state => state.divisions,
  getDepartments: state => state.departments,
  getProjects: state => state.projects,
  getUsers: state => state.users
};

const actions = {
  async registerCompany({ commit }, companyData) {
    try {
      const response = await api.registerCompany(companyData);
      commit('SET_COMPANY', response.data);
      return response;
    } catch (error) {
      console.error('registerCompany:', error);
      throw error;
    }
  },
  async addDivision({ commit }, divisionData) {
    try {
      const response = await api.addDivision(divisionData);
      commit('SET_DIVISION', response.data);
      return response;
    } catch (error) {
      console.error('addDivision:', error);
      throw error;
    }
  },
  async addDepartment({ commit }, departmentData) {
    try {
      const response = await api.addDepartment(departmentData);
      commit('SET_DEPARTMENT', response.data);
      return response;
    } catch (error) {
      console.error('addDepartment:', error);
      throw error;
    }
  },
  async addProject({ commit }, projectData) {
    try {
      const response = await api.addProject(projectData);
      commit('SET_PROJECT', response.data);
      return response;
    } catch (error) {
      console.error('addProject:', error);
      throw error;
    }
  },
  async addUser({ commit }, userData) {
    try {
      const response = await api.addUser(userData);
      commit('SET_USER', response.data);
      return response;
    } catch (error) {
      console.error('addUser:', error);
      throw error;
    }
  }
};

const mutations = {
  SET_COMPANY(state, company) {
    state.companies.push(company);
  },
  SET_DIVISION(state, division) {
    state.divisions.push(division);
  },
  SET_DEPARTMENT(state, department) {
    state.departments.push(department);
  },
  SET_PROJECT(state, project) {
    state.projects.push(project);
  },
  SET_USER(state, user) {
    state.users.push(user);
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};