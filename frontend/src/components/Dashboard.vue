<template>
  <div id="dashboardContainer">
    <div class="dashboard-header">
      <h1>Dashboard</h1>
      <select v-model="selectedModule" @change="fetchDashboardData">
        <option disabled value="">Select a Module</option>
        <option v-for="module in modules" :key="module.id" :value="module.id">{{ module.name }}</option>
      </select>
    </div>
    <div v-if="dashboardData" class="dashboard-content">
      <div class="dashboard-item">
        <h2>Submission Volumes</h2>
        <chart-component :data="dashboardData.dataSubmissions" chart-type="bar"></chart-component>
      </div>
      <div class="dashboard-item">
        <h2>Status Breakdown</h2>
        <chart-component :data="dashboardData.statuses" chart-type="pie"></chart-component>
      </div>
    </div>
    <div v-else class="no-data">
      <p>Select a module to view the dashboard.</p>
    </div>
  </div>
</template>

<script>
import ChartComponent from './ChartComponent.vue';
import { BASE_URL } from '../api/base';

export default {
  name: 'Dashboard',
  components: {
    ChartComponent
  },
  data() {
    return {
      selectedModule: '',
      modules: [],
      dashboardData: null
    };
  },
  created() {
    this.fetchModules();
  },
  methods: {
    fetchModules() {
      // Placeholder for fetching modules from the API
      // In a real application, this would be an API call
      this.modules = [
        { id: 'MOD123', name: 'HR Management' },
        // ... other modules
      ];
    },
    fetchDashboardData() {
      if (!this.selectedModule) return;
      const url = `${BASE_URL}/dashboard/${this.selectedModule}`;
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.dashboardData = data;
        })
        .catch(error => {
          console.error('Error fetching dashboard data:', error);
        });
    }
  }
};
</script>

<style scoped>
#dashboardContainer {
  padding: 20px;
}

.dashboard-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.dashboard-content {
  display: flex;
  flex-wrap: wrap;
}

.dashboard-item {
  flex-basis: 50%;
  padding: 10px;
}

.no-data {
  text-align: center;
  padding: 20px;
}
</style>