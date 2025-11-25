/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e6fffe',
          100: '#b3fff9',
          200: '#80fff5',
          300: '#4dffe0',
          400: '#1adfcc',
          500: '#01b3a3',
          600: '#018f82',
          700: '#016b61',
          800: '#004740',
          900: '#00231f',
          DEFAULT: '#01b3a3',
        },
      },
    },
  },
  plugins: [],
}