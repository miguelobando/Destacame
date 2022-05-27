<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8">
        <h3 class="has-text-centered">Buses</h3>
        <div v-if="buses.length === 0">
          <h3 class="has-text-centered">No hay buses registrados</h3>
        </div>
        <div v-else>
          <TablaBuses />
        </div>
      </div>
      <div class="column is-1">
        <button class="button" @click="setModalState">Agregar bus</button>
        <AgregarBusModal :open="modalState" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'BusesPage',
  data() {
    return {
      modalState: false,
    }
  },
  computed: mapState(['buses']),
  async created() {
    await this.getData({ resource: 'buses' })
    this.getData({ resource: 'choferes' })
  },
  methods: {
    ...mapActions(['getData', 'getBusData', 'getChoferesData']),
    setModalState() {
      this.modalState = !this.modalState
    },
  },
}
</script>

<style></style>
