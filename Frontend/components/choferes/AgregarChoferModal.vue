<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Agregar chofer</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="requestStatus !== 0">
        <div v-if="requestStatus === 201">
          <div class="is-fullwidth has-text-centered has-background-success">
            <p>Chofer registrado exitosamente</p>
          </div>
        </div>
        <div v-else>
          <div class="is-fullwidth has-text-centered has-background-danger">
            <p>Email invalido o ya registrado</p>
          </div>
        </div>
      </div>
      <section class="modal-card-body">
        <div class="is-flex is-flex-direction-column">
          <input
            v-model="nombre"
            type="text"
            class="input"
            placeholder="Nombre"
            :disabled="requestStatus === 201"
          />
          <input
            v-model="apellido"
            type="text"
            class="input mt-4"
            placeholder="Apellido"
            :disabled="requestStatus === 201"
          />
          <input
            v-model="email"
            type="email"
            class="input mt-4"
            placeholder="Email"
            :disabled="requestStatus === 201"
          />
        </div>
      </section>
      <footer class="modal-card-foot">
        <button
          class="button is-success"
          :disabled="requestStatus === 201"
          @click="addChofer"
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
  name: 'AgregarChoferModal',
  props: {
    open: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      email: '',
      nombre: '',
      apellido: '',
      requestStatus: 0,
    }
  },
  methods: {
    ...mapActions(['addData', 'getData']),
    closeModal() {
      this.nombre = ''
      this.apellido = ''
      this.email = ''
      this.requestStatus = 0
      this.$parent.setModalState()
    },
    async addChofer() {
      const data = {
        nombre: this.nombre,
        apellido: this.apellido,
        email: this.email,
        esChofer: true,
      }
      const resource = 'choferes'
      const payload = {
        data,
        resource,
      }
      this.requestStatus = await this.addData(payload)
      this.getData(payload)
    },
  },
}
</script>

<style></style>
