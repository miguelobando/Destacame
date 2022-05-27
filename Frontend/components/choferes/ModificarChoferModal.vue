<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Editar chofer</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="requestStatus !== 0">
        <div v-if="requestStatus === 200">
          <div class="is-fullwidth has-text-centered has-background-success">
            <p>Chofer editado exitosamente</p>
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
            :disabled="requestStatus === 200"
          />
          <input
            v-model="apellido"
            type="text"
            class="input mt-4"
            placeholder="Apellido"
            :disabled="requestStatus === 200"
          />
          <input
            v-model="email"
            type="email"
            class="input mt-4"
            placeholder="Email"
            :disabled="true"
          />
        </div>
      </section>
      <footer class="modal-card-foot">
        <button
          class="button is-success"
          :disabled="requestStatus === 200"
          @click="updateChofer"
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
  name: 'ModificarChoferModal',
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
      email: '',
      nombre: '',
      apellido: '',
      requestStatus: 0,
    }
  },
  watch: {
    open(oldValue, newVaue) {
      this.email = this.current.email
      this.nombre = this.current.nombre
      this.apellido = this.current.apellido
    },
  },
  methods: {
    ...mapActions(['updateData', 'getData']),
    closeModal() {
      this.nombre = ''
      this.apellido = ''
      this.email = ''
      this.requestStatus = 0
      this.$parent.setModalState()
    },
    async updateChofer() {
      const data = {
        nombre: this.nombre,
        apellido: this.apellido,
        email: this.email,
        esChofer: true,
      }
      const resource = 'choferes'
      const key = this.current.email
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
