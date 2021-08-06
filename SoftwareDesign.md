<h2>Software Design</h2>

 - [Read the prompt](https://docs.google.com/document/d/1ehzPRJoRrdmy3Bu9h9BQk6_4Q18dNMt4Ukho_GGgyuQ/edit)


<h5>Components</h5>

<div>
	A. At first we create all components that we'll need for our system
		with attributes& methods
</div>

1. Person (base class for Student & Professor as they're required to have similar ingo)
	- first_name: string
	- last_name: string
	- dateOfBirth: date (as age constantly changes -> use date of birth)
	- phoneNumber: string

2. Student class
	- international: boolean (if not -> local)
	- isPartTime(): boolean (if > than enrlolled theshold -> full else parttime)
	- isOnProbation(): boolean

3. Professor class
	- salary: float

4. Address (separate it from Person to make it easier for DB, as example)
	- country: string
	- state: string
	- city: string
	- street address: string
	- postal_code: string

5. Course class
	- name: string
	- code: string
	- minStudents: int
	- maxStudents: int
	- isCancelled(): boolean (if enough -> not cancelled else cancelled)
	- start: date
	- end: date

6. Enrol (links Student & Course)
	- date: date (when each student is enrolled)
	- grade: float (what each student receives)

<h5>Associations</h5>

<div>

	B. 
	- Next step is to define associations, i.e. how each class will interact with each other; so when we create class A, class B will be linked to it in some way. We define `multiplicity` of our association: how many of those classes can be associated together.
	PS: association generally is a solid line, `-`, without arrows
	PPS: `1---1..*` means  one class will have link to 1 to many other class

	 - About classes
		`-`: attribute
		`+`: method

	- Generalization is link between classes, `->`, which shows how
		classes are connected with each other

</div>

 - Preface: `Enrol` class is an <i>association class</i>: it links two classes together. It's linked to the association line between 2 classes.

```bash
		Person(base class)	1-----1..* Address
			- first_name		- country
			- last_name		- state	
			- dateOfBirth 		- city
			- phoneNumber		- street address
						- postal code
		 ^			 ^	
		/			  \
	  Student(child)		Professor(child) 1..* ----------|			
		- international		 - salary			|
		+ isPartTime()			 			|
		+ isOnProbation()                                   	|
		      0..* 				 		|
			|								 					
			|					      0..* Course
			|------------------------------------- 0..6 	   - name
						|			   - code
					Enrol(association class)	   - minStudents
						 - grade		   - maxStudent
						 - date			   + isCancelled
									   - start
									   - end

```

	- Post explanation: one `Person` has 1 to many addresses. But `Address` can be attached only to one `Person`. One`Professor` can teach many courses. Each `Course` has from 1 to many professors. Every `Student` has from 0 to 6 courses. Each `Course` can have from 0 to many students.

	- + If `Professor` needs to update student info, then it goes to associated class `Course`, this class is associated with `Enrol` and it has all info about `Student`. Hence professor doesn't need to sift through all students, but !!! change grade in `Enrol` class and it'll be updated in both `Course` & `Student`. Also, to look at the avg for the course we can look at ALL associations between `Student` & particular course, use `Enrol` to get the avg grade 
