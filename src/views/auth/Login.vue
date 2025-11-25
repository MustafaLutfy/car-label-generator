<template>
  <div>
      <!-- Background Gradient -->

    <!-- Main Container with Map Background -->
    <div class="relative z-10 flex min-h-screen items-center justify-center bg-[url(/assets/auth/map.png)] bg-cover bg-center bg-no-repeat px-6 py-10">
      <!-- Decorative Objects -->
      <img src="/assets/auth/coming-soon-object1.png" alt="decoration" class="absolute left-0 top-1/2 h-full max-h-[893px] -translate-y-1/2" />
      <img src="/assets/auth/coming-soon-object3.png" alt="decoration" class="absolute right-0 top-0 h-[300px]" />

      <!-- Login Container -->
      <div class="relative flex shadow-[0_0_20px_0_rgba(0,0,0,0.3)] w-full max-w-[1502px] flex-col justify-between overflow-hidden rounded-2xl bg-white/60 backdrop-blur-lg lg:min-h-[758px] lg:flex-row lg:gap-10 xl:gap-0">

        <!-- Left Side - Gradient with Skew -->
        <div class="relative hidden w-full items-center justify-center bg-gradient-to-br from-primary-400 via-primary-500 to-primary-600 p-5 lg:inline-flex lg:max-w-[835px] xl:-ml-28 xl:skew-x-[14deg]">
          <div class="absolute inset-y-0 w-8 bg-gradient-to-r from-primary/10 via-transparent to-transparent -right-10 xl:w-16 xl:-right-20"></div>

          <div class="xl:-skew-x-[14deg]">
            <div class="w-48 lg:w-72 ml-10">
              <div class="flex items-center gap-3 text-white">
                <span class="text-3xl font-bold">Car Label Generator</span>
              </div>
            </div>

            <div class="mt-24 hidden w-full max-w-[430px] lg:block border-b-2 border-primary-700">
              <img src="/assets/car.svg" alt="Login Illustration" class="w-full" />
            </div>
          </div>
        </div>

        <!-- Right Side - Login Form -->
        <div class="relative flex w-full flex-col items-center justify-center gap-6 px-4 pb-16 pt-6 sm:px-6 lg:max-w-[667px]">
          <!-- Logo and Language Selector -->
          <div class="flex w-full max-w-[440px] items-center gap-2 lg:absolute lg:right-6 lg:top-6 lg:max-w-full">
            <div class="w-8 block lg:hidden">
              <svg class="w-10 h-10 text-primary" viewBox="0 0 40 40" fill="currentColor">
                <path d="M20 5L15 15L20 25L25 15L20 5Z" />
                <circle cx="20" cy="30" r="3" />
              </svg>
            </div>

           
          </div>

          <!-- Form Content -->
          <div class="w-full max-w-[440px] lg:mt-16">
            <div class="mb-10">
              <h1 class="text-3xl font-extrabold uppercase !leading-snug text-primary md:text-4xl">Sign in</h1>
              <p class="text-base font-bold leading-normal text-gray-600">Enter your email and password to login</p>
            </div>

            <form @submit.prevent="handleLogin" class="space-y-5">
              <!-- Email -->
              <div>
                <label for="email" class="block mb-2 font-semibold text-gray-700">Username</label>
                <div class="relative text-gray-400">
                  <input
                    id="email"
                    v-model="formData.email"
                    type="text"
                    placeholder="Enter Email"
                    class="w-full pl-10 pr-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                    required
                    :disabled="loading"
                  />
                  <span class="absolute left-4 top-1/2 -translate-y-1/2">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </span>
                </div>
                <div v-if="errors.email" class="mt-1 text-sm text-red-600">{{ errors.email[0] }}</div>
              </div>

              <!-- Password -->
              <div>
                <label for="password" class="block mb-2 font-semibold text-gray-700">Password</label>
                <div class="relative text-gray-400">
                  <input
                    id="password"
                    v-model="formData.password"
                    :type="showPassword ? 'text' : 'password'"
                    placeholder="Enter Password"
                    class="w-full pl-10 pr-12 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
                    required
                    :disabled="loading"
                  />
                  <span class="absolute left-4 top-1/2 -translate-y-1/2">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                    </svg>
                  </span>
                  <button
                    type="button"
                    @click="showPassword = !showPassword"
                    class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 focus:outline-none"
                    :disabled="loading"
                  >
                    <svg v-if="!showPassword" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                    <svg v-else class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                    </svg>
                  </button>
                </div>
                <div v-if="errors.password" class="mt-1 text-sm text-red-600">{{ errors.password[0] }}</div>
              </div>

              <!-- Newsletter Checkbox -->
              <div>
                <label class="flex cursor-pointer items-center gap-3">
                  <input
                    v-model="subscribeNewsletter"
                    type="checkbox"
                    class="custom-checkbox w-5 h-5 bg-white border-2 border-gray-300 rounded focus:ring-2 focus:ring-primary cursor-pointer appearance-none"
                  />
                  <span class="text-gray-600 font-medium">Remember me</span>
                </label>
              </div>

              <!-- Error Message -->
              <div v-if="errorMessage" class="p-3 bg-red-50 border border-red-200 text-red-600 rounded-lg text-sm">
                {{ errorMessage }}
              </div>

              <!-- Submit Button -->
              <button
                type="submit"
                class="!mt-6 w-full py-3 px-4 bg-primary text-white font-semibold rounded-lg uppercase shadow-[0_10px_20px_-10px_rgba(67,97,238,0.44)] hover:from-pink-600 hover:to-blue-700 transition-all"
                :disabled="loading"
              >
                {{ loading ? 'Signing in...' : 'Sign in' }}
              </button>
            </form>

      
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
// import { useAuthStore } from '@/stores/auth'
// import { useNotification } from '@/composables/useNotification'

const router = useRouter()
// const authStore = useAuthStore()
// const notification = useNotification()

const formData = ref({
  email: '',
  password: ''
})

const loading = ref(false)
const errors = ref({})
const errorMessage = ref('')
const showPassword = ref(false)
const subscribeNewsletter = ref(false)

const handleLogin = async () => {
  loading.value = true
  errors.value = {}
  errorMessage.value = ''

  try {
    // Static login for testing
    if (formData.value.email === 'admin' && formData.value.password === '123@123') {
      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 500))

      // Store auth state in localStorage for persistence
      localStorage.setItem('isAuthenticated', 'true')
      localStorage.setItem('user', JSON.stringify({
        email: 'admin',
        name: 'Admin User'
      }))

      router.push('/label-generator')
    } else {
      throw new Error('Invalid credentials')
    }
  } catch (error) {
    console.error('Login error:', error)

    if (error.errors) {
      errors.value = error.errors
    }

    errorMessage.value = error.message || 'Login failed. Please check your credentials.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@keyframes blob {
  0% {
    transform: translate(0px, 0px) scale(1);
  }
  33% {
    transform: translate(30px, -50px) scale(1.1);
  }
  66% {
    transform: translate(-20px, 20px) scale(0.9);
  }
  100% {
    transform: translate(0px, 0px) scale(1);
  }
}

.animate-blob {
  animation: blob 7s infinite;
}

.animation-delay-2000 {
  animation-delay: 2s;
}

.animation-delay-4000 {
  animation-delay: 4s;
}

/* Custom checkbox styling */
.custom-checkbox:checked {
  background-color: #01b3a3;
  border-color: #01b3a3;
  background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
  background-size: 120% 120%;
  background-position: center;
  background-repeat: no-repeat;
}
</style>
