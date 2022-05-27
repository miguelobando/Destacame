<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Editar ruta</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="requestStatus !== 0">
        <div v-if="requestStatus === 200">
          <div class="is-fullwidth has-text-centered has-background-success">
            <p>Ruta registrada exitosamente</p>
          </div>
        </div>
        <div v-else>
          <div class="is-fullwidth has-text-centered has-background-danger">
            <p>Terminal invalido o ya registrado</p>
          </div>
        </div>
      </div>
      <section class="modal-card-body">
        <div class="is-flex is-flex-direction-column">
          <input
            v-model="terminal"
            type="text"
            class="input"
            placeholder="Terminal"
            :disabled="requestStatus === 200"
          />
          <input
            v-model="ciudad"
            type="text"
            class="input mt-4"
            placeholder="Ciudad"
            :disabled="requestStatus === 200"
          />
        </div>
      </section>
      <footer class="modal-card-foot">
        <button
          class="button is-success"
          :disabled="requestStatus === 200"
          @click="updateRuta"
        >
          Guardar
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'ModificarRutaModal',
  props: {
    open: {
      type: Boolean,
      required: true,
    },
    current: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      requestStatus: 0,
      terminal: '',
      ciudad: '',
    }
  },
  watch: {
    open(oldValue, newVaue) {
      this.terminal = this.current.terminal
      this.ciudad = this.current.ciudad
    },
  },
  methods: {
    ...mapActions(['updateData', 'getData']),
    closeModal() {
      this.$parent.setModalState()
      this.terminal = ''
      this.ciudad = ''
      this.requestStatus = 0
    },
    async updateRuta() {
      const data = {
        terminal: this.terminal,
        ciudad: this.ciudad,
      }
      const resource = 'rutas'
      const key = this.current.id
      const payload = {
        data,
        resource,
        key,
      }
      this.requestStatus = await this.updateData(payload)
      this.getData({ resource })
    },
  },
}
</script>

<style></style>
