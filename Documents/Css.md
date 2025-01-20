#language
Css (Cascading Style Sheets) is a programming language used in [[Website Development]] with [[Html]]to style websites. Css takes the name of the element (the object on the page) and then curly brackets where you then place the things you want to style this can be background color to font or font-size. A Css framework would be Bootstrap.
## Classes 

Classes are used when you want to style a bunch of different stuff that isn't a built in element like body, header, etc. this can be done with the `.classname {}`
#### Pseudo Classes
or effects are used to be even more specific with what elements look like based on what the user has done an example is the hover effect which will change the style based on the (You guessed it) user hovering of the element. This done using the `.classname:hover {}` 
## Ids
Ids are classes but when only used on one specific element and will take a higher priority than classes. done with the `#id_name {}`
## Media Queries  
Media queries are used to change the style of your website based on the size of the device you are using, the orientation of the device, and other variations. It is an important part of responsive design. This is done with `@media (max/min-width) {<element>}`

## Flexbox and Css Grid
Flexbox and Css Grid are powerful layout systems used to give your website a responsive look.

#### Flexbox
Flex box is used to make one-dimensional layouts like columns and rows. Flexbox works with the flex box parent container and the child items. The container is made with `display: flex;` .  The most commonly used properties are:
- `flex-direction`: will determine the direction the items are laid out in the flex container.
  - `row` (default): items are laid out in a row right to left
  - `row-reverse`: items are laid out in a row, from right to left.
  - `column`: items are laid out in a column, from top to bottom
  - `column-reverse`: items laid out in a column, bottom to top  
- **`align-items`**: Aligns the flex items along the cross axis (perpendicular to the main axis).
 - `stretch` (default): Items stretch to fill the container (only if the item has no set height).
 - `flex-start`: Items are aligned to the start of the cross axis.
 - `flex-end`: Items are aligned to the end of the cross axis.
 - `center`: Items are centered along the cross axis.
 - `baseline`: Items are aligned such that their baselines align.
-  **`justify-content`**: Aligns the flex items along the main axis (horizontally for `row`, vertically for `column`).
 - `flex-start` (default): Items are packed toward the start of the main axis.
 - `flex-end`: Items are packed toward the end of the main axis.
 - `center`: Items are centered along the main axis.
 - `space-between`: Items are evenly distributed, with the first item at the start and the last item at the end.
 - `space-around`: Items are evenly distributed, with equal space around them.
 - `space-evenly`: Items are evenly distributed with equal space between them.
- **`align-content`**: Aligns the flex lines when there is extra space in the cross axis. This property is used when there are multiple lines of flex items.
 - `stretch` (default): Lines stretch to take up the remaining space.
 - `flex-start`: Lines are packed toward the start of the cross axis.
 - `flex-end`: Lines are packed toward the end of the cross axis.
 - `center`: Lines are centered along the cross axis.
 - `space-between`: Lines are evenly distributed with the first line at the start and the last line at the end.
 - `space-around`: Lines are evenly distributed with equal space around them.
 - `space-evenly`: Lines are evenly distributed with equal space between them.
- **`flex-wrap`**: Controls whether the flex items should wrap onto multiple lines if they overflow the container.
 - `nowrap` (default): All items are placed in a single line.
 - `wrap`: Items wrap onto multiple lines, from top to bottom.
 - `wrap-reverse`: Items wrap onto multiple lines, from bottom to top.
- **`flex-grow`**: Allows a flex item to grow to fill the available space in the flex container.
 - A value of `1` means the item can grow to fill the available space.
 - A value of `0` (default) means the item will not grow.
#### Css Grid 
Css Grid is the two-dimensional version of Flexbox allowing even more customization as it can handle rows and columns simultaneously. Css has the same parent container and child item system as flexbox and is made with `display:grid;`. 
- **`grid-template-columns`**: Defines the number and size of columns in the grid.
 - Example: `grid-template-columns: 200px 1fr 100px;`
 - Example: `grid-template-columns: repeat(3, 1fr);`
- **`grid-template-rows`**: Defines the number and size of rows in the grid.
 - Example: `grid-template-rows: 100px auto 100px;`
 - Example: `grid-template-rows: repeat(3, 1fr);`
-  **`grid-template-areas`**: Defines named grid areas for easier placement of grid items.
- **`grid-gap`**, **`column-gap`**, and **`row-gap`**: Define the spacing between grid items.
- **`justify-items`**: Aligns grid items horizontally within their grid area.
 - Values: `start`, `end`, `center`, `stretch` (default)
- **`align-items`**: Aligns grid items vertically within their grid area.
- **`justify-content`**: Aligns the entire grid horizontally within the grid container.
  - Values: `start`, `end`, `center`, `stretch`, `space-around`, `space-between`, `space-evenly`
- **`align-content`**: Aligns the entire grid vertically within the grid container.
  - Values: `start`, `end`, `center`, `stretch`, `space-around`, `space-between`, `space-evenly`
- **`fr` (fraction unit)**: A flexible length unit that represents a fraction of the available space.
  - Example: `grid-template-columns: 1fr 2fr;` (The second column will take twice as much space as the first)