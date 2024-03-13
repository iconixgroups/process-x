import { api } from '@/api/settings.js';
import Vue from 'vue';

const state = {
  modules: [],
  currentModule: null,
};

const getters = {
  getModules: state => state.modules,
  getCurrentModule: state => state.currentModule,
};

const actions = {
  async addModule({ commit }, moduleData) {
    try {
      const response = await api.addModule(moduleData);
      commit('SET_MODULE', response.data);
      return response;
    } catch (error) {
      console.error('Error adding module:', error);
      throw error;
    }
  },
  async updateModule({ commit }, { moduleId, moduleData }) {
    try {
      const response = await api.updateModule(moduleId, moduleData);
      commit('UPDATE_MODULE', { moduleId, moduleData: response.data });
      return response;
    } catch (error) {
      console.error('Error updating module:', error);
      throw error;
    }
  },
  async fetchModules({ commit }) {
    try {
      const response = await api.fetchModules();
      commit('SET_MODULES', response.data);
      return response;
    } catch (error) {
      console.error('Error fetching modules:', error);
      throw error;
    }
  },
  setCurrentModule({ commit }, module) {
    commit('SET_CURRENT_MODULE', module);
  },
};

const mutations = {
  SET_MODULES(state, modules) {
    state.modules = modules;
  },
  SET_MODULE(state, module) {
    state.modules.push(module);
  },
  UPDATE_MODULE(state, { moduleId, moduleData }) {
    const index = state.modules.findIndex(module => module.id === moduleId);
    if (index !== -1) {
      Vue.set(state.modules, index, moduleData);
    }
  },
  SET_CURRENT_MODULE(state, module) {
    state.currentModule = module;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};