with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Containers.Vectors;
with Ada.Containers; use Ada.Containers;



procedure Main is

   package Integer_Vectors is new Ada.Containers.Vectors(Positive, Integer);
   package Integer_Vectors_Sorting is
     new Integer_Vectors.Generic_Sorting;
   subtype Vector is Integer_Vectors.Vector;
   use all type Vector;
   use Integer_Vectors_Sorting;

   Movement     : Unbounded_String;
   InputFile    : File_Type;
   FileName     : String := "C:\GNAT\2021\bin\textfiles\problem3.txt";
   A            : Unbounded_String;
   Total        : Integer := 0;
   Position     : Integer := 0;

   procedure PrintVector(V : Vector)
   is
   begin
      for Elem of V loop
        Put_Line("" & Integer'Image(Elem));
      end loop;
   end PrintVector;


   function SplitIntoSizes(Str : in Unbounded_String)
     return Vector
   is
      Sizes     : Vector;
      Delimiter : Character := 'x';
      TempStr   : Unbounded_String;
   begin
      for I in 1 .. Length (Str) loop
         if Element(Str, I) /= Delimiter then
            TempStr := TempStr & Element(Str, I);
         else
            Sizes.Append (Integer'Value (To_String(TempStr)));
            TempStr := Null_Unbounded_String;
         end if;
      end loop;
      Sizes.Append(Integer'Value(To_String(TempStr)));
      return Sizes;
   end SplitIntoSizes;

   function GetLengthOfRibbon(V : in out Vector) return Integer
   is

      Length  : Integer := V (1);
      Width   : Integer := V (2);
      Height  : Integer := V (3);
      SmallSide1, SmallSide2 : Integer;
      --SortedV : Vector  := Sort(V);
   begin
      Sort(V);
      SmallSide1 := V(1);
      SmallSide2 := V(2);
    --PrintVector(V);
      return 2*SmallSide1 + 2*SmallSide2 + Length*Width*Height;
   end GetLengthOfRibbon;

begin
   Open (InputFile, In_File, Filename);
   while not End_Of_File (InputFile) loop
      A     := To_Unbounded_String (Get_Line(InputFile));
      Put_Line(To_String(A));
   end loop;
   Close (InputFile);
   Put_Line("Total Feet of Ribbon Needed: " & Total'Image);
end Main;
