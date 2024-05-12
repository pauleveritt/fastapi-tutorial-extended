import React, { useEffect, useState } from "react";

export function Index() {
    const URL = "http://localhost:8080/v1/question/";
    let [questions, setQuestions] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch(URL)
                .then((response) => response.json())
                .then((data) => {
                    setQuestions(data);
                });
        };
        // noinspection JSIgnoredPromiseFromCall
        fetchData();
    }, []);
    return (
        <div className="grid gap-4 grid-cols-4 mx-2 mt-2">
            {questions &&
                questions.map((question) => (
                    <div
                        key={question.id}
                        className="card lg:card-side bg-base-100 shadow-xl"
                    >
                        <div className="card-body">
                            <h2 className="card-title">
                                Question Number {question.id}
                            </h2>
                            <a
                                href={`${URL}/${question.id}`}
                                aria-label="Question"
                            >
                                {question.question_text}
                            </a>
                        </div>
                    </div>
                ))}
        </div>
    );
}
