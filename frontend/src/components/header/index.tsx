import React from 'react';
import { Link } from 'react-router-dom';
import { Container, ItemList, List } from './styles';

function Header(props: any) {
    return (
        <Container>
            <List>
                <Link to="/"><ItemList> Home</ItemList></Link>
                <Link to="/media"><ItemList>Media</ItemList></Link>
                <Link to="/youtube"><ItemList>Youtube</ItemList></Link>
                <Link to="/web"><ItemList>Web</ItemList></Link>
                <Link to="/status"><ItemList>Status</ItemList></Link>
            </List>
        </Container>
    )
}

export default Header;