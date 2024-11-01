import React from 'react';
import { Link } from 'react-router-dom';
import Dashboard from '../Pages/DashboardPage/Dashboard';
import '../index.css'
// import styled from 'styled-components';
 function Tabs (){

    return (
        <>
         <div className='Tabs'>
            <ul>
            <Link to = '/dashboard' element = {<Dashboard/>} ><div className = 'tabs-container' >Dashboard</div></Link>
            <Link to = '/dashboard' element = {<Dashboard/>} ><div className = 'tabs-container' >Current Metrics</div></Link>
            <Link to = '/dashboard' element = {<Dashboard/>} ><div className = 'tabs-container' >Quick access</div></Link>
            </ul>
         </div>
        </>

       
    

    );
 }
 export default Tabs;
