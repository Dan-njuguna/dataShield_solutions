import React, { useState } from 'react'
import Sidenavbar from '../../components/Sidenavbar';
import Topnavbar from '../../components/Topnavbar';
import './dashindex.css'
import DSlogo from '../../img/DSlogo.png'
// import styled from "styled-components"
function Dashboard() {
// create a function that maanges the state of  each individual component of the tiopnavbar and then 
//pass that funtion to the topnavbar
const [selectedContent, setSelectedContent] = useState('')
//CALLBACK handleclick funtion to handel the topnavbar
const handleTopnavbarContent = (pageContent) => {
  setSelectedContent(pageContent);
};
//a funtion for closing the side column 
  const closeSideColumn = () => {
    setSelectedContent('');
  };
  // render the dashboard component here and import Sidenavbar and Topnavbar components
  return (
    <>
    <Topnavbar className = "Topnavbar" onLinkClick = {handleTopnavbarContent}/>
    <div className='dash-container'>
        <div className='cont-col-1'><Sidenavbar/></div>
        <div className="cont-col-2">
        <img src = {DSlogo} alt = ""  className='logo' />
          <p> Welcome to data shield</p>
          {/* Render the selected content here */}
          {selectedContent ? (
            <div>
              <h2>{selectedContent.title}</h2>
              <p>{selectedContent.content}</p>
              <button className='close-btn' onClick={closeSideColumn}>close</button>
            </div>
          ) : (
            <p></p>
          )}
        </div>
      </div>

    </>
  )
}

export default  Dashboard;