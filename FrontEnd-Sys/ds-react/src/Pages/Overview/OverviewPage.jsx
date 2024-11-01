import React from 'react';
import Card from './components/Card';
import Tabs from './components/Tabs';
import './index.css';
// import DSlogo from '../../../Assets/DSlogo.png';
const OverviewPage = () => {
  return (
  <>
  {/* <img src = {DSlogo} alt = "" className = "logo1"/> */}
    <div  className='overview'>
      <Card/>
      <Tabs/>
    </div>
    </>
  )
}
export default OverviewPage;
