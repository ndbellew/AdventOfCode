with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

package NiceString is
   type NiceWord is
      record
         ThreeVowel   : Boolean;
         TwoLetter    : Boolean;
         NoBaddies    : Boolean;
         AppearsTwice : Boolean;
         LetterWrap   : Boolean;
      end record;
   -- Part 1
   procedure IsThreeVowel(NW : in out NiceWord; nString :  in Unbounded_String);
   procedure IsTwoLetter (NW : in out NiceWord; nString :  in Unbounded_String);
   procedure HasBaddies  (NW : in out Niceword; NString :  in Unbounded_String);
   -- Part 2
   procedure RepeatedLetter(NW : in out NiceWord; NString : in Unbounded_String);
   procedure ContainsPairs(NW : in out NiceWord; nString : in Unbounded_String);
end NiceString;
