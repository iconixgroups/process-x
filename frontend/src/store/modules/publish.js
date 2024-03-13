import { api } from '@/api/publish.js';
import Vue from 'vue';

const state = {
  modules: [],
  isPublishing: false,
  publishError: null
};

const getters = {
  getModules: state => state.modules,
  isPublishing: state => state.isPublishing,
  publishError: state => state.publishError
};

const actions = {
  async fetchModules({ commit }) {
    try {
      const response = await api.fetchModules();
      commit('setModules', response.data);
    } catch (error) {
      commit('setPublishError', error);
    }
  },
  async publishModule({ commit }, moduleId) {
    commit('setIsPublishing', true);
    try {
      const response = await api.publishModule(moduleId);
      commit('updateModuleStatus', { moduleId, status: response.data.publish });
      commit('setIsPublishing', false);
    } catch (error) {
      commit('setPublishError', error);
      commit('setIsPublishing', false);
    }
  }
};

const mutations = {
  setModules(state, modules) {
    state.modules = modules;
  },
  setIsPublishing(state, isPublishing) {
    state.isPublishing = isPublishing;
  },
  setPublishError(state, error) {
    state.publishError = error;
  },
  updateModuleStatus(state, { moduleId, status }) {
    const moduleIndex = state.modules.findIndex(module => module.id === moduleId);
    if (moduleIndex !== -1) {
      Vue.set(state.modules[moduleIndex], 'published', status);
    }
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};