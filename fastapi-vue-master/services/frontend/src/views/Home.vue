<template>
  <section>
    <div v-if="isLoggedIn" id="logout">
      <h1>Stats</h1>
      <hr/><br/>
      <div class="card" style="width: 20rem;">
        <div class="card-body">
          <h3>All results:</h3>
            <p><strong>Positive results:</strong> {{  }}</p>
            <p>In total: {{  }}</p>
        </div>
      </div>
      <div class="card" style="width: 20rem;">
        <div class="card-body">
          <h3>Results per gen type:</h3>
          <p><strong>Positive results:</strong> {{  }}</p>
          <p>In total: {{  }}</p>
        </div>
      </div>
      <div class="card" style="width: 20rem;">
        <div class="card-body">
            <h3>My results:</h3>
            <p><strong>My uploaded results:</strong> {{  }}</p>
            <p>In total: {{  }}</p>
        </div>
      </div>
      <p id="logout">Click <a href="/dashboard">here</a> to view or add results.</p>

    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>
<script>

export default {
  name: 'Home',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
}
</script>
