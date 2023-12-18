with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;



procedure Part2 is

   InputFile    : File_Type;
   FileName     : constant String := "C:\GNAT\2021\bin\textfiles\problem1.txt";
   A            : Unbounded_String;
   CorrectFloor : Integer := 0;
   Position     : Integer := 0;

begin

   Open (InputFile, In_File, Filename);
   while not End_Of_File (InputFile) loop
      A := To_Unbounded_String (Get_Line(InputFile));
      Put_Line ("Eyo");
   end loop;
   Close (InputFile);
   for Paren in 1 .. Length (A) loop
      if Element(A, Paren) = '(' then
         CorrectFloor := CorrectFloor + 1;
      else
         CorrectFloor := CorrectFloor - 1;
         if CorrectFloor < 0
           and Position = 0 then
            Position := Paren;
         end if;
      end if;
   end loop;
   -- Put_Line(Ada.Strings.Unbounded.To_String(A));
   Put_Line("Correct Floor " & CorrectFloor'Image);
   Put_Line("Position "      & Position'Image);

      -- return Value;
   --  Insert code here.
  Put_Line ("null;");
end Part2;
