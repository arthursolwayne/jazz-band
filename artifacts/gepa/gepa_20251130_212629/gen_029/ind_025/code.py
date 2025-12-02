
import pretty_midi
import numpy as np

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax (program 64)
pm.instruments.append(instrument)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Create a single note to build tension in Bar 1 (Ray on drums)
# This is the "waiting" moment — a kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use a percussion track for this (but we'll simulate it using note events for clarity)

# Bar 1: Drums only (simulated)
# Time per beat: 0.375s (at 160 BPM)
# Bar length: 1.5s

# Kick on 1 and 3 (0.0s and 0.75s)
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.075)
instrument.notes.append(kick_note)
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.825)
instrument.notes.append(kick_note)

# Snare on 2 and 4 (0.375s and 1.125s)
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.45)
instrument.notes.append(snare_note)
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.2)
instrument.notes.append(snare_note)

# Hihat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5)
hihat_notes = [0.0, 0.375, 0.75, 1.125, 1.5]
for t in hihat_notes:
    hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.1)
    instrument.notes.append(hihat_note)

# Bar 2: All instruments enter
# You take the melody — short motif, sing it, leave it hanging

# Start of Bar 2: 1.5s
# Tenor sax motif in Fm (Fm7 chord: F, Ab, C, Eb)
# Use chromatic + syncopation to create tension

# F (F4) on beat 1
note = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6)
instrument.notes.append(note)

# Ab (Ab4) on an off-beat (beat 1 + 0.25)
note = pretty_midi.Note(velocity=105, pitch=68, start=1.75, end=1.9)
instrument.notes.append(note)

# C (C5) on the end of beat 2 (beat 2 is 1.875s)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0)
instrument.notes.append(note)

# Eb (Eb4) on the end of beat 3 (beat 3 is 2.25s) — leave it hanging
note = pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.375)
instrument.notes.append(note)

# Bass line: Marcus — walking line, chromatic approaches, no repeated notes
# Bar 2: Fm7 chord (F, Ab, C, Eb) — walk around it with chromatic notes

# Start of Bar 2: F (F2)
note = pretty_midi.Note(velocity=70, pitch=48, start=1.5, end=1.6)
instrument.notes.append(note)

# Chromatic down: Eb (Eb2) on beat 2 (1.875)
note = pretty_midi.Note(velocity=70, pitch=47, start=1.875, end=1.95)
instrument.notes.append(note)

# D (D2) on beat 3 (2.25)
note = pretty_midi.Note(velocity=70, pitch=46, start=2.25, end=2.325)
instrument.notes.append(note)

# C (C2) on beat 4 (2.625)
note = pretty_midi.Note(velocity=70, pitch=45, start=2.625, end=2.7)
instrument.notes.append(note)

# Piano: Diane — 7th chords, comp on 2 and 4
# Fm7 chord: F, Ab, C, Eb

# Bar 2: comp on beat 2 and 4

# Beat 2 (1.875s): Fm7
note = pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.0)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.0)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=72, start=1.875, end=2.0)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0)
instrument.notes.append(note)

# Beat 4 (2.625s): Fm7
note = pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=2.8)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=2.8)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=72, start=2.625, end=2.8)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.8)
instrument.notes.append(note)

# Bar 3: All instruments in, but no new melody — keep the feeling of waiting
# Add a subtle delay and dynamic shift in the tenor line to create space

# Tenor sax: restate the motif but with a slight delay and softer dynamic
# Start at 2.8s (beginning of Bar 3)

note = pretty_midi.Note(velocity=95, pitch=65, start=2.8, end=2.9)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=3.05, end=3.2)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=72, start=3.125, end=3.3)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5)
instrument.notes.append(note)

# Bar 4: End with a question — leave the motif incomplete
# Tenor sax: start the motif again, but end on the Eb, leaving it unresolved

note = pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.6)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=105, pitch=68, start=3.75, end=3.9)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=105, pitch=69, start=4.25, end=4.375)
instrument.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file saved as 'dante_intro.mid'")
