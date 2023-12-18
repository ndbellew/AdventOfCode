with Ada.Text_IO; use Ada.Text_IO;
with Ada.Containers; use Ada.Containers;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Containers.Vectors;
with Ada.Containers.Ordered_Sets;
with Ada.Exceptions; use Ada.Exceptions;
with Tuples;



procedure Main is

   package Coord_Tuple is new Tuples;
   subtype Tuple is Coord_Tuple.Tuple;


   package Coord_Vectors is new Ada.Containers.Vectors(Index_Type => Positive, Element_Type => Unbounded_String );
   subtype Vector is Coord_Vectors.Vector;
   use all type Vector;

   package Coord_Set is new
     Ada.Containers.Ordered_Sets
       (Element_Type => Unbounded_String);
   subtype Set is Coord_Set.Set;
   use all type Set;

   Houses       : Vector;
   VerifyHouses : Set;
   InputFile    : File_Type;
   FileName     : String := "C:\GNAT\2021\bin\textfiles\problem3.txt";
   A            : Unbounded_String;
   CurrNS       : Integer := 0;
   CurrEW       : Integer := 0;
   Location     : Tuple;
   D            : Character;

   procedure PrintVector(V : Vector)
   is
   begin
      for Elem of V loop
        Put_Line(To_String(Elem)); --Should be string Vector
      end loop;
   end PrintVector;

   procedure PrintSet(S : Set)
   is
   begin
      for Elem of S loop
         Put_Line(To_String(Elem));
      end loop;
   end PrintSet;

   function Move(CurrNorth : in out Integer; CurrEast : in out Integer; Direction : in Character ) return Tuple

   is
     T : Tuple;
   begin
      if Direction = '^' then
         CurrNorth := CurrNorth + 1;
      elsif Direction = 'v' then
         CurrNorth := CurrNorth - 1;
      elsif Direction = '>' then
         CurrEast := CurrEast + 1;
      elsif Direction = '<' then
         CurrEast := CurrEast - 1;
      else
         Put_Line("Something broke!");
      end if;

      T.Elem1 := CurrNorth;
      T.Elem2 := CurrEast;

      return T;
   end Move;


begin
   Open (InputFile, In_File, Filename);
   while not End_Of_File (InputFile) loop
      A     := To_Unbounded_String (Get_Line(InputFile));
   end loop;
   Location.Elem1 := CurrNS;
   Location.Elem2 := CurrEW;
   Houses.Append( To_Unbounded_String(Coord_Tuple.GetElemsString(Location)));
   VerifyHouses.Insert(To_Unbounded_String(Coord_Tuple.GetElemsString(Location)));
   for Direc in To_String(A)'Range loop
      D := Element(A, Direc);
      Location := Move(CurrNorth => CurrNS, CurrEast => CurrEW, Direction => D);
      Houses.Append(To_Unbounded_String(Coord_Tuple.GetElemsString(Location)));
      begin
      VerifyHouses.Insert(To_Unbounded_String(Coord_Tuple.GetElemsString(Location)));
      exception
         when Constraint_Error =>
            Put_Line("Location " & Coord_Tuple.GetElemsString(Location) &" Already in Set");
      end;
      CurrNS := Location.Elem1;
      CurrEW := Location.Elem2;
   end loop;

   Close (InputFile);
   Put_Line("Total Number of houses is " & Count_Type'Image(VerifyHouses.Length));
end Main;

