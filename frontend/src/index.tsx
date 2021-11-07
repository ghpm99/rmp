import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './pages/index';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import Media from './pages/media';
import Youtube from './pages/youtube';
import Web from './pages/web';
import Status from './pages/status';

ReactDOM.render(
  <BrowserRouter>
    <Header />
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/media" element={<Media />} />
      <Route path="/youtube" element={<Youtube />} />
      <Route path="/web" element={<Web />} />
      <Route path="/status" element={<Status />} />
    </Routes>
    <Footer />
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
