<template>
  <div class="module-settings">
    <h1>Module Settings</h1>
    <form @submit.prevent="createModule">
      <div class="form-group">
        <label for="moduleName">Module Name:</label>
        <input type="text" id="moduleName" v-model="moduleData.moduleName" required>
      </div>
      <div class="form-group">
        <label for="companyCode">Company Code:</label>
        <input type="text" id="companyCode" v-model="moduleData.companyCode" required>
      </div>
      <div class="form-group">
        <label for="divisionCode">Division Code:</label>
        <input type="text" id="divisionCode" v-model="moduleData.divisionCode" required>
      </div>
      <button type="submit">Create Module</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ModuleSettings',
  data() {
    return {
      moduleData: {
        moduleName: '',
        companyCode: '',
        divisionCode: ''
      }
    };
  },
  methods: {
    async createModule() {
      try {
        const response = await this.$axios.post(`${process.env.VUE_APP_BASE_API_URL}/settings/module`, this.moduleData);
        this.$emit('moduleCreated', response.data);
        this.resetForm();
      } catch (error) {
        console.error('Error creating module:', error);
      }
    },
    resetForm() {
      this.moduleData = {
        moduleName: '',
        companyCode: '',
        divisionCode: ''
      };
    }
  }
};
</script>

<style scoped>
.module-settings {
  max-width: 600px;
  margin: auto;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

input[type="text"] {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

button {
  padding: 0.5rem 1rem;
  background-color: #5cb85c;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #4cae4c;
}
</style>