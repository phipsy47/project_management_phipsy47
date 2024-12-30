import React from 'react'
import ReactDOM from 'react-dom/client'
import TopElement from './TopElement'
import TextBox from './TextBox'
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <TopElement />
    <TextBox />
  </React.StrictMode>,
)

