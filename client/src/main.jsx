import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { QueryClient, QueryClientProvider, useQuery } from "@tanstack/react-query";
import { GoogleOAuthProvider } from '@react-oauth/google';
const VITE_GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;
console.log(VITE_GOOGLE_CLIENT_ID)
const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
        <QueryClientProvider client={queryClient}>
        <GoogleOAuthProvider clientId={VITE_GOOGLE_CLIENT_ID}>
    <App />
    </GoogleOAuthProvider>
    </QueryClientProvider>

  </React.StrictMode>,
)
