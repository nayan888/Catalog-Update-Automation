#!/usr/bin/env python3

import os
import reports
import emails
from datetime import datetime

def get_summary():
    summary = ''
    desc_dir = os.path.join('supplier-data', 'descriptions')

    for txt in os.listdir(desc_dir):
        with open(os.path.join(desc_dir, txt)) as fp:
            summary += f'name: {fp.readline().strip()}<br/>weight: {fp.readline().strip()}<br/><br/>'
    
    return summary

def main():
    attachment = os.path.join('tmp', 'processed.pdf')
    title = f"Processed Update on {datetime.now().strftime('%d %b %Y')}"
    paragraph = get_summary()
    reports.generate_report(attachment, title, paragraph)

    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email('automation@example.com', 'student@example.com',
                                    'Upload Completed - Online Fruit Store',
                                    email_body, attachment)
    emails.send_email(message)


if __name__ == '__main__':
    main()