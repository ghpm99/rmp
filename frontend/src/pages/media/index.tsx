import React from "react";
import { Container, Title } from "./styles";

function Media() {
    return (
        <Container>
            <Title>Media</Title>
            <div>Arquivos:</div>
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Formato</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Arman Cekin - Run</td>
                        <td>mp3</td>
                    </tr>
                </tbody>
            </table>
            <div>Playlist:</div>
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Formato</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>
            </table>

            <button>Enviar</button>
        </Container>
    )
}

export default Media