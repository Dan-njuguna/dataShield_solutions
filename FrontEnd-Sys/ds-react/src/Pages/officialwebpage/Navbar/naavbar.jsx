import React, { useState, useEffect } from 'react'
import './navbar.css'
import DSlogo from '../../../Assets/DSlogo.png'

export default function Naavbar() {
  const [sticky, setSticky] = useState(false);
  useEffect(()=> {
    window.addEventListener('scroll', ()=> {
      window.scrollY > 500 ? setSticky(true) : setSticky(false)
    })
  }, []);
  return (
    <>
     <nav className={`container ${sticky? 'dark-nav' : '' }`}>
     <img src={DSlogo} alt="" className='logo' />
     <ul>
     <li>Home</li>
         <li>About</li>
         <li>Services</li>
        <li>Demo</li>
        <li>Privacy </li>
         <li><buttton className= 'btn'> Contact us</buttton></li>
     </ul>
     </nav>
    </>

  )
}
