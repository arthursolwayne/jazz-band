
import pretty_midi

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key to F major
# F major scale: F, G, A, Bb, C, D, E
# We'll use this to construct the notes

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI uses piano for drums
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Time per bar in seconds: 6.0 seconds / 4 bars = 1.5 seconds per bar
# Note: 160 BPM = 60 / 160 = 0.375 seconds per beat

# Define the note durations in seconds
note_duration = 0.375  # One beat
eighth_note = 0.1875
sixteenth_note = 0.09375

# Define the F major scale (in MIDI note numbers)
# F = 65, G = 67, A = 69, Bb = 70, C = 72, D = 74, E = 76
f_major = [65, 67, 69, 70, 72, 74, 76]

# --- Bar 1: Little Ray (drums) alone ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: 0.0s to 1.5s

# Kick on 1 (0.0s) and 3 (1.125s)
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + note_duration)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.125 + note_duration)
drums.notes.append(kick1)
drums.notes.append(kick2)

# Snare on 2 (0.375s) and 4 (1.5s)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.375 + note_duration)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + note_duration)
drums.notes.append(snare1)
drums.notes.append(snare2)

# Hi-hat on every eighth note
hi_hat_notes = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]
for start in hi_hat_notes:
    hi_hat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + sixteenth_note)
    drums.notes.append(hi_hat)

# --- Bar 2: Everyone enters, sax takes melody ---

# Time for Bar 2: 1.5s to 3.0s

# Bass: Walking line in F, chromatic approaches, never the same note twice
# Using F scale and chromatic notes around it
bass_notes = [
    (1.5, 70),  # Bb
    (1.875, 72),  # C
    (2.25, 74),  # D
    (2.625, 72),  # C
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_duration)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# First bar: 1.5s to 3.0s
# Chords on beat 2 (1.875s) and 4 (3.0s)

# F7 chord: F, A, C, E (65, 69, 72, 76)
chord1_notes = [65, 69, 72, 76]
for note in chord1_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=1.875, end=1.875 + note_duration)
    piano.notes.append(piano_note)

# Next chord on beat 4 (3.0s)
# F7 again
for note in chord1_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=3.0, end=3.0 + note_duration)
    piano.notes.append(piano_note)

# Sax: Melody — one short motif, make it sing. Start it, leave it hanging.

# Use this motif:
# F (65) on beat 1 (1.5s)
# G (67) on beat 2 (1.875s)
# A (69) on beat 3 (2.25s)
# Leave it hanging — don't resolve on beat 4

sax_note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + note_duration)
sax_note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + note_duration)
sax_note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + note_duration)
sax.notes.append(sax_note1)
sax.notes.append(sax_note2)
sax.notes.append(sax_note3)

# --- Bar 3 and 4: Continue with the same idea ---

# Time for Bar 3: 3.0s to 4.5s

# Bass: Walking line, continue chromatic movement
bass_notes_bar3 = [
    (3.0, 70),  # Bb
    (3.375, 72),  # C
    (3.75, 74),  # D
    (4.125, 72),  # C
]
for start, pitch in bass_notes_bar3:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_duration)
    bass.notes.append(note)

# Piano: 7th chords again on 2 and 4
chord2_notes = [65, 69, 72, 76]
piano_note = pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.375 + note_duration)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.375 + note_duration)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.375 + note_duration)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.375 + note_duration)
piano.notes.append(piano_note)

# On beat 4 (4.5s) again
for note in chord1_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=4.5, end=4.5 + note_duration)
    piano.notes.append(piano_note)

# Drums: Continue with the same pattern
# Kick on 1 (3.0s) and 3 (4.125s)
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.0 + note_duration)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.125 + note_duration)
drums.notes.append(kick3)
drums.notes.append(kick4)

# Snare on 2 (3.375s) and 4 (4.5s)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.375 + note_duration)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.5 + note_duration)
drums.notes.append(snare3)
drums.notes.append(snare4)

# Hi-hat on every eighth
hi_hat_notes_bar3 = [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125]
for start in hi_hat_notes_bar3:
    hi_hat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + sixteenth_note)
    drums.notes.append(hi_hat)

# Sax: Continue the motif, but don’t resolve. End with a question.
# Motif: F (65), G (67), A (69) — leave it on A.

sax_note4 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + note_duration)
sax.notes.append(sax_note4)
sax_note5 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.375 + note_duration)
sax.notes.append(sax_note5)
sax_note6 = pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.75 + note_duration)
sax.notes.append(sax_note6)

# Write the MIDI file to disk
midi.write('jazz_intro_in_f.mid')
