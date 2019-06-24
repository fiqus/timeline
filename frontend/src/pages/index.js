import React from 'react';
import {Timeline, TimelineEvent} from "react-event-timeline";
import Map from "pigeon-maps";
import Marker from 'pigeon-marker'
import Gallery from 'react-grid-gallery';

class Index extends React.Component {
  state = {
    data: null,
    mapCenter: [55.3781, -3.4360],
    zoom: 6
  };

  componentDidMount() {
    fetch("/api/timeline_entries/")
      .then(response => response.json())
      .then(data => this.setState({data}));
  }

  navigateMap(mapCenter){
    this.setState({mapCenter, zoom:12});
  }

  render() {
    const {data, mapCenter, zoom} = this.state;

    if (!data) {
      return <div>LOADING</div>
    }

    return (
      <div className="main">
        <div className="title-container">
          <h1>Uk Trip 2019</h1>
          <p>Timeline of events recorded when <a href="https://fiqus.coop/">Fiqus</a> and <a href="https://camba.coop/">Camba</a> visited the UK</p>
        </div>
        <div className={"content"}>
          <div className={"map_container"}>
            <Map center={mapCenter} zoom={zoom}>
              {data.map((d, i) =>
                <Marker className={"test"}
                        key={i}
                        anchor={d['lat_lng']}
                        payload={1}
                        onClick={({event, anchor, payload}) => {
                        }}/>)}
            </Map>
          </div>
          <div className={"timeline_container"}>
            <Timeline
              style={{margin: "0 auto 0 0"}}
              lineStyle={{width: 10, backgroundColor: "#f38181", marginLeft:-16}}>
              {data.map((d, i) =>
                <TimelineEvent key={i}
                               title={<h2>{d.title}</h2>}
                               createdAt={<span className={"date"}>{new Date(Date.parse(d.datetime)).toDateString()}</span>}
                               bubbleStyle={{backgroundColor: "#f38181", border: "#f38181",
                                 width: 50, height: 50, marginLeft: -20, borderWidth: 10}}
                               iconStyle={{width: 40, height: 40, margin:"0 auto"}}
                               icon={<img className={"timeline-marker"} src="marker.png" alt=""/>}
                               onIconClick={this.navigateMap.bind(this,d['lat_lng'])}

                >
                  <div className="description">
                    {d.description.split("\n").map((d, i) => <p key={i}>{d}</p>)}
                  </div>
                  <Gallery enableImageSelection={false} images={d.images.map(({img, thumbnail}) => {
                    return {
                      thumbnail: thumbnail.src,
                      thumbnailWidth: thumbnail.width,
                      thumbnailHeight:thumbnail.height,
                      src: img
                    }
                  })}/>
                </TimelineEvent>)}
            </Timeline>
          </div>
        </div>
      </div>
    );
  }
}

Index.propTypes = {};

export default Index;
