using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NavierStokes
{
    public class FluidElement
    {
        public FluidElement(int index,double[] speed,double[] vorticity)
        {
            int _index = index;
            /* Speed and vorticity of form int[cooordinates._D]*/
            var _speed = speed;
            var _vorticity = vorticity;

        }
    }
}
