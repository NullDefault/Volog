import React, {Component} from 'react'
import MentorList from './mentorList'
import ProfileOpen from './profileOpen'
import {getStudentList} from "../../../../functions/services/api/faculty_requests/get_student_list";
import {getMentorList} from "../../../../functions/services/api/faculty_requests/get_mentor_list";

export default class Mentor extends Component {
    state = {
        students: null,
        selectedStudentData: null,
        page: 1,
        countData: 0,
        studentNo: 0,
        searchQuery: ''
    };

    componentDidMount() {
        this.getStudentData();
    }


    getStudentData = () => {
        const {page, searchQuery} = this.state;
        getMentorList(this, searchQuery, page);
    };


    pagination = (pageno) => {
        console.log(pageno)
        this.setState({page: pageno}, () => {
            this.getStudentData();
        });

    };

    selectedStudent = (index) => {
        const student = this.state.students[index];
        this.setState({selectedStudentData: student, studentNo: index})
    };

    searchStudent = (event) => {
        let studentQuery = event.target.value.toLowerCase();
        this.setState({searchQuery: studentQuery, page: 1}, () => {
            this.getStudentData()
        });

    };

    render() {
        const {students, selectedStudentData, page, countData, studentNo} = this.state;
        // console.log(students);
        return (
            <>
                {
                    students &&
                    <>
                        <div className="bg-green-100 w-1/2 p-3" id="leftSide" style={{height: '90vh'}}>
                            <MentorList
                                pagination={this.pagination}
                                studentData={students}
                                selectedStudent={this.selectedStudent}
                                page={page}
                                searchStudent={this.searchStudent}
                                countData={countData}
                                studentNo={studentNo}
                            />
                        </div>
                        <div className="bg-green-200  w-full" id="rightSide" style={{height: '90vh'}}>
                            <ProfileOpen data={selectedStudentData}/>
                        </div>
                    </>
                }

            </>
        )
    }
}
