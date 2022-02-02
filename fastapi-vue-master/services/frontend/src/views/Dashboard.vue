<template>
  <div>
    <section>
      <h1>Add new result</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="patient" class="form-label">Patient's name:</label>
          <input type="text" name="patient" v-model="form.patient" class="form-control" />
        </div>
        <div id="v-model-select" class="demo">
          <label for="result" class="form-label">Result: </label>
          <select v-model="form.result" name="result">
            <option disabled value="">Select one</option>
            <option>Positive</option>
            <option>Negative</option>
            <option>Insufficient</option>
            <option>Cancelled</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="gen" class="form-label">Gen type:</label>
          <textarea
            name="gen"
            v-model="form.gen"
            class="form-control"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Results</h1>
      <hr/><br/>

      <div v-if="results.length">
        <div v-for="result in results" :key="result.id" class="results">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Patient:</strong> {{ result.patient }}</li>
                <li><strong>Doctor:</strong> {{ result.author.username }}</li>
                <li><strong>Result:</strong> {{ result.result }}</li>
                <li><strong>Gen:</strong> {{ result.gen }}</li>
                <li><router-link :to="{name: 'Result', params:{id: result.id}}">View more</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Dashboard',
  data() {
    return {
      form: {
        patient: '',
        result: '',
        gen:'',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getResults');
  },
  computed: {
    ...mapGetters({ results: 'stateNotes'}),
  },
  methods: {
    ...mapActions(['createResult']),
    async submit() {
      await this.createResult(this.form);
    },
  },
};
</script>
