import { GoHome, GoSearch } from "react-icons/go";
import { MdLocalLibrary, MdRecommend } from "react-icons/md";
import { SiBookstack } from "react-icons/si";


export const links = [
  { name: 'Home', to: '/', icon: GoHome },
  { name: 'Search', to: '/search', icon: GoSearch },
  { name: 'Your Library', to: '/rated-books', icon: MdLocalLibrary },
  { name: 'Recommendations', to: '/book-recommendations', icon: SiBookstack},
];


export default links;