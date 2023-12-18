with Ada.Text_IO; use Ada.Text_IO;

package body Tuples is

   function GetElemsString(T : in Tuple) return String
   is
      Answer : String(1 .. 100);
   begin
      -- Print_Line("(" & T.Elem1'Image & ", " & T.Elem2'Image & ")");
      return "(" & T.Elem1'Image & ", " & T.Elem2'Image & ")";
   end GetElemsString;

end Tuples;
