import { apiService } from '@/api/auth.js';
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const auth = {
  namespaced: true,

  state: {
    user: null,
    isAuthenticated: false,
  },

  getters: {
    authenticatedUser: (state) => state.user,
    isAuthenticated: (state) => state.isAuthenticated,
  },

  actions: {
    async socialSignIn({ commit }, payload) {
      try {
        const response = await apiService.socialSignIn(payload.provider, payload.token);
        commit('SET_USER', response.data.user);
        commit('SET_AUTHENTICATED', true);
      } catch (error) {
        console.error('Error during social sign-in:', error);
      }
    },

    async emailRegister({ commit }, payload) {
      try {
        const response = await apiService.emailRegister(payload.email, payload.password);
        commit('SET_USER', response.data.user);
        commit('SET_AUTHENTICATED', true);
      } catch (error) {
        console.error('Error during email registration:', error);
      }
    },

    async verifyEmail({ commit }, payload) {
      try {
        const response = await apiService.verifyEmail(payload.email, payload.otp);
        commit('SET_USER', response.data.user);
        commit('SET_AUTHENTICATED', true);
      } catch (error) {
        console.error('Error during email verification:', error);
      }
    },

    signOut({ commit }) {
      commit('SET_USER', null);
      commit('SET_AUTHENTICATED', false);
    },
  },

  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },

    SET_AUTHENTICATED(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
  },
};

export default new Vuex.Store({
  modules: {
    auth,
  },
});