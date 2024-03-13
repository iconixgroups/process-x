import { api } from '@/api/design.js';
import Vue from 'vue';

const state = {
  processes: [],
  currentProcess: null,
  forms: [],
  currentForm: null,
  workflows: [],
  currentWorkflow: null
};

const getters = {
  getProcesses: state => state.processes,
  getCurrentProcess: state => state.currentProcess,
  getForms: state => state.forms,
  getCurrentForm: state => state.currentForm,
  getWorkflows: state => state.workflows,
  getCurrentWorkflow: state => state.currentWorkflow
};

const actions = {
  async fetchProcesses({ commit }, moduleId) {
    try {
      const response = await api.fetchProcesses(moduleId);
      commit('setProcesses', response.data);
    } catch (error) {
      console.error('Error fetching processes:', error);
    }
  },
  async createProcess({ commit }, processDetails) {
    try {
      const response = await api.createProcess(processDetails);
      commit('addProcess', response.data);
    } catch (error) {
      console.error('Error creating process:', error);
    }
  },
  async fetchForms({ commit }, processId) {
    try {
      const response = await api.fetchForms(processId);
      commit('setForms', response.data);
    } catch (error) {
      console.error('Error fetching forms:', error);
    }
  },
  async createForm({ commit }, formDetails) {
    try {
      const response = await api.createForm(formDetails);
      commit('addForm', response.data);
    } catch (error) {
      console.error('Error creating form:', error);
    }
  },
  async fetchWorkflows({ commit }, formId) {
    try {
      const response = await api.fetchWorkflows(formId);
      commit('setWorkflows', response.data);
    } catch (error) {
      console.error('Error fetching workflows:', error);
    }
  },
  async createWorkflow({ commit }, workflowDetails) {
    try {
      const response = await api.createWorkflow(workflowDetails);
      commit('addWorkflow', response.data);
    } catch (error) {
      console.error('Error creating workflow:', error);
    }
  }
};

const mutations = {
  setProcesses(state, processes) {
    state.processes = processes;
  },
  addProcess(state, process) {
    state.processes.push(process);
  },
  setCurrentProcess(state, process) {
    state.currentProcess = process;
  },
  setForms(state, forms) {
    state.forms = forms;
  },
  addForm(state, form) {
    state.forms.push(form);
  },
  setCurrentForm(state, form) {
    state.currentForm = form;
  },
  setWorkflows(state, workflows) {
    state.workflows = workflows;
  },
  addWorkflow(state, workflow) {
    state.workflows.push(workflow);
  },
  setCurrentWorkflow(state, workflow) {
    state.currentWorkflow = workflow;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};