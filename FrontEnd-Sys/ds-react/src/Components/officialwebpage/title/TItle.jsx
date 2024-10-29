import React from 'react'
import './Title.css'
export default function Title({subTitle, title}) {
  return (
    <div className='title'>
       <h1 className='h1'>{title}</h1>
      <p className='p'>{subTitle} </p>
        
        
     
    </div>
  )
}
