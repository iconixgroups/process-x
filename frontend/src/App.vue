<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
    // Components will be auto-imported on route change
  }
};
</script>

<style>
/* Global styles */
body {
  font-family: 'Arial', sans-serif;
}

#app {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Add other global styles if necessary */
</style>