import { GoHome, GoSearch } from "react-icons/go";
import { MdLocalLibrary, MdRecommend } from "react-icons/md";
import { SiBookstack } from "react-icons/si";

export const defaultAuthors = [
  { frontendValue: 'Joanne Rowling', backendValue: 'J. K. Rowling' },
  { frontendValue: 'Antoine de Saint-Exupéry', backendValue: 'Antoine de Saint-ExupÃ©ry' },
  { frontendValue: 'Orson Card', backendValue: 'Orson Scott Card' },
  { frontendValue: 'Stephen Chbosky', backendValue: 'Stephen Chbosky' },
  { frontendValue: 'John Tolkien', backendValue: 'J.R.R. TOLKIEN' },
  { frontendValue: 'Lois Lowry', backendValue: 'LOIS LOWRY' },
  { frontendValue: 'Daniel Quinn', backendValue: 'Daniel Quinn' },
  { frontendValue: 'Jhumpa Lahiri', backendValue: 'Jhumpa Lahiri' },
  { frontendValue: 'Anne Frank', backendValue: 'ANNE FRANK' },
  { frontendValue: 'Elwyn White', backendValue: 'E. B. White' }
];

export const links = [
  { name: 'Home', to: '/', icon: GoHome },
  { name: 'Search', to: '/search', icon: GoSearch },
  { name: 'Your Library', to: '/rated-books', icon: MdLocalLibrary },
  { name: 'Recommendations', to: '/book-recommendations', icon: SiBookstack},
];

export default links;