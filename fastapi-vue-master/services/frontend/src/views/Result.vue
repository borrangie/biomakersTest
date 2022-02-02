<template>
  <div v-if="result">
    <p><strong>Patient:</strong> {{ result.patient }}</p>
    <p><strong>Result:</strong> {{ result.result }}</p>
    <p><strong>Gen:</strong> {{ result.gen }}</p>
    <p><strong>Author:</strong> {{ result.author.username }}</p>

    <div v-if="user.id === result.author.id">
      <p><router-link :to="{name: 'EditResult', params:{id: result.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeResult()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Result',
  props: ['id'],
  async created() {
    try {
      await this.viewResult(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ result: 'stateResult', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewResult', 'deleteResult']),
    async removeResult() {
      try {
        await this.deleteResult(this.id);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
      }
    }
  },
};
</script>
