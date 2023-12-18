with Ada.Text_IO; use Ada.Text_IO;

generic package Tuples is
   type Tuple is
      record
         Elem1 : Integer;
         Elem2 : Integer;
      end record;
   function GetElemsString(T : Tuple) return String;
end Tuples;
