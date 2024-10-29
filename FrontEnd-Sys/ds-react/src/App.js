import React from 'react';
import OverviewPage from './Components/Overview/body/OverviewPage';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Dashboard from './Components/DashboardPage/Dashboard';
 import Webpage from './Components/officialwebpage/body';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<OverviewPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/webpage" element = {<Webpage/>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
