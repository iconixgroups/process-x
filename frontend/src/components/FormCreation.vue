<template>
  <div class="form-creation">
    <h1>Form Creation</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else>
      <form @submit.prevent="submitForm">
        <div class="form-section">
          <h2>Header</h2>
          <input type="text" v-model="form.header.title" placeholder="Form Title" required>
          <input type="text" v-model="form.header.description" placeholder="Form Description">
        </div>

        <div class="form-section">
          <h2>Requestor Details</h2>
          <input type="text" v-model="form.requestor.name" placeholder="Requestor Name" required>
          <input type="email" v-model="form.requestor.email" placeholder="Requestor Email" required>
        </div>

        <div class="form-section">
          <h2>Item Level Details</h2>
          <input type="text" v-model="form.item.name" placeholder="Item Name" required>
          <input type="number" v-model="form.item.quantity" placeholder="Quantity" required>
        </div>

        <div class="form-section">
          <h2>Signatories Details</h2>
          <input type="text" v-model="form.signatories.approver" placeholder="Approver Name" required>
          <input type="text" v-model="form.signatories.reviewer" placeholder="Reviewer Name" required>
        </div>

        <div class="form-section">
          <h2>Footer</h2>
          <textarea v-model="form.footer.notes" placeholder="Additional Notes"></textarea>
        </div>

        <button type="submit">Create Form</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FormCreation',
  data() {
    return {
      loading: false,
      form: {
        header: {
          title: '',
          description: ''
        },
        requestor: {
          name: '',
          email: ''
        },
        item: {
          name: '',
          quantity: null
        },
        signatories: {
          approver: '',
          reviewer: ''
        },
        footer: {
          notes: ''
        }
      }
    };
  },
  methods: {
    submitForm() {
      this.loading = true;
      const apiUrl = `${process.env.VUE_APP_BASE_API_URL}/design/form`;
      this.$axios.post(apiUrl, this.form)
        .then(response => {
          this.loading = false;
          // Handle success
          console.log('Form created:', response.data);
          this.$emit('formCreated', response.data);
        })
        .catch(error => {
          this.loading = false;
          // Handle error
          console.error('Error creating form:', error);
        });
    }
  }
};
</script>

<style scoped>
.form-creation {
  max-width: 600px;
  margin: auto;
}

.form-section {
  margin-bottom: 20px;
}

.loading {
  text-align: center;
}
</style>