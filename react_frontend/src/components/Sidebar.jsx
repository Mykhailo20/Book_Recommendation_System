import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { RiCloseLine } from 'react-icons/ri';

import { logo } from '../assets';
import { links } from '../assets';


const NavLinks = ({ handleClick }) => (
  <div>
    { links.map((item) => (
      <NavLink 
        key={item.name}
        to={item.to}
        className="flex flex-row justify-start items-center
                   my-8 text-sm font-medium text-gray-400
                   hover:text-cyan-400"
        onClick={() => handleClick && handleClick() }
      >
        <item.icon className='w-6 h-6 mr-2'/>
        {item.name}
      </NavLink>
    )) }
  </div>
)

const Sidebar = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <div className='md:flex hidden flex-col w-[220px] py-10 px-4 
                    bg-[#191624]
    '>
      <div className='flex flex-col justify-center'>
        <img src={logo} alt="logo" className='w-full h-14 object-contain fill-white'/>
        <h3 className='text-center text-white font-bold'>Books System</h3>
      </div>
      <NavLinks />
    </div>
  )
};

export default Sidebar;
