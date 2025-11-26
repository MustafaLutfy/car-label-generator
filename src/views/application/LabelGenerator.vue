<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-50 via-white to-primary-100">
    <!-- Header -->
    <header class="bg-white shadow-md">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">

          <h1 class="text-2xl font-bold text-primary">Car Label Generator</h1>
        </div>
        <button
          @click="handleLogout"
          class="px-4 py-2 text-primary hover:bg-primary-50 rounded-lg transition-colors font-semibold"
        >
          Logout
        </button>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="bg-white rounded-2xl shadow-lg p-6 lg:p-8">
        <!-- Import Section -->
        <div class="mb-8">
          <h2 class="text-2xl font-bold text-primary mb-4">Import Data</h2>
          <div class="flex flex-col sm:flex-row gap-4">
            <input
              type="file"
              ref="fileInput"
              @change="handleFileUpload"
              accept=".xlsx,.xls,.csv"
              class="hidden"
            />
            <button
              @click="$refs.fileInput.click()"
              class="flex items-center justify-center gap-2 px-6 py-3 bg-primary text-white font-semibold rounded-lg hover:bg-primary-600 transition-colors"
            >
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              Import Excel/CSV
            </button>
            <button
              v-if="labelData.manufacturerName"
              @click="clearData"
              class="px-6 py-3 border-2 border-primary text-primary font-semibold rounded-lg hover:bg-primary-50 transition-colors"
            >
              Clear Data
            </button>
          </div>
          <p class="mt-2 text-[16px] text-gray-600">
            Upload an Excel or CSV file with car label data
          </p>
        </div>

        <!-- Label Preview and Edit Section -->
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
          <!-- Edit Form -->
          <div>
            <h2 class="text-2xl font-bold text-primary mb-4">Edit Label Data</h2>
            <form @submit.prevent class="space-y-4">
              <div>
                <label class="block mb-2 font-semibold text-gray-700">Manufacturer Name (اسم الصانع)</label>
                <input
                  v-model="labelData.manufacturerName"
                  type="text"
                  placeholder="شركة هيونداي موتور"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Country of Production (بلد الانتاج)</label>
                <input
                  v-model="labelData.countryOfProduction"
                  type="text"
                  placeholder="جمهورية التشيك"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Production Date (تاريخ الانتاج)</label>
                <input
                  v-model="labelData.productionDate"
                  type="text"
                  placeholder="2025/11"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Model Year (سنة الطراز)</label>
                <input
                  v-model="labelData.modelYear"
                  type="text"
                  placeholder="2026"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Max Weight (الوزن الاقصى للمركبة)</label>
                <input
                  v-model="labelData.maxWeight"
                  type="text"
                  placeholder="1,500"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Max Weight Per Axle (الوزن الاقصى على كل محور)</label>
                <input
                  v-model="labelData.maxWeightPerAxle"
                  type="text"
                  placeholder="(بالنسبة للشاحنات)"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Compliance Note (ملاحظة المطابقة)</label>
                <textarea
                  v-model="labelData.complianceNote"
                  placeholder="تطابق هذه المركبة المواصفات المعتمدة من الجهاز المركزي للتقييس والسيطرة النوعية /العراق"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                  rows="3"
                ></textarea>
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">VIN Number (الرقم التعريفي)</label>
                <input
                  v-model="labelData.vinNumber"
                  type="text"
                  placeholder="TMAJB81D2SJ516697"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Vehicle Classification (صنف المركبة)</label>
                <input
                  v-model="labelData.vehicleClassification"
                  type="text"
                  placeholder="سيارة متعددة الأغراض"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Engine (المحرك)</label>
                <input
                  v-model="labelData.engine"
                  type="text"
                  placeholder="بنزين 4 سلندر 2000 سي سي"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Model (الطراز)</label>
                <input
                  v-model="labelData.model"
                  type="text"
                  placeholder="Hyundai Tucson NX4e DCT 2.0L SUV AWD 5Doors"
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>

              <div>
                <label class="block mb-2 font-semibold text-gray-700">Factory (المصنع)</label>
                <input
                  v-model="labelData.factory"
                  type="text"
                  placeholder="هيونداي موتور مصنع التشيك ش.م.م."
                  class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                />
              </div>
            </form>
          </div>

          <!-- Label Preview -->
          <div>
            <div class="flex items-center justify-between mb-4">
              <h2 class="text-2xl font-bold text-primary">Label Preview</h2>
              <button
                @click="exportToPDF"
                :disabled="!labelData.manufacturerName"
                class="flex items-center gap-2 px-6 py-3 bg-primary text-white font-semibold rounded-lg hover:bg-primary-600 transition-colors disabled:bg-gray-300 disabled:cursor-not-allowed"
              >
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                Export PDF
              </button>
            </div>

            <!-- Label Card - Exact 10cm × 5cm preview with border -->
            <div class="border-4 border-black mx-auto" style="width: 400px; height: 200px;">
              <div
                id="label-content"
                class="bg-white w-full h-full"
                style="direction: rtl; font-family: 'Arial', sans-serif; padding: 0px 8px 10px 8px; font-size: 12.2px; line-height: 1.2;"
              >
                <div style="display: flex; flex-direction: column; gap: 1px;">
                  <!-- Row 1 - Two columns -->
                  <div style="display: grid; grid-template-columns: 0.8fr 1fr; gap: 2px;">
                    <div style="text-align: right;">
                      <p  style="margin: 0; font-weight: bold;">بلد الانتاج: <span>{{ labelData.countryOfProduction || '' }}</span></p>
                    </div>
                    <div style="text-align: right;">
                      <p style="margin: 0; font-weight: bold;">اسم الصانع: <span>{{ labelData.manufacturerName || '' }}</span></p>
                    </div>
                  </div>

                  <!-- Row 2 - Two columns -->
                  <div style="display: grid; grid-template-columns: 0.8fr 1fr; gap: 2px;">
                    <div style="text-align: right;">
                      <p style="margin: 0; font-weight: bold;">سنة الطراز: <span>{{ labelData.modelYear || '' }}</span></p>
                    </div>
                    <div style="text-align: right;">
                      <p style="margin: 0; font-weight: bold;">تاريخ الانتاج: <span>{{ labelData.productionDate || '' }}</span></p>
                    </div>
                  </div>

                  <!-- Row 3 - Full width -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right;">الوزن الاقصى للمركبة بـ (كغ): <span>{{ labelData.maxWeight || '' }}</span></p>
                  </div>

                  <!-- Row 4 - Full width -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right;">الوزن الاقصى على كل محور بـ (كغ) (بالنسبة للشاحنات): <span>{{ labelData.maxWeightPerAxle || '' }}</span></p>
                  </div>

                  <!-- Row 5 - Compliance Note -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right; line-height: 1.3;">
                      {{ labelData.complianceNote || defaultComplianceNote }}
                    </p>
                  </div>

                  <!-- Row 6 - VIN -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right;">الرقم التعريفي للمركبة <span style="direction: ltr; display: inline-block;">VIN</span>:<span class="text-[14.5px] transform -translate-y-[2px]"  style="font-family: monospace;">{{ labelData.vinNumber || '' }}</span></p>
                  </div>
 
                  <!-- Row 7 - Vehicle Classification -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right;">صنف المركبة: <span>{{ labelData.vehicleClassification || '' }}</span></p>
                  </div>

                  <!-- Row 8 - Engine -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right;">المحرك: <span>{{ labelData.engine || '' }}</span></p>
                  </div>

                  <!-- Row 9 - Model -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right;">الطراز: <span class="text-[12.5px] transform -translate-y-[1px]" style="direction: ltr; display: inline-block;">{{ labelData.model || '' }}</span></p>
                  </div>

                  <!-- Row 10 - Factory -->
                  <div>
                    <p style="margin: 0; font-weight: bold; text-align: right;">المصنع: <span>{{ labelData.factory || '' }}</span></p>
                  </div>
                </div>
              </div>
            </div>

            <p class="mt-4 text-[16px] text-gray-600 text-center">
              This preview shows how your label will appear in the PDF
            </p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import * as XLSX from 'xlsx'
import html2canvas from 'html2canvas'
import jsPDF from 'jspdf'

const router = useRouter()
const fileInput = ref(null)

const defaultComplianceNote = 'تطابق هذه المركبة المواصفات المعتمدة من الجهاز المركزي للتقييس والسيطرة النوعية /العراق'

const labelData = ref({
  manufacturerName: '',
  countryOfProduction: '',
  productionDate: '',
  modelYear: '',
  maxWeight: '',
  maxWeightPerAxle: '',
  complianceNote: '',
  vinNumber: '',
  vehicleClassification: '',
  engine: '',
  model: '',
  factory: ''
})

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
      const firstRow = jsonData[0]

      // Map Excel columns to label data
      // Adjust these mappings based on your Excel structure
      labelData.value = {
        manufacturerName: firstRow['Manufacturer Name'] || firstRow['manufacturerName'] || '',
        countryOfProduction: firstRow['Country'] || firstRow['countryOfProduction'] || '',
        productionDate: firstRow['Production Date'] || firstRow['productionDate'] || '',
        modelYear: firstRow['Model Year'] || firstRow['modelYear'] || '',
        maxWeight: firstRow['Max Weight'] || firstRow['maxWeight'] || '',
        maxWeightPerAxle: firstRow['Max Weight Per Axle'] || firstRow['maxWeightPerAxle'] || '',
        complianceNote: firstRow['Compliance Note'] || firstRow['complianceNote'] || defaultComplianceNote,
        vinNumber: firstRow['VIN'] || firstRow['vinNumber'] || '',
        vehicleClassification: firstRow['Classification'] || firstRow['vehicleClassification'] || '',
        engine: firstRow['Engine'] || firstRow['engine'] || '',
        model: firstRow['Model'] || firstRow['model'] || '',
        factory: firstRow['Factory'] || firstRow['factory'] || ''
      }
    }
  } catch (error) {
    console.error('Error reading file:', error)
    alert('Error reading file. Please make sure it is a valid Excel or CSV file.')
  }

  // Reset file input
  event.target.value = ''
}

const clearData = () => {
  labelData.value = {
    manufacturerName: '',
    countryOfProduction: '',
    productionDate: '',
    modelYear: '',
    maxWeight: '',
    maxWeightPerAxle: '',
    complianceNote: '',
    vinNumber: '',
    vehicleClassification: '',
    engine: '',
    model: '',
    factory: ''
  }
}

const exportToPDF = async () => {
  const element = document.getElementById('label-content')

  try {
    // Wait for fonts to be loaded
    await document.fonts.ready

    // PDF dimensions: exactly 10cm × 5cm (100mm × 50mm)
    const pdfWidthMm = 100
    const pdfHeightMm = 50

    // Canvas dimensions for print quality (300 DPI)
    // 100mm = 3.937 inches × 300 DPI = 1181 pixels
    // 50mm = 1.969 inches × 300 DPI = 591 pixels
    const scale = 3

    // Capture the element at high resolution
    const canvas = await html2canvas(element, {
      scale: scale,
      useCORS: true,
      allowTaint: true,
      logging: false,
      letterRendering: true,
      foreignObjectRendering: false,
      imageTimeout: 0,
      removeContainer: true,
      backgroundColor: '#ffffff'
    })

    // Create PDF with exact dimensions: 10cm × 5cm
    const pdf = new jsPDF({
      orientation: 'landscape',
      unit: 'mm',
      format: [pdfWidthMm, pdfHeightMm],
      compress: true
    })

    // Add the canvas image to fill the entire PDF page
    const imgData = canvas.toDataURL('image/png', 1.0)
    pdf.addImage(imgData, 'PNG', 0, 0, pdfWidthMm, pdfHeightMm, '', 'FAST')

    // Save the PDF
    pdf.save(`car-label-${labelData.value.vinNumber || 'export'}.pdf`)
  } catch (error) {
    console.error('Error exporting PDF:', error)
    alert('Failed to export PDF. Please try again.')
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
</style>
