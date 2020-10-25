import React from "react";
import VProgressBar from '../components/elements/ProgressBar'
import Container from 'react-bootstrap/Container';
import UserPic from "../components/elements/Cards/userPic";
import "../static/css/pages/studentPg.css"
import HoursTable from "../components/display/HoursTable";
import {Button, ButtonGroup, Col, Row} from "react-bootstrap";
import Paper from "@material-ui/core/Paper";

class StudentDashboard extends React.Component {

    render() {

        return <Container className="student-page">
            <Row area-label="top spacer">

            </Row>
            <Paper className="student-progress-profile">
                <Row>
                    <Col>
                        <UserPic>

                        </UserPic>
                    </Col>
                    <Col>
                        Welcome Back, User!
                    </Col>
                </Row>
                <Container className="progress-bar" >
                    <VProgressBar>

                    </VProgressBar>
                </Container>
                <Row>
                    <ButtonGroup class-name="student-buttons">
                        <Button variant="secondary">Report Hours</Button>
                        <Button variant="secondary">View Pending</Button>
                        <Button variant="secondary">Notifications</Button>
                    </ButtonGroup>
                </Row>
            </Paper>
            <Row>
                <HoursTable>

                </HoursTable>
            </Row>
        </Container>
    }

}


export default StudentDashboard;