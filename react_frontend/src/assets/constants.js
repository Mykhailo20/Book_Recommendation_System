import { GoHome, GoSearch } from "react-icons/go";
import { MdLocalLibrary, MdRecommend } from "react-icons/md";
import { SiBookstack } from "react-icons/si";

export const defaultAuthors = [
  { displayValue: 'Joanne Rowling', backendValue: 'J. K. Rowling' },
  { displayValue: 'Antoine de Saint-Exupéry', backendValue: 'Antoine de Saint-ExupÃ©ry' },
  { displayValue: 'Orson Card', backendValue: 'Orson Scott Card' },
  { displayValue: 'Stephen Chbosky', backendValue: 'Stephen Chbosky' },
  { displayValue: 'John Tolkien', backendValue: 'J.R.R. TOLKIEN' },
  { displayValue: 'Lois Lowry', backendValue: 'LOIS LOWRY' },
  { displayValue: 'Daniel Quinn', backendValue: 'Daniel Quinn' },
  { displayValue: 'Jhumpa Lahiri', backendValue: 'Jhumpa Lahiri' },
  { displayValue: 'Anne Frank', backendValue: 'ANNE FRANK' },
  { displayValue: 'Elwyn White', backendValue: 'E. B. White' }
];

export const links = [
  { name: 'Home', to: '/', icon: GoHome },
  { name: 'Search', to: '/search', icon: GoSearch },
  { name: 'Your Library', to: '/rated-books', icon: MdLocalLibrary },
  { name: 'Recommendations', to: '/book-recommendations', icon: SiBookstack},
];

export default links;