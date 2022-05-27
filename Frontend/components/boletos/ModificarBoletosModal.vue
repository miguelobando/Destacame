<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Modificar boleto</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="reqStatus !== 0">
        <div v-if="reqStatus === 200">
          <div class="is-fullwidth has-text-centered has-background-success">
            <p>Boleto registrado exitosamente</p>
          </div>
        </div>
        <div v-else>
          <div class="is-fullwidth has-text-centered has-background-danger">
            <div v-if="reqStatus === 409">
              <p>No se ha podido registrar el pasajero</p>
            </div>
            <div v-else>
              <p>Datos de boleto invalidos</p>
            </div>
          </div>
        </div>
      </div>
      <section class="modal-card-body">
        <div class="is-flex is-flex-direction-column">
          <div v-if="tipoPasajero == 'viejo'">
            <div class="select is-fullwidth mt-4">
              <select v-model="pasajero" :disabled="reqStatus === 200">
                <option value="" disabled>Pasajero</option>
                <option
                  v-for="pasajeroItem in pasajeros"
                  :key="pasajeroItem.email"
                  :value="pasajeroItem.email"
                >
                  {{ pasajeroItem.email }} ({{ pasajeroItem.apellido }},
                  {{ pasajeroItem.nombre }})
                </option>
              </select>
            </div>
          </div>
          <div class="select is-fullwidth mt-4">
            <select
              v-model="trayecto"
              :disabled="reqStatus === 200"
              @change="filterHorario"
            >
              <option value="" disabled>Trayecto</option>
              <option
                v-for="trayectoItem in trayectos"
                :key="trayectoItem.id"
                :value="trayectoItem.id"
              >
                Desde: {{ showRuta(trayectoItem.inicio) }}. Hasta:
                {{ showRuta(trayectoItem.fin) }}
              </option>
            </select>
          </div>
          <div class="select is-fullwidth mt-4">
            <select
              v-model="horario"
              :disabled="reqStatus === 200"
              @change="filterAsiento"
            >
              <option value="" disabled>Horario</option>
              <option
                v-for="item in horariosFiltered"
                :key="item.id"
                :disabled="reqStatus === 200"
                :value="item.id"
              >
                {{ showLocalTime(item.horario) }}
              </option>
            </select>
          </div>
          <div class="select is-fullwidth mt-4">
            <select v-model="asiento" :disabled="reqStatus === 200">
              <option value="">Asiento</option>
              <option :value="current.asiento">
                {{ getNumeroAsiento(current.asiento) }}
              </option>
              <option
                v-for="asientoDisponible in asientosFiltered"
                :key="asientoDisponible.id"
                :value="asientoDisponible.id"
              >
                {{ asientoDisponible.numeroAsiento }}
              </option>
            </select>
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button
          class="button is-success"
          :disabled="reqStatus === 200"
          @click="updateBoleto"
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
  name: 'ModificarBoletoModal',
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
      pasajero: '',
      asiento: '',
      trayecto: '',
      horario: '',
      reqStatus: 0,
      tipoPasajero: '',
      horariosFiltered: [],
      asientosFiltered: [],
      nombre: '',
      apellido: '',
      email: '',
    }
  },
  computed: {
    ...mapState([
      'pasajeros',
      'asientos',
      'trayectos',
      'rutas',
      'horarios',
      'buses',
      'boletos',
    ]),
  },
  watch: {
    open(oldValue, newValue) {
      this.pasajero = this.current.pasajero
      this.trayecto = this.current.trayecto
      this.tipoPasajero = 'viejo'
      this.horario = this.current.horario
      this.filterHorario()
      this.asiento = this.current.asiento
      this.filterAsiento()
    },
  },
  methods: {
    ...mapActions(['updateData', 'getData']),
    async updateBoleto() {
      const data = {
        asiento: this.asiento,
        pasajero: this.pasajero,
        trayecto: this.trayecto,
        horario: this.horario,
      }
      const resource = 'boletos'
      const key = this.current.id
      const payload = {
        data,
        resource,
        key,
      }
      this.reqStatus = await this.updateData(payload)
      this.getData({ resource })
    },

    closeModal() {
      this.asiento = ''
      this.trayecto = ''
      this.horario = ''
      this.reqStatus = 0
      this.horariosFiltered = []
      this.asientosFiltered = []
      this.reqStatus = 0
      this.$parent.setModalState()
      this.tipoPasajero = ''
      this.nombre = ''
      this.apellido = ''
      this.email = ''
    },
    showRuta(id) {
      const ruta = this.rutas.find((e) => e.id === id)
      if (ruta === undefined) return ''
      else return `${ruta.terminal}, ${ruta.ciudad}`
    },
    showLocalTime(time) {
      const newdate = new Date(time).toLocaleDateString('es-cl')
      const newhour = new Date(time).toLocaleTimeString('es-cl').slice(0, -3)
      return `${newdate} ${newhour}`
    },
    filterHorario() {
      this.horariosFiltered = this.horarios.filter(
        (e) => e.trayecto === this.trayecto
      )
    },
    filterAsiento() {
      const horario = this.horarios.find((e) => e.id === this.horario)
      const asientosAll = this.asientos.filter((e) => e.bus === horario.bus)
      this.asientosFiltered = asientosAll.reduce((p, c) => {
        if (
          this.boletos.find(
            (e) =>
              e.asiento === c.id &&
              e.trayecto === this.trayecto &&
              e.horario === this.horario
          )
        ) {
          return [...p]
        } else {
          return [...p, c]
        }
      }, [])
    },
    getNumeroAsiento(id) {
      const asiento = this.asientos.find((e) => e.id === id)
      return asiento?.numeroAsiento
    },
  },
}
</script>

<style></style>
