<template>
  <div class="modal" :class="{ 'is-active': open }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Agregar boleto</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <div v-if="reqStatus !== 0">
        <div v-if="reqStatus === 201">
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
          <div v-if="tipoPasajero == ''" class="columns">
            <div class="column">
              <button class="button is-info" @click="tipoPasajero = 'nuevo'">
                Nuevo pasajero
              </button>
            </div>
            <div class="column">
              <button class="button is-primary" @click="tipoPasajero = 'viejo'">
                Antiguo pasajero
              </button>
            </div>
          </div>
          <div v-if="tipoPasajero == 'viejo'">
            <div class="select is-fullwidth mt-4">
              <select v-model="pasajero" :disabled="reqStatus === 201">
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
          <div v-if="tipoPasajero == 'nuevo'">
            <div class="is-flex is-flex-direction-column">
              <input
                v-model="nombre"
                type="text"
                class="input"
                placeholder="Nombre"
                :disabled="reqStatus === 201"
              />
              <input
                v-model="apellido"
                type="text"
                class="input mt-4"
                placeholder="Apellido"
                :disabled="reqStatus === 201"
              />
              <input
                v-model="email"
                type="email"
                class="input mt-4"
                placeholder="Email"
                :disabled="reqStatus === 201"
              />
            </div>
          </div>
          <div class="select is-fullwidth mt-4">
            <select
              v-model="trayecto"
              :disabled="reqStatus === 201"
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
              :disabled="reqStatus === 201"
              @change="filterAsiento"
            >
              <option value="" disabled>Horario</option>
              <option
                v-for="item in horariosFiltered"
                :key="item.id"
                :disabled="reqStatus === 201"
                :value="item.id"
              >
                {{ showLocalTime(item.horario) }}
              </option>
            </select>
          </div>
          <div class="select is-fullwidth mt-4">
            <select v-model="asiento" :disabled="reqStatus === 201">
              <option value="">Asiento</option>
              <option
                v-for="asientoDisponible in asientosFiltered"
                :key="asientoDisponible.id"
                :value="asientoDisponible.id"
                :disabled="reqStatus === 201"
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
          :disabled="reqStatus === 201"
          @click="addBoleto"
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
  name: 'AgregarBoletoModal',
  props: {
    open: {
      type: Boolean,
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
  methods: {
    ...mapActions(['addData', 'getData']),
    async addBoleto() {
      if (this.tipoPasajero === 'nuevo') {
        await this.createBoletoYPasajero()
      } else {
        const data = {
          asiento: this.asiento,
          pasajero: this.pasajero,
          trayecto: this.trayecto,
          horario: this.horario,
        }
        const resource = 'boletos'
        const payload = {
          data,
          resource,
        }
        this.reqStatus = await this.addData(payload)
        this.getData({ resource: 'boletos' })
      }
    },
    async createBoletoYPasajero() {
      let data
      let payload
      let resource
      data = {
        email: this.email,
        nombre: this.nombre,
        apellido: this.apellido,
      }
      resource = 'pasajeros'
      payload = {
        data,
        resource,
      }
      const req = await this.addData(payload)
      if (req === 201) {
        data = {
          asiento: this.asiento,
          pasajero: this.email,
          trayecto: this.trayecto,
          horario: this.horario,
        }
        resource = 'boletos'
        payload = {
          data,
          resource,
        }
        this.addData(payload).then((e) => {
          this.reqStatus = e
          this.getData({ resource: 'boletos' })
        })
      } else {
        this.reqStatus = 409
      }
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
      const newhour = new Date(time).toLocaleTimeString('es-cl')
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
  },
}
</script>

<style></style>
