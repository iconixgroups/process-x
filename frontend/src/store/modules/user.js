import { api } from '@/api/user.js';
import Vue from 'vue';

const state = {
  user: null,
  userStatus: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  user: state => state.user,
  userStatus: state => state.userStatus,
};

const actions = {
  async signInWithSocial({ commit }, payload) {
    try {
      const response = await api.signInWithSocial(payload.provider, payload.token);
      commit('setUser', response.data);
      commit('setUserStatus', 'success');
    } catch (error) {
      commit('setUserStatus', 'error');
      throw error;
    }
  },
  async registerWithEmail({ commit }, payload) {
    try {
      const response = await api.registerWithEmail(payload.email, payload.password);
      commit('setUser', response.data);
      commit('setUserStatus', 'success');
    } catch (error) {
      commit('setUserStatus', 'error');
      throw error;
    }
  },
  async verifyEmail({ commit }, payload) {
    try {
      const response = await api.verifyEmail(payload.email, payload.otp);
      commit('setUser', response.data);
      commit('setUserStatus', 'verified');
    } catch (error) {
      commit('setUserStatus', 'error');
      throw error;
    }
  },
  async signOut({ commit }) {
    commit('setUser', null);
    commit('setUserStatus', null);
  },
};

const mutations = {
  setUser(state, user) {
    state.user = user;
  },
  setUserStatus(state, status) {
    state.userStatus = status;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};