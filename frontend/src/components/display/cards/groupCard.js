import React, {Component} from 'react';
import {Button, Card, Container} from 'react-bootstrap';
import "../../../static/css/pages/mentorPg.css";

class GroupCard extends Component {
    constructor(props) {
        super(props)
        this.state = {
            Mentor: 'Deja',
            StuNames: ['Perrfection', 'Mahmoud', 'David']
        }
    }


    render() {
        return <Container>
            <Card className="groupCard" style={{width: '18rem'}}>
                <Card.Body>
                    <Card.Title>Mentor: Deja </Card.Title>
                    <Card.Subtitle>Students: </Card.Subtitle>
                    <Card.Text className="groupCard">
                        Perrfection
                        Mahmoud
                        David
                    </Card.Text>
                    <Button>View all students </Button>
                </Card.Body>
            </Card>
        </Container>
    }
}

export default GroupCard;