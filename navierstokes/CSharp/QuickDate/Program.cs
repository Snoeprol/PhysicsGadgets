using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NavierStokes
{
    public class Program
    {
        static void Main(string[] args) 
        {
            var coordinates = new Coordinates(2, 2);
            int[] coordinate = new int[coordinates._D];
            for (int i = 0; i < coordinates._V; i++)
            {
                coordinates.Index2Coord(i, coordinate);
                Console.WriteLine(string.Join("\t", coordinate));
            }
        System.Console.ReadLine();
        }
    }
}
