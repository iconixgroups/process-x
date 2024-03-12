<template>
  <div class="workflow-management">
    <h1>Workflow Management</h1>
    <form @submit.prevent="createWorkflow">
      <div class="form-group">
        <label for="formId">Select Form:</label>
        <select id="formId" v-model="workflow.formId" required>
          <option v-for="form in forms" :key="form.id" :value="form.id">{{ form.name }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="reviewFields">Reviewable Fields:</label>
        <multiselect v-model="workflow.reviewFields" :options="fields" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Pick fields" label="name" track-by="name" :preselect-first="true"></multiselect>
      </div>
      <div class="form-group">
        <label for="reviewers">Assign Reviewers:</label>
        <multiselect v-model="workflow.reviewers" :options="users" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Pick reviewers" label="name" track-by="name" :preselect-first="true"></multiselect>
      </div>
      <div class="form-group">
        <label for="outcomes">Workflow Outcomes:</label>
        <multiselect v-model="workflow.outcomes" :options="outcomes" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Pick outcomes" label="label" track-by="value" :preselect-first="true"></multiselect>
      </div>
      <button type="submit" class="btn btn-primary">Create Workflow</button>
    </form>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect';

export default {
  components: {
    Multiselect
  },
  data() {
    return {
      workflow: {
        formId: '',
        reviewFields: [],
        reviewers: [],
        outcomes: []
      },
      forms: [],
      fields: [],
      users: [],
      outcomes: [
        { label: 'Approve', value: 'approve' },
        { label: 'Reject', value: 'reject' },
        { label: 'On Hold', value: 'on_hold' }
      ]
    };
  },
  created() {
    this.fetchForms();
    this.fetchFields();
    this.fetchUsers();
  },
  methods: {
    fetchForms() {
      // Fetch forms associated with the selected module
      // Placeholder for actual API call
      this.forms = [
        { id: 'form1', name: 'Leave Request' },
        { id: 'form2', name: 'Expense Report' }
      ];
    },
    fetchFields() {
      // Fetch fields of the selected form
      // Placeholder for actual API call
      this.fields = [
        { name: 'startDate' },
        { name: 'endDate' }
      ];
    },
    fetchUsers() {
      // Fetch users to assign as reviewers
      // Placeholder for actual API call
      this.users = [
        { name: 'John Doe', id: 'user1' },
        { name: 'Jane Smith', id: 'user2' }
      ];
    },
    createWorkflow() {
      // Placeholder for actual API call to create workflow
      console.log('Workflow created:', this.workflow);
      // Reset form after submission
      this.workflow = {
        formId: '',
        reviewFields: [],
        reviewers: [],
        outcomes: []
      };
    }
  }
};
</script>

<style scoped>
.workflow-management {
  max-width: 600px;
  margin: auto;
}

.form-group {
  margin-bottom: 1rem;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.multiselect {
  width: 100%;
}
</style>