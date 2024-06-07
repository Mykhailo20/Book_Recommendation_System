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

export const defaultTitles = [
  "1984",
  "2nd Chance",
  "4 Blondes",
  "Year of Wonders",
  "Harry Potter and the Sorcerer's Stone (Book 1)",
  "Zen and the Art of Motorcycle Maintenance: An Inquiry into Values",
  "Dragonfly in Amber",
  "Brave New World",
  "Anne of the Island",
  "Where the Red Fern Grows"
]

export const links = [
  { name: 'Home', to: '/', icon: GoHome },
  { name: 'Search', to: '/search', icon: GoSearch },
  { name: 'Your Library', to: '/rated-books', icon: MdLocalLibrary },
  { name: 'Recommendations', to: '/book-recommendations', icon: SiBookstack},
];

export default links;