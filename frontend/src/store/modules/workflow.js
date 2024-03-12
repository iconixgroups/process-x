import { BASE_URL, API_VERSION } from '@/api/config';

const state = {
  workflows: [],
  currentWorkflow: null,
};

const getters = {
  allWorkflows: (state) => state.workflows,
  currentWorkflow: (state) => state.currentWorkflow,
};

const actions = {
  async fetchWorkflows({ commit }, moduleId) {
    try {
      const response = await fetch(`${BASE_URL}/${API_VERSION}/design/workflow?moduleId=${moduleId}`);
      const data = await response.json();
      commit('setWorkflows', data);
    } catch (error) {
      console.error('Error fetching workflows:', error);
    }
  },
  async createWorkflow({ commit }, workflowDetails) {
    try {
      const response = await fetch(`${BASE_URL}/${API_VERSION}/design/workflow`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(workflowDetails),
      });
      const data = await response.json();
      commit('addWorkflow', data);
    } catch (error) {
      console.error('Error creating workflow:', error);
    }
  },
  async updateWorkflow({ commit }, workflowDetails) {
    try {
      const response = await fetch(`${BASE_URL}/${API_VERSION}/design/workflow/${workflowDetails.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(workflowDetails),
      });
      const data = await response.json();
      commit('updateWorkflow', data);
    } catch (error) {
      console.error('Error updating workflow:', error);
    }
  },
  async deleteWorkflow({ commit }, id) {
    try {
      await fetch(`${BASE_URL}/${API_VERSION}/design/workflow/${id}`, {
        method: 'DELETE',
      });
      commit('removeWorkflow', id);
    } catch (error) {
      console.error('Error deleting workflow:', error);
    }
  },
  setCurrentWorkflow({ commit }, workflow) {
    commit('setCurrentWorkflow', workflow);
  },
};

const mutations = {
  setWorkflows: (state, workflows) => (state.workflows = workflows),
  addWorkflow: (state, newWorkflow) => state.workflows.push(newWorkflow),
  updateWorkflow: (state, updatedWorkflow) => {
    const index = state.workflows.findIndex((workflow) => workflow.id === updatedWorkflow.id);
    if (index !== -1) {
      state.workflows.splice(index, 1, updatedWorkflow);
    }
  },
  removeWorkflow: (state, id) => (state.workflows = state.workflows.filter((workflow) => workflow.id !== id)),
  setCurrentWorkflow: (state, workflow) => (state.currentWorkflow = workflow),
};

export default {
  state,
  getters,
  actions,
  mutations,
};