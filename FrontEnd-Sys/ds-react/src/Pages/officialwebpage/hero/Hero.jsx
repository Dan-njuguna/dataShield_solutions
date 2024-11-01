import React from 'react'
import './hero.css'
import dark_arrow from '../../../Assets/dark_arrow.png'

export default function Hero() {
  return (
    <div className='Hero webcontainer'>
        <div className="hero-text">
            <h1>We ensure compliance with data rules</h1>
            <p>
                Welcome to DataShield, 
                a revolutionary platform designed to protect and analyze your sensitive data.
            </p>
            <button className='btn2'>Explore more<img src ={dark_arrow} alt= ""/></button>

        </div>
        
    </div>
  )
}
