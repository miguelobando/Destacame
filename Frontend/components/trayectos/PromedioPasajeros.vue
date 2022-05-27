<template>
  <div>
    {{ number }}
  </div>
</template>

<script>
export default {
  name: 'PromedioPasajeros',
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      number: 0,
    }
  },
  mounted() {
    this.getPromedioPasajeros(this.id)
  },
  methods: {
    getPromedioPasajeros(id) {
      this.$axios
        .get(
          `http://127.0.0.1:8000/api/v1/trayectos/${id}/promediopasajeros/1/`
        )
        .then((e) => {
          this.number = e.data
        })
    },
  },
}
</script>

<style></style>
