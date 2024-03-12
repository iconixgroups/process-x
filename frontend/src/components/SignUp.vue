<template>
  <div class="signup-container">
    <div class="social-signin">
      <button @click="socialSignIn('google')" class="social-button google">Sign in with Google</button>
      <button @click="socialSignIn('facebook')" class="social-button facebook">Sign in with Facebook</button>
    </div>
    <form @submit.prevent="emailSignUp" class="email-signup-form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="user.email" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="user.password" required>
      </div>
      <button type="submit" class="signup-button">Sign Up</button>
    </form>
    <div v-if="showOtpField" class="otp-verification">
      <label for="otp">Enter OTP:</label>
      <input type="text" id="otp" v-model="otp" required>
      <button @click="verifyEmail" class="verify-button">Verify</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        email: '',
        password: ''
      },
      otp: '',
      showOtpField: false
    };
  },
  methods: {
    socialSignIn(provider) {
      // Call to backend API to handle social sign-in
      this.$axios.post(`${process.env.VUE_APP_BASE_URL}/auth/social`, { provider })
        .then(response => {
          // Handle successful sign-in
          this.$store.dispatch('auth/setUser', response.data);
          this.$router.push('/dashboard');
        })
        .catch(error => {
          // Handle errors
          console.error('Social sign-in error:', error);
        });
    },
    emailSignUp() {
      // Call to backend API to handle email sign-up
      this.$axios.post(`${process.env.VUE_APP_BASE_URL}/auth/register`, this.user)
        .then(() => {
          // Show OTP field for verification
          this.showOtpField = true;
        })
        .catch(error => {
          // Handle errors
          console.error('Email sign-up error:', error);
        });
    },
    verifyEmail() {
      // Call to backend API to verify email with OTP
      this.$axios.post(`${process.env.VUE_APP_BASE_URL}/auth/verify`, { email: this.user.email, otp: this.otp })
        .then(response => {
          // Handle successful verification
          this.$store.dispatch('auth/setUser', response.data);
          this.$router.push('/dashboard');
        })
        .catch(error => {
          // Handle errors
          console.error('OTP verification error:', error);
        });
    }
  }
};
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
}

.social-signin {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.social-button {
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

.google {
  background-color: #db4437;
  color: white;
}

.facebook {
  background-color: #4267b2;
  color: white;
}

.email-signup-form .form-group {
  margin-bottom: 15px;
}

.email-signup-form label {
  display: block;
}

.email-signup-form input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
}

.signup-button {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border: none;
  cursor: pointer;
}

.otp-verification {
  margin-top: 20px;
}

.otp-verification label {
  display: block;
}

.otp-verification input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}

.verify-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
</style>