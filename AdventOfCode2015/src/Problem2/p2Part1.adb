with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Containers.Vectors;
with Ada.Containers; use Ada.Containers;



procedure Main is

   package Integer_Vectors is new Ada.Containers.Vectors(Positive, Integer);
      subtype Vector is Integer_Vectors.Vector;
   use all type Vector;
   LWH          : Vector;
   InputFile    : File_Type;
   FileName     : String := "C:\GNAT\2021\bin\textfiles\problem2.txt";
   A            : Unbounded_String;
   Total        : Integer := 0;
   Position     : Integer := 0;

   function SplitIntoSizes(Str : in Unbounded_String)
     return Vector
   is
     -- V         : Vector;
      --I         : Natural;
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

   function SurfaceAreaFromVector(V : in Vector) return Integer
   is
      Length     : Integer;
      Width      : Integer;
      Height     : Integer;
      function GetSmallestSide(Length: in Integer;
                               Width : in Integer;
                               Height : in Integer) return Integer
      is
         LW  : Integer := Length * Width;
         WH  : Integer := Width  * Height;
         HL  : Integer := Height * Length;
      begin
         if LW <= WH and LW <= HL then
            return LW;
         elsif WH <= HL then
            return WH;
         else
            return HL;
         end if;
      end GetSmallestSide;

   begin
      Length := V (1);
      Width  := V (2);
      Height := V (3);
      return 2*Length*Width + 2*Width*Height + 2*Height*Length + GetSmallestSide(Length, Width, Height);
   end SurfaceAreaFromVector;



begin
   Open (InputFile, In_File, Filename);
   while not End_Of_File (InputFile) loop
      A     := To_Unbounded_String (Get_Line(InputFile));
      LWH   := SplitIntoSizes(A);
      Total := Total + SurfaceAreaFromVector(LWH);
   end loop;
   Close (InputFile);
   -- Put_Line(Ada.Strings.Unbounded.To_String(A));
   Put_Line("Total square feet of wrapping paper " & Total'Image);
   -- Put_Line("Position "      & Position'Image);
      -- return Value;
end Main;
