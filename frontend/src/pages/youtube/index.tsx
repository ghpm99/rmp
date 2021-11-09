import React from "react";
import { Container, Title } from "./styles";

function Youtube() {
    return (
        <Container>
            <Title>Youtube</Title>
            <form>
                <label>Link:</label>
                <input type="text" />
                <input type="submit" />
            </form>
            <div>Playlist:</div>
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>link</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            TWICE "What is Love?" M/V
                        </td>
                        <td>
                            https://www.youtube.com/watch?v=i0p1bmr0EmE&list=RDMMjIpiLvkDIK8&index=14
                        </td>
                    </tr>
                </tbody>
            </table>
        </Container>
    )
}

export default Youtube