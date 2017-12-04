/**
 * A.java
 * Author: RedEyes
 * Borrowed from Stack Overflow: https://stackoverflow.com/questions/30968231/whats-wrong-with-my-code
 */

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

class A implements ActionListener {

    JFrame f;
    JButton b;
    JPanel p;
    JLabel l;
    JTextField t;

    A(String s) {
        JFrame f=new JFrame(s);
        f.setVisible(true);
        f.setSize(400,400);
        JButton b= new JButton("OK");
        JTextField t=new JTextField();
        JPanel p=new JPanel(); 
        f.add(p);
        p.setBounds(0,0,300,300);
        p.add(b);
        b.setBounds(30,40,80,80);
        p.add(t);
        t.setBounds(100,200,80,80);
        b.addActionListener(this);
        t.addActionListener(this);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == b) {    
            t.setText("Hey There");
        }
        System.out.println("I m done!!");
    }

    public static void main(String[] args) {
         System.out.println("Hey there");  
         new A("First App");  
    }
}