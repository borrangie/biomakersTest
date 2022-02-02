<template>
  <section>
    <h1>Edit result</h1>
    <hr/><br/>

    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="patient" class="form-label">Patient:</label>
        <input type="text" name="patient" v-model="form.patient" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="result" class="form-label">Result:</label>
        <textarea
          name="result"
          v-model="form.result"
          class="form-control"
        ></textarea>
      </div>
      <div class="mb-3">
        <label for="gen" class="form-label">Gen:</label>
        <textarea
          name="gen"
          v-model="form.gen"
          class="form-control"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'EditResult',
  props: ['id'],
  data() {
    return {
      form: {
        patient: '',
        result: '',
        gen: '',
      },
    };
  },
  created: function() {
    this.GetResult();
  },
  computed: {
    ...mapGetters({ result: 'stateResult' }),
  },
  methods: {
    ...mapActions(['updateResult', 'viewResult']),
    async submit() {
    try {
      let result = {
        id: this.id,
        form: this.form,
      };
      await this.updateResult(result);
      this.$router.push({name: 'Result', params:{id: this.result.id}});
    } catch (error) {
      console.log(error);
    }
    },
    async GetResult() {
      try {
        await this.viewResult(this.id);
        this.form.patient = this.result.patient;
        this.form.result = this.result.result;
        this.form.gen = this.result.gen;
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    }
  },
};
</script>
