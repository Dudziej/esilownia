import React from "react";
import {Carousel} from "react-bootstrap";
import {useState} from "react";
import placeholder from "../../imgs/placeholder.png"
import placeholder2 from "../../imgs/placeholder2.png"
import placeholder3 from "../../imgs/placeholder3.png"

function Karuzela() {
    const [index, setIndex] = useState(0);

    const handleSelect = (selectedIndex, e) => {
        setIndex(selectedIndex);
    };

    return (
        <div className="homeCarousel">

            <hr></hr>
            <h1 style={{"fontSize": "4vw"}} className="display-1 pb-4 pt-4">Zacznij z nami trenować !</h1>
            <hr></hr>

            <Carousel activeIndex={index} onSelect={handleSelect}>

                <Carousel.Item>

                    <img
                        className="d-block w-100"
                        src={placeholder2}
                        alt="slide1"
                    />
                    <Carousel.Caption style={{color:'orange', backgroundColor:'black'}}>
                        <h3 className="font-weight-light">Treningi personalne i grupowe</h3>
                        <p className="font-weight-light">Wybierz co Ci bardziej odpowiada.</p>
                    </Carousel.Caption>

                </Carousel.Item>
                <Carousel.Item>

                    <img
                        className="d-block w-100"
                        src={placeholder}
                        alt="slide2"
                    />
                    <Carousel.Caption style={{color:'orange', backgroundColor:'black'}}>
                        <h3 className="font-weight-light">Dashboard</h3>
                        <p className="font-weight-light">Korzystaj z naszego Dashboardu do ustalania terminów
                            ćwiczeń.</p>
                    </Carousel.Caption>

                </Carousel.Item>
                <Carousel.Item>

                    <img
                        className="d-block w-100"
                        src={placeholder3}
                        alt="slide3"
                    />
                    <Carousel.Caption style={{color:'orange', backgroundColor:'black'}}>
                        <h3 className="font-weight-light">Dieta</h3>
                        <p className="font-weight-light">Wybierz odpowiadającą Ci dietę.</p>
                    </Carousel.Caption>

                </Carousel.Item>

            </Carousel>
        </div>
    );
}

export default Karuzela;