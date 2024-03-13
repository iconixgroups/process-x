<template>
  <div class="company-registration">
    <h1>Company Registration</h1>
    <form @submit.prevent="submitCompanyRegistration">
      <div class="form-group">
        <label for="companyName">Company Name:</label>
        <input type="text" id="companyName" v-model="companyDetails.companyName" required>
      </div>
      <div class="form-group">
        <label for="aliasName">Alias Name:</label>
        <input type="text" id="aliasName" v-model="companyDetails.aliasName" required>
      </div>
      <div class="form-group">
        <label for="companyCode">Company Code:</label>
        <input type="text" id="companyCode" v-model="companyDetails.companyCode" required>
      </div>
      <div class="form-group">
        <label for="registrationDate">Registration Date:</label>
        <input type="date" id="registrationDate" v-model="companyDetails.registrationDate" required>
      </div>
      <div class="form-group">
        <label for="address">Address:</label>
        <input type="text" id="address" v-model="companyDetails.address" required>
      </div>
      <div class="form-group">
        <label for="contactNumber">Contact Number:</label>
        <input type="tel" id="contactNumber" v-model="companyDetails.contactNumber" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="companyDetails.email" required>
      </div>
      <div class="form-group">
        <label for="website">Website:</label>
        <input type="url" id="website" v-model="companyDetails.website">
      </div>
      <div class="form-group">
        <label for="owners">Owners:</label>
        <textarea id="owners" v-model="companyDetails.owners"></textarea>
      </div>
      <button type="submit">Register Company</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CompanyRegistration',
  data() {
    return {
      companyDetails: {
        companyName: '',
        aliasName: '',
        companyCode: '',
        registrationDate: '',
        address: '',
        contactNumber: '',
        email: '',
        website: '',
        owners: ''
      }
    };
  },
  methods: {
    submitCompanyRegistration() {
      const apiUrl = `${process.env.VUE_APP_BASE_API_URL}/company`;
      this.$axios.post(apiUrl, this.companyDetails)
        .then(response => {
          // Handle the response from the server
          console.log('Company registered successfully:', response.data);
          this.$router.push('/dashboard');
        })
        .catch(error => {
          // Handle any errors from the server
          console.error('Error registering company:', error);
        });
    }
  }
};
</script>

<style scoped>
.company-registration {
  max-width: 600px;
  margin: auto;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
}

.form-group input[type="text"],
.form-group input[type="date"],
.form-group input[type="tel"],
.form-group input[type="email"],
.form-group input[type="url"],
.form-group textarea {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
}

button[type="submit"] {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}
</style>