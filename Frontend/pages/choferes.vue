<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8">
        <h3 class="has-text-centered">Choferes</h3>
        <div v-if="choferes.length === 0">
          <h3 class="has-text-centered">No hay choferes registrados</h3>
        </div>
        <div v-else>
          <TablaChoferes :data="choferes" />
        </div>
      </div>
      <div class="column is-1">
        <button class="button" @click="setModalState()">Agregar chofer</button>
        <AgregarChoferModal :open="modalState" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'ChoferesPage',
  data() {
    return {
      modalState: false,
    }
  },
  computed: mapState(['choferes']),
  created() {
    this.getData({ resource: 'choferes' })
  },
  methods: {
    ...mapActions(['getData']),
    setModalState() {
      this.modalState = !this.modalState
    },
  },
}
</script>

<style></style>
