<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Editar Trayecto</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="requestStatus !== 0">
        <div v-if="requestStatus === 200">
          <div class="is-fullwidth has-text-centered has-background-success">
            <p>Trayecto editado exitosamente</p>
          </div>
        </div>
        <div v-else>
          <div class="is-fullwidth has-text-centered has-background-danger">
            <p>Trayecto invalido o ya registrado</p>
          </div>
        </div>
      </div>
      <div v-if="rutas.length === 0" class="modal-card-body">
        <h3>No hay rutas registradas</h3>
      </div>
      <div v-else>
        <section class="modal-card-body">
          <div class="is-flex is-flex-direction-column">
            <div class="select is-fullwidth">
              <select
                v-model="inicio"
                required
                aria-placeholder="origen"
                :disabled="requestStatus === 200"
              >
                <option disabled value="">Ruta de origen</option>
                <option
                  v-for="rutaItem in rutas"
                  :key="rutaItem.id"
                  :value="rutaItem.id"
                >
                  {{ rutaItem.terminal }} , {{ rutaItem.ciudad }}
                </option>
              </select>
            </div>
            <div class="select is-fullwidth mt-4">
              <select v-model="fin" required :disabled="requestStatus === 200">
                <option disabled value="">Ruta de destino</option>
                <option
                  v-for="rutaItem in rutas"
                  :key="rutaItem.id"
                  :value="rutaItem.id"
                >
                  {{ rutaItem.terminal }} , {{ rutaItem.ciudad }}
                </option>
              </select>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button
            class="button is-success"
            :disabled="requestStatus === 201"
            @click="updateTrayecto"
          >
            Guardar
          </button>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'ModificarTrayectoModal',
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
      fin: '',
      inicio: '',
    }
  },
  computed: mapState(['rutas', 'buses']),
  watch: {
    open(oldVallue, newVaue) {
      this.fin = this.current.fin
      this.inicio = this.current.inicio
    },
  },
  async created() {
    await this.getData({ resource: 'rutas' })
  },
  methods: {
    ...mapActions(['updateData', 'getData']),
    closeModal() {
      this.$parent.setModalState()
      this.fin = ''
      this.inicio = ''
      this.requestStatus = 0
    },
    async updateTrayecto() {
      const data = {
        fin: this.fin,
        inicio: this.inicio,
      }
      const resource = 'trayectos'
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
