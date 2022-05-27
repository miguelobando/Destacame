<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Agregar bus</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="resultadoDeReq !== 0">
        <div v-if="resultadoDeReq === 201">
          <div class="is-fullwidth has-text-centered has-background-success">
            <p>Bus registrado exitosamente</p>
          </div>
        </div>
        <div v-else>
          <div class="is-fullwidth has-text-centered has-background-danger">
            <p>Placa invalida o ya registrada</p>
          </div>
        </div>
      </div>
      <section class="modal-card-body">
        <div class="is-flex is-flex-direction-column">
          <input
            v-model="placa"
            class="input"
            type="text"
            placeholder="Placa"
            :disabled="resultadoDeReq === 201"
          />
          <div class="select is-fullwidth mt-4">
            <select v-model="chofer" :disabled="resultadoDeReq === 201">
              <option disabled>Chofer</option>
              <option value="">Sin Chofer</option>
              <option
                v-for="choferItem in choferes"
                :key="choferItem.email"
                :value="choferItem.email"
              >
                {{ choferItem.email }} ({{ choferItem.apellido }},
                {{ choferItem.nombre }})
              </option>
            </select>
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button
          class="button is-success"
          :disabled="resultadoDeReq === 201"
          @click="addBus"
        >
          Guardar
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'AgregarBusModal',
  props: {
    open: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      chofer: '',
      placa: '',
      resultadoDeReq: 0,
    }
  },
  computed: mapState(['choferes']),
  methods: {
    ...mapActions(['addData', 'getData']),
    async addBus() {
      const data = {
        placa: this.placa,
        chofer: this.chofer,
      }
      const resource = 'buses'
      const payload = {
        resource,
        data,
      }
      this.resultadoDeReq = await this.addData(payload)
      this.getData({ resource: 'buses' })
    },
    closeModal() {
      this.chofer = ''
      this.placa = ''
      this.resultadoDeReq = 0
      this.$parent.setModalState()
    },
  },
}
</script>

<style></style>
