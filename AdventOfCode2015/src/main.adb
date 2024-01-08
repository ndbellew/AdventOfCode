with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Fixed;
with Ada.Containers; use Ada.Containers;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Exceptions; use Ada.Exceptions;
with Ada.Numerics.Generic_Elementary_Functions; use Ada.Numerics.Generic_Elementary_Functions;


procedure Main is

   type TwoDimension_Array is array  (Integer range 0 .. 1000, Integer range 0 .. 1000) of Boolean;
   type Single_Array is array (Integer range 0 .. 100000) of Boolean;

   InputFile             : File_Type;
   FileName              : String  := "C:\Users\shepe\AdventOfCode\AdventOfCode2015\textfiles\problem5.txt";
   A                     : Unbounded_String;
   Map       : TwoDimension_Array := (others=>(others=> False));
   procedure getPoints (x1 : in Integer; y1 : in Integer; x2 : in Integer; y2 : in Integer; NumberMap : TwoDimension_Array) is
      AllPoints : Single_Array;
      deltaX    : Integer := abs (x2 - x1);
      deltaY    : Integer := abs (y2 - y1);
   begin
      for Y in y1 .. y2 loop
         for X in x1 .. x2 loop
            if NumberMap(X,Y) then
               NumberMap(X,Y) := True;
            else
               NumberMap(X,Y) := False;
            end if;
         end loop;

      end loop;

   end getPoints;

begin
   Open (InputFile, In_File, Filename);
   while not End_Of_File (InputFile) loop
      A   :=   To_Unbounded_String (Get_Line(InputFile));
   end loop;
   Put_Line("+");
end Main;
