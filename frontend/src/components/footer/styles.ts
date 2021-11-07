import styled from "styled-components";

export const Container = styled.footer`
background-color: #222831;
align-self: auto;
color:#EEEEEE;
padding: 15px;
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
`;

export const ItemList = styled.li`
  padding: 20px;
  cursor: pointer;
  &:hover{
    background-color: #393E46;
  }
`;
