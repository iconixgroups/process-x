import { BASE_URL } from '@/api/baseUrl';
import axios from 'axios';

const state = {
  dashboardData: null,
  reports: [],
};

const getters = {
  getDashboardData: (state) => state.dashboardData,
  getReports: (state) => state.reports,
};

const actions = {
  async fetchDashboardData({ commit }, moduleId) {
    try {
      const response = await axios.get(`${BASE_URL}/dashboard/${moduleId}`);
      commit('setDashboardData', response.data);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    }
  },
  async generateReport({ commit }, { moduleId, reportCriteria }) {
    try {
      const response = await axios.get(`${BASE_URL}/reports/${moduleId}`, { params: reportCriteria });
      commit('addReport', response.data);
    } catch (error) {
      console.error('Error generating report:', error);
    }
  },
};

const mutations = {
  setDashboardData(state, data) {
    state.dashboardData = data;
  },
  addReport(state, report) {
    state.reports.push(report);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};