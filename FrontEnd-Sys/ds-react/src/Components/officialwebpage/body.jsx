import React from 'react'
import  './webindex.css'
import Hero from './hero/Hero'
import Naavbar from './Navbar/naavbar'
import Services from './services/services'
import Title from './title/TItle'
import AboutWebpage from './About/AboutWebpage'
import Contact from './contacts/Contact'
export default function Webpage() {
  return (
    <>
    <div className='body'>
    <Naavbar/>
    <Hero/>
    <div className="rest-body">
    <AboutWebpage/>
    <Title subTitle="What we offer" title = "Our services"/>
    <div className="container ">
    <Services/>
    </div>

<Title title="FAQs" subTitle = "Customer reviews "/>

<Title  title = " Contact us" subTitle="Get in touch"/>
<Contact/>
    </div>
    
    </div>

    </>
  )
}
