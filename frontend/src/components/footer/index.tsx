import React from 'react';
import { Container, List, ItemList } from './styles';


function Footer() {
    return (
        <Container>
            <List>
                <ItemList>Home</ItemList>
                <ItemList>Media</ItemList>
                <ItemList>Youtube</ItemList>
                <ItemList>Web</ItemList>
                <ItemList>Privacy Policy</ItemList>
            </List>
        </Container>
    )
}

export default Footer;