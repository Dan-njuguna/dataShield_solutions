import React from 'react'
import Aboutimg from '../../../Assets/abt_img.jpeg'
//import play_icon from '../../../Assets/play_icon.png'
import './about.css'

export default function AboutWebpage() {
  return (
    <div className='about'>
        <div className="about_left">
    <img src= {Aboutimg} alt =""/>
    {/* <img src = {play_icon} alt = "" className='play_icon'/> */}
        </div>
        <div className="about_right">  
            <h3>
                About us
            </h3>
            <h2>
                DataShield 
            </h2>
            <p>
We are a dedicated organization committed to
 safeguarding data privacy and security.
  Our primary mission is to empower businesses and organizations by providing
   comprehensive compliance monitoring solutions.
</p>
        </div>
    </div>
  )
}
