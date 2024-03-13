<template>
  <div class="module-publication">
    <h1>Publish Module</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else>
      <div v-if="error" class="error">{{ error }}</div>
      <div v-if="module">
        <h2>{{ module.moduleName }}</h2>
        <p>Module ID: {{ module.moduleId }}</p>
        <button @click="publishModule" :disabled="module.isPublished">Publish</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { BASE_URL } from '../../api/auth.js';

export default {
  name: 'ModulePublication',
  data() {
    return {
      loading: true,
      error: null,
      module: null
    };
  },
  methods: {
    async fetchModule() {
      try {
        const moduleId = this.$route.params.moduleId;
        const response = await axios.get(`${BASE_URL}/settings/module/${moduleId}`);
        this.module = response.data;
        this.loading = false;
      } catch (error) {
        this.error = "Failed to load module data.";
        this.loading = false;
      }
    },
    async publishModule() {
      try {
        const moduleId = this.module.moduleId;
        await axios.post(`${BASE_URL}/publish/module/${moduleId}`, { publish: true });
        this.module.isPublished = true;
        alert('Module published successfully!');
      } catch (error) {
        this.error = "Failed to publish module.";
      }
    }
  },
  created() {
    this.fetchModule();
  }
};
</script>

<style scoped>
.module-publication {
  padding: 20px;
}

.loading {
  color: #888;
}

.error {
  color: red;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #5cb85c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>