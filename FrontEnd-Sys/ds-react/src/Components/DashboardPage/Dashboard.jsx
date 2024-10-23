import React, { useState } from 'react'
import Sidenavbar from './Sidenavbar';
import Topnavbar from './Topnavbar';
import './index.css';
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
    <Topnavbar onLinkClick = {handleTopnavbarContent}/>
    <div className='dash-container'>
        <div className='cont-col-1'><Sidenavbar/></div>
        <div className="cont-col-2">
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