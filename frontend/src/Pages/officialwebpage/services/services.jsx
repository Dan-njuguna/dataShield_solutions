import React from 'react'
import { useRef } from 'react'
import './services.css'
import audits from '../../../img/audits.jpeg'
import Regulation from '../../../img/Regulation.jpeg'
import Risk_mng from '../../../img/Risk_mng.jpeg'
import back_icon from '../../../img/Back_icon (2).png'
import next_icon from '../../../img/Next_icon (2).png'
//import check_cirlce from '../../../img/check_circle.png'
export default function Services() {
    // to select the ul tag we use useRef
    const slider = useRef();
    let tx = 0; //let translate x be = to 0


    //we add the logic fr the back and next icons
    const slideForward = () => {
        if(tx > -50){
            tx -= 25
        }

    slider.current.style.transform = `translateX(${tx}%)`
    }
    const slideBackward = () => {
        if(tx < 0){
            tx += 25
        }

         slider.current.style.transform = `translateX(${tx}%)`
    }


  return (
    <div className='services'>
        <img src = {next_icon} alt = ""className='next-btn' onClick={slideForward}/>
        <img src = {back_icon} alt = "" className='back-btn' onClick={slideBackward}/>
            <div className = "slider">
                <ul ref={slider}>
                    <li>
                        <div className="slide">
                            <div className='info'>
                                <img src={Regulation} alt =""/>
                            </div>
                            <div>
                            <h3>
                                Regulation Tracker
                            </h3>
                            <p>
                            Stay informed about the latest data regulations impacting your business. 
                            Our Regulation Tracker provides a clear overview of compliance status, 
                            allowing you to identify potential risks and take proactive measures.
                            </p>
                        </div>     
                        </div>
                       
                    </li>

                    <li>
                       <div className="slide">
                        <div className='info'>
                            <img src={Risk_mng} alt =""/>
                        </div>
                        <div>
                            <h3>
                            Risk Management:
                            </h3>
                            <p>
                            Reduce the risk of data breaches by implementing strong risk management practices. 
                            Our Risk Management tool helps you identify and mitigate potential risks, 
                            ensuring compliance with data regulations.
                            </p>
                        </div>
                        </div>
                    </li>
                    
                    <li>
                       <div className="slide">
                        <div className='info'>
                            <img src={Risk_mng} alt =""/>
                        </div>
                        <div>
                            <h3>
                            Compliance Reports:
                            </h3>
                            <p>
                            Generate comprehensive compliance reports tailored to your specific needs. 
                            Our reporting feature offers customizable options, 
                            including filters, export formats, and scheduled delivery, ensuring you have the insights you need to make informed decisions.
                            </p>
                        </div>
                        </div>
                    </li>

                    <li>
                        <div className="slide">
                           <div className='info'>
                            <img src={audits} alt =""/>
                           </div>
                           <div>
                            <h3>
                            Task Management:
                            </h3>
                            <p>
                            Streamline your compliance efforts with our task management tool. 
                            Assign, track, and prioritize compliance tasks,
                             ensuring timely completion and maintaining a high level of compliance.
                            </p>
                           </div>
                        </div>
                        
                    </li>
                </ul>

            </div>
        </div>

  )
}
