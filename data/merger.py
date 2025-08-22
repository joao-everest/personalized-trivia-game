# import json
# import os

# def merge_quiz_files():
#     # Define your file mappings (adjust file names as needed)
#     file_category_mapping = {
#         'history.json': 'History',
#         'geography.json': 'Geography', 
#         'science.json': 'Science & Nature',
#         'entertainment.json': 'Pop Culture & Entertainment',
#         'sports.json': 'Sports',
#         'arts.json': 'Arts & Literature'
#     }
    
#     all_questions = []
    
#     # Process each file
#     for filename, category in file_category_mapping.items():
#         try:
#             # Check if file exists
#             if not os.path.exists(filename):
#                 print(f"Warning: {filename} not found, skipping...")
#                 continue
                
#             # Load JSON file
#             with open(filename, 'r', encoding='utf-8') as file:
#                 questions = json.load(file)
            
#             # Add category to each question
#             for question in questions:
#                 question['category'] = category
#                 all_questions.append(question)
            
#             print(f"✓ Processed {filename}: {len(questions)} questions added")
            
#         except json.JSONDecodeError:
#             print(f"Error: {filename} contains invalid JSON")
#         except Exception as e:
#             print(f"Error processing {filename}: {e}")
    
#     # Save merged file
#     output_filename = 'all_quiz_questions.json'
    
#     try:
#         with open(output_filename, 'w', encoding='utf-8') as output_file:
#             json.dump(all_questions, output_file, indent=2, ensure_ascii=False)
        
#         print(f"\n🎉 Success! Merged {len(all_questions)} questions into '{output_filename}'")
        
#         # Show summary
#         category_counts = {}
#         for question in all_questions:
#             category = question['category']
#             category_counts[category] = category_counts.get(category, 0) + 1
        
#         print("\nSummary by category:")
#         for category, count in category_counts.items():
#             print(f"  {category}: {count} questions")
            
#     except Exception as e:
#         print(f"Error saving merged file: {e}")

# if __name__ == "__main__":
#     merge_quiz_files()

import json
import os

def merge_quiz_files():
    # Define your file mappings (adjust file names as needed)
    file_category_mapping = {
        'history.json': 'History',
        'geography.json': 'Geography', 
        'science.json': 'Science & Nature',
        'entertainment.json': 'Pop Culture & Entertainment',
        'sports.json': 'Sports',
        'arts.json': 'Arts & Literature'
    }
    
    all_questions = []
    
    # Process each file
    question_counter = 1  # Global counter for unique IDs
    
    for filename, category in file_category_mapping.items():
        try:
            # Check if file exists
            if not os.path.exists(filename):
                print(f"Warning: {filename} not found, skipping...")
                continue
                
            # Load JSON file
            with open(filename, 'r', encoding='utf-8') as file:
                questions = json.load(file)
            
            # Add category and update question_id for each question
            for question in questions:
                question['category'] = category
                question['question_id'] = question_counter  # Convert to integer
                question_counter += 1
                all_questions.append(question)
            
            print(f"✓ Processed {filename}: {len(questions)} questions added")
            
        except json.JSONDecodeError:
            print(f"Error: {filename} contains invalid JSON")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    # Save merged file
    output_filename = 'all_quiz_questions.json'
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            json.dump(all_questions, output_file, indent=2, ensure_ascii=False)
        
        print(f"\n🎉 Success! Merged {len(all_questions)} questions into '{output_filename}'")
        
        # Show summary
        category_counts = {}
        for question in all_questions:
            category = question['category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        print("\nSummary by category:")
        for category, count in category_counts.items():
            print(f"  {category}: {count} questions")
            
    except Exception as e:
        print(f"Error saving merged file: {e}")

if __name__ == "__main__":
    merge_quiz_files()