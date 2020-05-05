using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NavierStokes;

namespace NavierStokes
{
    class Navier
    {
        public Navier()
        {
            int h = 1;
            int T = 8;
            int IL = 10;
            double V0 = 10;
            double omega = 0.1;
            double nu = 1;
            int iter = 0;
            double R = V0 * h / nu;

            Coordinates coordinates = new Coordinates(100, 2);
            for (int index = 0; index < coordinates._V; index ++)
            {
                /* Set initials */
                int[] coordinate = new int[coordinates._D];
                coordinates.Index2Coord(index, coordinate);
                if (coordinate[1] == coordinates._N)
                {
                    new FluidElement(index, new double[] { 0, coordinate[1] * V0 }, new double[] { 0, 0 });
                }
                else if (coordinate[1] == coordinates._N)
                {
                    new FluidElement(index, new double[] { 0 , 0 }, new double[] { 0, 0 });
                }
                else if (coordinate[1] == coordinates._N - 1)
                {
                    new FluidElement(index, new double[] { 0, 0 }, new double[] { 0, 0 });
                }
                else
                {
                    new FluidElement(index, new double[] { coordinate[1] * V0, 0 }, new double[] { 0, 0 });
                }
            }
        }

    }
}
