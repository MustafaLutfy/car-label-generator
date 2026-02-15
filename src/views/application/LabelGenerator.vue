<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-50 via-white to-primary-100">
    <!-- Header -->
    <header class="bg-white shadow-md">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <h1 class="text-2xl font-bold text-primary">Car Label Generator</h1>
        </div>
        <button @click="handleLogout"
          class="px-4 py-2 text-primary hover:bg-primary-50 rounded-lg transition-colors font-semibold">
          Logout
        </button>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="bg-white rounded-2xl shadow-lg p-6 lg:p-8">
        <!-- Actions Bar -->
        <div class="flex flex-col sm:flex-row gap-4 mb-8 justify-between items-start sm:items-center">
          <div class="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
            <input type="file" ref="fileInput" @change="handleFileUpload" accept=".xlsx,.xls,.csv" class="hidden" />
            <button @click="$refs.fileInput.click()"
              class="flex items-center justify-center gap-2 px-6 py-3 bg-primary text-white font-semibold rounded-lg hover:bg-primary-600 transition-colors">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              Import Excel/CSV
            </button>
            <button @click="addNewItem"
              class="flex items-center justify-center gap-2 px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
              Add Item
            </button>
            <button v-if="items.length > 0" @click="clearAllData"
              class="px-6 py-3 border-2 border-red-500 text-red-500 font-semibold rounded-lg hover:bg-red-50 transition-colors">
              Clear All
            </button>
          </div>

          <button v-if="items.length > 0" @click="exportAllToPDF" :disabled="isExporting"
            class="flex items-center justify-center gap-2 px-6 py-3 bg-green-600 text-white font-semibold rounded-lg hover:bg-green-700 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed">
            <svg v-if="!isExporting" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <svg v-else class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none"
              viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
              </path>
            </svg>
            {{ isExporting ? 'Generating PDF...' : 'Export All to PDF' }}
          </button>
        </div>

        <!-- Data Table -->
        <div v-if="items.length > 0" class="overflow-x-auto border border-gray-200 rounded-lg">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Manufacturer</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Model</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  VIN</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Prod. Date</th>
                <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="item in items" :key="item.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ item.manufacturerName }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ item.model }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-mono text-gray-600">{{ item.vinNumber }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ item.productionDate }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <button @click="openEditModal(item)" class="text-primary hover:text-primary-700 mr-4">Edit</button>
                  <button @click="deleteItem(item.id)" class="text-red-600 hover:text-red-900">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Empty State -->
        <div v-else class="text-center py-12 border-2 border-dashed border-gray-300 rounded-lg">
          <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">No data imported</h3>
          <p class="mt-1 text-sm text-gray-500">Upload an Excel or CSV file to get started.</p>
        </div>
      </div>
    </main>

    <!-- Edit Modal -->
    <div v-if="isEditModalOpen" class="fixed inset-0 z-50 overflow-y-auto" aria-labelledby="modal-title" role="dialog"
      aria-modal="true">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <!-- Background overlay -->
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"
          @click="closeEditModal"></div>

        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

        <!-- Modal panel -->
        <div
          class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-6xl sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="flex justify-between items-center mb-6">
              <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">Edit Label</h3>
              <button @click="closeEditModal" class="text-gray-400 hover:text-gray-500">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <!-- Form -->
              <div class="space-y-4 max-h-[60vh] overflow-y-auto pr-2">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Manufacturer Name (اسم الصانع)</label>
                    <input v-model="editingItem.manufacturerName" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Country (بلد الانتاج)</label>
                    <input v-model="editingItem.countryOfProduction" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Production Date (تاريخ
                      الانتاج)</label>
                    <input v-model="editingItem.productionDate" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Model Year (سنة الطراز)</label>
                    <input v-model="editingItem.modelYear" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Max Weight (الوزن الاقصى)</label>
                    <input v-model="editingItem.maxWeight" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Max Weight/Axle (الوزن/محور)</label>
                    <input v-model="editingItem.maxWeightPerAxle" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div class="md:col-span-2">
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Compliance Note (ملاحظة
                      المطابقة)</label>
                    <textarea v-model="editingItem.complianceNote" rows="2"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary"></textarea>
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">VIN (الرقم التعريفي)</label>
                    <input v-model="editingItem.vinNumber" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Classification (صنف المركبة)</label>
                    <input v-model="editingItem.vehicleClassification" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Engine (المحرك)</label>
                    <input v-model="editingItem.engine" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div>
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Model (الطراز)</label>
                    <input v-model="editingItem.model" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                  <div class="md:col-span-2">
                    <label class="block mb-1 text-sm font-semibold text-gray-700">Factory (المصنع)</label>
                    <input v-model="editingItem.factory" type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary" />
                  </div>
                </div>
              </div>

              <!-- Preview -->
              <div class="flex flex-col items-center justify-center bg-gray-50 rounded-lg p-4">
                <h4 class="text-lg font-bold text-gray-700 mb-4">Preview</h4>
                <div class="border-4 border-black" style="width: 400px; height: 200px;">
                  <LabelTemplate :data="editingItem" />
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="saveEdit" type="button"
              class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-primary text-base font-medium text-white hover:bg-primary-700 focus:outline-none sm:ml-3 sm:w-auto sm:text-sm">
              Save Changes
            </button>
            <button @click="closeEditModal" type="button"
              class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Hidden Export Container -->
    <div class="absolute top-0 left-0 -z-50 opacity-0 pointer-events-none"
      style="width: 400px; height: 200px; overflow: hidden;">
      <div id="export-container"  style="width: 400px; height: 200px;">
        <LabelTemplate v-show="exportItem" :data="exportItem || {}" />
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, nextTick, defineComponent, h, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import * as XLSX from 'xlsx'
import html2canvas from 'html2canvas'
import jsPDF from 'jspdf'
import QRCode from 'qrcode'

// --- Internal Component for Label Template ---
// Defining it here to reuse in Preview and Export
const LabelTemplate = defineComponent({
  props: ['data'],
  setup(props) {
    const qrCodeDataUrl = ref('')
    const defaultComplianceNote = 'تطابق هذه المركبة المواصفات المعتمدة من الجهاز المركزي للتقييس والسيطرة النوعية /العراق'

    const generateQRCode = async () => {
      const d = props.data || {}
      // Create readable text-based format for QR code with line breaks - includes ALL data
      const lines = []

      if (d.manufacturerName) lines.push(`Manufacturer: ${d.manufacturerName}`)
      if (d.countryOfProduction) lines.push(`Country: ${d.countryOfProduction}`)
      if (d.productionDate) lines.push(`Prod Date: ${d.productionDate}`)
      if (d.modelYear) lines.push(`Year: ${d.modelYear}`)
      if (d.maxWeight) lines.push(`Max Weight: ${d.maxWeight}`)
      if (d.maxWeightPerAxle) lines.push(`Axle Weight: ${d.maxWeightPerAxle}`)
      if (d.complianceNote) lines.push(`Compliance: ${d.complianceNote}`)
      if (d.vinNumber) lines.push(`VIN: ${d.vinNumber}`)
      if (d.vehicleClassification) lines.push(`Class: ${d.vehicleClassification}`)
      if (d.engine) lines.push(`Engine: ${d.engine}`)
      if (d.model) lines.push(`Model: ${d.model}`)
      if (d.factory) lines.push(`Factory: ${d.factory}`)

      const qrText = lines.join('\n')

      try {
        qrCodeDataUrl.value = await QRCode.toDataURL(qrText, {
          width: 120,
          margin: 0,
          errorCorrectionLevel: 'L'
        })
      } catch (error) {
        console.error('Error generating QR code:', error)
      }
    }

    onMounted(() => {
      generateQRCode()
    })

    // Watch for data changes to regenerate QR code
    watch(() => props.data, () => {
      generateQRCode()
    }, { deep: true })

    return () => {
      const d = props.data || {}
      return h('div', {
        class: 'bg-white w-full h-full',
        style: {
          direction: 'rtl',
          fontFamily: "'Arial', sans-serif",
          padding: '0px 8px 10px 8px',
          fontSize: '12.2px',
          lineHeight: '1.2',
          position: 'relative'
        }
      }, [
        h('div', { style: { display: 'flex', flexDirection: 'column', gap: '3px' } }, [
          // Row 1
          h('div', { style: { display: 'grid', gridTemplateColumns: '1fr 0.8fr', gap: '2px' } }, [
            h('div', { style: { textAlign: 'right' } }, [
              h('p', { style: { margin: 0, fontWeight: 'bold' } }, ['اسم الصانع: ', h('span', d.manufacturerName || '')])
            ]),
            h('div', { style: { textAlign: 'right' } }, [
              h('p', { style: { margin: 0, fontWeight: 'bold' } }, ['بلد الانتاج: ', h('span', d.countryOfProduction || '')])
            ])
          ]),
          // Row 2
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right' } }, ['سنة الطراز: ', h('span', d.modelYear || '')])
          ]),
          // Row 3
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right' } }, ['الوزن الاقصى للمركبة بـ (كغ): ', h('span', d.maxWeight || '')])
          ]),
          // Row 4 - Axle Weight Label with Front/Rear Values on Same Line
          h('div', { style: { display: 'flex', alignItems: 'center' } }, [
            h('p', { style: { margin: 0, fontWeight: 'bold' } }, 'الوزن الاقصى على كل محور بـ (كغ):'),
            h('div', { style: { display: 'flex', gap: '20px', marginRight: '20px' } }, [
              h('p', { style: { margin: 0, fontWeight: 'bold' } }, ['خلفي: ', h('span', d.maxWeightPerAxle ? String(d.maxWeightPerAxle).split('/')[1]?.trim() || '' : '')]),
              h('p', { style: { margin: 0, fontWeight: 'bold' } }, ['أمامي: ', h('span', d.maxWeightPerAxle ? String(d.maxWeightPerAxle).split('/')[0]?.trim() || '' : '')])
            ])
          ]),
          // Row 5 - Compliance Note
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right', lineHeight: '1.3' } }, d.complianceNote || defaultComplianceNote)
          ]),
          // Row 6 - VIN
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right' } }, [
              'الرقم التعريفي للمركبة ',
              h('span', { style: { direction: 'ltr', display: 'inline-block' } }, 'VIN'),
              ':',
              h('span', { style: { fontFamily: 'monospace', fontSize: '12.2px' } }, d.vinNumber || '')
            ])
          ]),
          // Row 7 - Classification
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right' } }, ['صنف المركبة: ', h('span', d.vehicleClassification || '')])
          ]),
          // Row 8 - Engine
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right' } }, ['المحرك: ', h('span', d.engine || '')])
          ]),
          // Row 9 - Model
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right' } }, [
              'الطراز: ',
              h('span', { class: 'text-[12.5px] transform -translate-y-[1px]', style: { direction: 'ltr', display: 'inline-block' } }, d.model || '')
            ])
          ]),
          // Row 10 - Factory
          h('div', {}, [
            h('p', { style: { margin: 0, fontWeight: 'bold', textAlign: 'right' } }, ['المصنع: ', h('span', d.factory || '')])
          ])
        ]),
        // QR Code in bottom-left corner
        qrCodeDataUrl.value ? h('img', {
          src: qrCodeDataUrl.value,
          style: {
            position: 'absolute',
            bottom: '5px',
            left: '5px',
            width: '70px',
            height: '70px',
            zIndex: '10',
            imageRendering: 'crisp-edges'
          },
          alt: 'QR Code'
        }) : null
      ])
    }
  }
})

const router = useRouter()
const fileInput = ref(null)
const items = ref([])
const isEditModalOpen = ref(false)
const editingItem = ref({})
const exportItem = ref(null)
const isExporting = ref(false)

const defaultComplianceNote = 'تطابق هذه المركبة المواصفات المعتمدة من الجهاز المركزي للتقييس والسيطرة النوعية /العراق'

const addNewItem = () => {
  const newItem = {
    id: Date.now(),
    manufacturerName: '',
    countryOfProduction: '',
    productionDate: '',
    modelYear: '',
    maxWeight: '',
    maxWeightPerAxle: '',
    complianceNote: defaultComplianceNote,
    vinNumber: '',
    vehicleClassification: '',
    engine: '',
    model: '',
    factory: ''
  }
  items.value.push(newItem)
  openEditModal(newItem)
}

const handleLogout = () => {
  localStorage.removeItem('isAuthenticated')
  localStorage.removeItem('user')
  router.push('/')
}

const handleFileUpload = async (event) => {
  const file = event.target.files[0]
  if (!file) return

  try {
    const data = await file.arrayBuffer()
    const workbook = XLSX.read(data)
    const sheetName = workbook.SheetNames[0]
    const worksheet = workbook.Sheets[sheetName]
    const jsonData = XLSX.utils.sheet_to_json(worksheet)

    if (jsonData.length > 0) {
      const newItems = jsonData.map((row, index) => ({
        id: Date.now() + index,
        manufacturerName: row['Manufacturer Name'] || row['manufacturerName'] || '',
        countryOfProduction: row['Country'] || row['countryOfProduction'] || '',
        productionDate: row['Production Date'] || row['productionDate'] || '',
        modelYear: row['Model Year'] || row['modelYear'] || '',
        maxWeight: row['Max Weight'] || row['maxWeight'] || '',
        maxWeightPerAxle: row['Max Weight Per Axle'] || row['maxWeightPerAxle'] || '',
        complianceNote: row['Compliance Note'] || row['complianceNote'] || defaultComplianceNote,
        vinNumber: row['VIN'] || row['vinNumber'] || '',
        vehicleClassification: row['Classification'] || row['vehicleClassification'] || '',
        engine: row['Engine'] || row['engine'] || '',
        model: row['Model'] || row['model'] || '',
        factory: row['Factory'] || row['factory'] || ''
      }))

      items.value = [...items.value, ...newItems]
    }
  } catch (error) {
    console.error('Error reading file:', error)
    alert('Error reading file. Please make sure it is a valid Excel or CSV file.')
  }

  event.target.value = ''
}

const clearAllData = () => {
  if (confirm('Are you sure you want to clear all data?')) {
    items.value = []
  }
}

const deleteItem = (id) => {
  if (confirm('Are you sure you want to delete this item?')) {
    items.value = items.value.filter(item => item.id !== id)
  }
}

const openEditModal = (item) => {
  editingItem.value = { ...item } // Create a copy
  isEditModalOpen.value = true
}

const closeEditModal = () => {
  isEditModalOpen.value = false
  editingItem.value = {}
}

const saveEdit = () => {
  const index = items.value.findIndex(i => i.id === editingItem.value.id)
  if (index !== -1) {
    items.value[index] = { ...editingItem.value }
  }
  closeEditModal()
}

const exportAllToPDF = async () => {
  if (items.value.length === 0) return

  isExporting.value = true
  const element = document.getElementById('export-container')

  if (!element) {
    console.error('Export container not found')
    alert('Export container not found. Please refresh the page and try again.')
    isExporting.value = false
    return
  }

  try {
    await document.fonts.ready

    // PDF dimensions: 10cm x 5cm
    const pdfWidthMm = 100
    const pdfHeightMm = 50
    const scale = 5

    const pdf = new jsPDF({
      orientation: 'landscape',
      unit: 'mm',
      format: [pdfWidthMm, pdfHeightMm],
      compress: false
    })

    for (let i = 0; i < items.value.length; i++) {
      try {
        // Update the hidden export item
        exportItem.value = items.value[i]

        // Wait for DOM update
        await nextTick()
        // Small delay to ensure rendering is complete (sometimes needed for fonts/layout)
        await new Promise(resolve => setTimeout(resolve, 100))

        const canvas = await html2canvas(element, {
          scale: scale,
          useCORS: true,
          allowTaint: true,
          logging: false,
          letterRendering: true,
          backgroundColor: '#ffffff'
        })

        const imgData = canvas.toDataURL('image/png', 1.0)

        if (i > 0) {
          pdf.addPage([pdfWidthMm, pdfHeightMm], 'landscape')
        }

        pdf.addImage(imgData, 'PNG', 0, 0, pdfWidthMm, pdfHeightMm, '', 'FAST')
      } catch (itemError) {
        console.error(`Error exporting item ${i + 1}:`, itemError)
        // Continue with next item instead of stopping
      }
    }

    pdf.save(`car-labels-export-${new Date().toISOString().slice(0, 10)}.pdf`)

  } catch (error) {
    console.error('Error exporting PDF:', error)
    alert('Failed to export PDF. Please try again.')
  } finally {
    isExporting.value = false
    exportItem.value = null
  }
}
</script>

<style scoped>
#label-content {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

#label-content * {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Ensure consistent rendering for PDF export */
#label-content p {
  margin: 0;
  line-height: 1.4;
  text-rendering: optimizeLegibility;
}

/* Better Arabic text rendering */
#label-content p,
#label-content span {
  font-feature-settings: normal;
  font-variant-ligatures: normal;
  -webkit-font-feature-settings: normal;
}
/* Reuse existing styles if needed */
</style>