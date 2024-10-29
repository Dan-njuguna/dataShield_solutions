import React from 'react';
import Card from '../card/Card';
import Tabs from '../tabs/Tabs';
import './index.css';
// import DSlogo from '../../../Assets/DSlogo.png';
const OverviewPage = () => {
  return (
  <>
  {/* <img src = {DSlogo} alt = "" className = "logo1"/> */}
    <div >
      <Card/>
      <Tabs/>
    </div>
    </>
  )
}
export default OverviewPage;
