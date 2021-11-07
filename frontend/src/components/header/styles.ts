import styled from "styled-components";

export const Container = styled.header`
background-color: #222831;
align-self: auto;
color:#EEEEEE;
`;

export const List = styled.ul`
  padding: 0;
  list-style: none;
  text-align: center;
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 0;
  margin-top: 0;
  display: flex;
  justify-content: space-between;
  a {
    color:#EEEEEE;
    text-decoration: none;
  }
`;

export const ItemList = styled.li`
  padding: 10px;
  cursor: pointer;
  &:hover{
    background-color: #393E46;
  }
`;
