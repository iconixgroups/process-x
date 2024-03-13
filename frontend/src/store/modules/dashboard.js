import { api } from '@/api/dashboard.js';
import Vue from 'vue';

const state = {
  dashboardData: {},
};

const getters = {
  getDashboardData: state => state.dashboardData,
};

const actions = {
  async fetchDashboardData({ commit }, moduleId) {
    try {
      const response = await api.fetchDashboardData(moduleId);
      commit('SET_DASHBOARD_DATA', response.data);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    }
  },
};

const mutations = {
  SET_DASHBOARD_DATA(state, data) {
    Vue.set(state, 'dashboardData', data);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};