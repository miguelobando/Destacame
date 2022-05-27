<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Agregar Horario</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="reqStatus !== 0">
        <div v-if="reqStatus === 201">
          <div class="is-fullwidth has-text-centered has-background-success">
            <p>Horario registrado exitosamente</p>
          </div>
        </div>
        <div v-else>
          <div class="is-fullwidth has-text-centered has-background-danger">
            <p>Horario invalido o ya registrada</p>
          </div>
        </div>
      </div>
      <section class="modal-card-body">
        <div class="is-flex is-flex-direction-column">
          <div class="select is-fullwidth mt-4">
            <select v-model="trayecto" :disabled="reqStatus === 201">
              <option disabled>Trayecto</option>
              <option value="">Sin trayecto</option>
              <option
                v-for="trayectoItem in trayectos"
                :key="trayectoItem.id"
                :value="trayectoItem.id"
              >
                {{ getNombreRuta(trayectoItem.inicio) }} ->
                {{ getNombreRuta(trayectoItem.fin) }}
              </option>
            </select>
          </div>
          <input v-model="fecha" class="mt-4" name="fecha" type="date" />
          <input v-model="hora" class="mt-4" name="hora" type="time" />
          <div class="select is-fullwidth mt-4">
            <select v-model="bus" :disabled="reqStatus === 201">
              <option disabled>Bus</option>
              <option value="">Sin Bus</option>
              <option
                v-for="busItem in buses"
                :key="busItem.placa"
                :value="busItem.placa"
              >
                Bus: {{ busItem.placa }}
                {{
                  busItem.chofer !== null ? `- Chofer: ${busItem.chofer}` : ''
                }}
              </option>
            </select>
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button
          class="button is-success"
          :disabled="reqStatus === 201"
          @click="addHorario()"
        >
          Guardar
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'AgregarHorarioModal',
  props: {
    open: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      reqStatus: 0,
      trayecto: '',
      fecha: '',
      hora: '',
      bus: '',
    }
  },
  computed: mapState(['trayectos', 'rutas', 'buses']),
  methods: {
    ...mapActions(['addData', 'getData']),
    closeModal() {
      this.reqStatus = 0
      this.trayecto = ''
      this.fecha = ''
      this.hora = ''
      this.bus = ''
      this.$parent.setModalState()
    },
    getNombreRuta(id) {
      const ruta = this.rutas.find((e) => e.id === id)
      return `${ruta.terminal}, ${ruta.ciudad}`
    },
    async addHorario() {
      const isoFormat = new Date(`${this.fecha}T${this.hora}`).toISOString()
      const data = {
        trayecto: this.trayecto,
        horario: isoFormat,
        bus: this.bus,
      }
      const resource = 'horarios'
      const payload = {
        data,
        resource,
      }
      this.reqStatus = await this.addData(payload)
      this.getData({ resource })
    },
  },
}
</script>

<style>
input[type='date'],
input[type='time'] {
  -webkit-font-smoothing: antialiased;
  text-size-adjust: 100%;
  box-sizing: inherit;
  margin: 0;
  font-family: BlinkMacSystemFont, -apple-system, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    'Helvetica', 'Arial', sans-serif;
  -webkit-appearance: none;
  align-items: center;
  border: 1px solid transparent;
  box-shadow: none;
  height: 2.5em;
  justify-content: flex-start;
  line-height: 1.5;
  padding-bottom: calc(0.5em - 1px);
  padding-left: calc(0.75em - 1px);
  padding-top: calc(0.5em - 1px);
  position: relative;
  background-color: hsl(0deg, 0%, 100%);
  border-color: rgb(219, 219, 219);
  border-radius: 4px;
  color: hsl(0deg, 0%, 21%);
  cursor: pointer;
  display: block;
  font-size: 1em;
  max-width: 100%;
  outline: none;
  padding-right: 2.5em;
  width: 100%;
}
</style>
