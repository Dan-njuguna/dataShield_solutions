import React from 'react'
import { Link } from 'react-router-dom';
import Dashboard from './Dashboard';
import OverviewPage from '../Overview/body/OverviewPage';
// import DSLogo from '../../Assets/DSlogo.png'

 function Sidenavbar() {


  // Define a function to open the column when clicked
  return (
    <>
    {/* <div className='container'> */}
        <div className='Sidenavbar'>
          {/* <img src = {DSLogo} alt = ""/>
          < */}
            <ul>
              <Link to = '/' element = {<Dashboard/>}>help</Link>
              <Link to = '/' element = {<OverviewPage/>}>Overview</Link>
            </ul>
        {/* </div> */}
        {/* <div className='side-column'>

        </div> */}

    </div>

    </>
    
  )
}
export default Sidenavbar;
