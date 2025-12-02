
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set the key to F minor (Fm)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0.0)]  # Fm is key number 5

# Define MIDI note numbers for the notes in F minor
# Fm scale: F, Gb, Ab, A, Bb, C, Db
scale_degrees = [0, 1, 3, 4, 5, 7, 8]  # Relative to F (note number 65)
scale_notes = [65 + d for d in scale_degrees]  # F = 65

# Define the instruments
# Tenor Sax: Program 64 (MIDI program for saxophone)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# Bass: Program 33 (Double Bass)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# Piano: Program 0 (Acoustic Piano)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# Drums: Program 128 (Drum Kit)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

# Time per bar: 1.5 seconds
bar_duration = 1.5
note_duration = bar_duration / 8  # 1/8 note = 0.1875 seconds
rest_duration = bar_duration / 4  # 1/4 rest = 0.375 seconds

# Bar 1: Drums only - setting the rhythm
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds for the start of the 4-bar section
start_time = 0.0

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.1875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 0.9375)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.5625)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75 * 3, end=start_time + 0.9375 * 3)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=start_time + i * 0.1875, end=start_time + i * 0.1875 + 0.0625)
    drums.notes.append(drum_hihat)

# Bar 2: All instruments in, Tenor Sax takes the melody

# Tenor Sax - short motif, with space and tension
# F (65), Ab (68), A (69), Bb (70) — a searching, unresolved phrase
note1 = pretty_midi.Note(velocity=100, pitch=65, start=start_time + 0.75, end=start_time + 0.75 + 0.1875)
note2 = pretty_midi.Note(velocity=100, pitch=68, start=start_time + 0.75 + 0.375, end=start_time + 0.75 + 0.375 + 0.1875)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=start_time + 0.75 + 0.75, end=start_time + 0.75 + 0.75 + 0.1875)
note4 = pretty_midi.Note(velocity=100, pitch=70, start=start_time + 0.75 + 1.125, end=start_time + 0.75 + 1.125 + 0.1875)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Bass: Walking line in Fm — chromatic approach
# F (65), Gb (66), Ab (68), A (69), Bb (70), C (72), Db (73), F (65)
# Walking in 8th notes with chromatic passes
bass_notes = [65, 66, 68, 69, 70, 72, 73, 65]
for i, pitch in enumerate(bass_notes):
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time + 0.75 + i * 0.1875, end=start_time + 0.75 + i * 0.1875 + 0.1875)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# F7 (F, A, C, Eb), Ab7 (Ab, C, Eb, Gb), A7 (A, C#, E, G), Bb7 (Bb, D, F, Ab)
# Comp on 2 and 4 of the second bar (i.e. at 1.125 and 1.5 seconds)

# F7 chord on beat 2 (1.125)
note_f = pretty_midi.Note(velocity=90, pitch=65, start=1.125, end=1.125 + 0.1875)
note_a = pretty_midi.Note(velocity=90, pitch=69, start=1.125, end=1.125 + 0.1875)
note_c = pretty_midi.Note(velocity=90, pitch=72, start=1.125, end=1.125 + 0.1875)
note_eb = pretty_midi.Note(velocity=90, pitch=67, start=1.125, end=1.125 + 0.1875)
piano.notes.append(note_f)
piano.notes.append(note_a)
piano.notes.append(note_c)
piano.notes.append(note_eb)

# Ab7 chord on beat 4 (1.5)
note_ab = pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.5 + 0.1875)
note_c2 = pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.5 + 0.1875)
note_eb2 = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + 0.1875)
note_gb = pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.5 + 0.1875)
piano.notes.append(note_ab)
piano.notes.append(note_c2)
piano.notes.append(note_eb2)
piano.notes.append(note_gb)

# Save the MIDI file
pm.write("jazz_intro_Fm.mid")
print("MIDI file saved as 'jazz_intro_Fm.mid'")
