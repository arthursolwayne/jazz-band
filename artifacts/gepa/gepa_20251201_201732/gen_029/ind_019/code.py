
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to F minor (Fm)
key_signature = pretty_midi.KeySignature(key_number=21)  # F minor
pm.key_signature = key_signature

# Define time signature (4/4)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4)
pm.time_signature = time_signature

# Create instruments
# 1. Bass (Marcus)
bass_program = Program(program=33)  # Acoustic Bass
bass_instrument = Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# 2. Piano (Diane)
piano_program = Program(program=0)  # Acoustic Grand Piano
piano_instrument = Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 3. Drums (Little Ray)
drum_program = Program(program=128)  # Acoustic Drums
drum_instrument = Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# 4. Tenor Sax (You)
sax_program = Program(program=66)  # Tenor Saxophone
sax_instrument = Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Define timing parameters
beats_per_bar = 4
beat_duration = 60.0 / 160  # 0.375 seconds per beat
bar_duration = beat_duration * beats_per_bar  # 1.5 seconds per bar
time = 0.0

# Bar 1: Little Ray alone (drums only)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1
note = Note(velocity=80, start=time, end=time + 0.1)
note.pitch = 36  # Kick drum
drum_instrument.notes.append(note)

# Snare on 2
note = Note(velocity=90, start=time + beat_duration, end=time + beat_duration + 0.1)
note.pitch = 38  # Snare drum
drum_instrument.notes.append(note)

# Hihat on every eighth
for i in range(8):
    note = Note(velocity=60, start=time + i * beat_duration / 2, end=time + i * beat_duration / 2 + 0.05)
    note.pitch = 42  # Hihat
    drum_instrument.notes.append(note)

time += bar_duration

# Bar 2: Everyone in, Diane plays a chord (Fm7)
# Diane: Fm7 (F, Ab, C, Eb) as open voicing
# Time: bar 2, beat 2 (comp on 2 and 4)
diane_note1 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note1.pitch = 71  # F (C4)
piano_instrument.notes.append(diane_note1)

diane_note2 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note2.pitch = 67  # Ab (E4)
piano_instrument.notes.append(diane_note2)

diane_note3 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note3.pitch = 76  # C (G4)
piano_instrument.notes.append(diane_note3)

diane_note4 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note4.pitch = 70  # Eb (F#4)
piano_instrument.notes.append(diane_note4)

# Marcus: Walking bass line (Fm)
# F, Gb, E, D, C, Bb, B, C
# Convert to MIDI notes
# F2 = 53, Gb2 = 54, E2 = 51, D2 = 50, C2 = 48, Bb2 = 46, B2 = 49, C2 = 48
bass_notes = [53, 54, 51, 50, 48, 46, 49, 48]
for i, pitch in enumerate(bass_notes):
    start = time + (i * beat_duration / 2)
    end = start + 0.1
    note = Note(velocity=90, start=start, end=end, pitch=pitch)
    bass_instrument.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4

# Kick on 1
note = Note(velocity=80, start=time, end=time + 0.1)
note.pitch = 36  # Kick drum
drum_instrument.notes.append(note)

# Snare on 2
note = Note(velocity=90, start=time + beat_duration, end=time + beat_duration + 0.1)
note.pitch = 38  # Snare drum
drum_instrument.notes.append(note)

# Hihat on every eighth
for i in range(8):
    note = Note(velocity=60, start=time + i * beat_duration / 2, end=time + i * beat_duration / 2 + 0.05)
    note.pitch = 42  # Hihat
    drum_instrument.notes.append(note)

time += bar_duration

# Bar 3: Diane plays a new chord (Abmaj7)
# Abmaj7 (Ab, C, Eb, G) - open voicing
# Time: comp on 2 and 4
diane_note1 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note1.pitch = 64  # Ab (D4)
piano_instrument.notes.append(diane_note1)

diane_note2 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note2.pitch = 72  # C (G4)
piano_instrument.notes.append(diane_note2)

diane_note3 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note3.pitch = 70  # Eb (F#4)
piano_instrument.notes.append(diane_note3)

diane_note4 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note4.pitch = 76  # G (A4)
piano_instrument.notes.append(diane_note4)

# Marcus continues walking bass line
bass_notes = [54, 51, 50, 48, 46, 49, 48, 50]
for i, pitch in enumerate(bass_notes):
    start = time + (i * beat_duration / 2)
    end = start + 0.1
    note = Note(velocity=90, start=start, end=end, pitch=pitch)
    bass_instrument.notes.append(note)

# Little Ray again: Kick 1, Snare 2
note = Note(velocity=80, start=time, end=time + 0.1)
note.pitch = 36
drum_instrument.notes.append(note)

note = Note(velocity=90, start=time + beat_duration, end=time + beat_duration + 0.1)
note.pitch = 38
drum_instrument.notes.append(note)

# Hihat
for i in range(8):
    note = Note(velocity=60, start=time + i * beat_duration / 2, end=time + i * beat_duration / 2 + 0.05)
    note.pitch = 42
    drum_instrument.notes.append(note)

time += bar_duration

# Bar 4: Diane resolves to Cm7
# Cm7 (C, Eb, Gb, Bb)
# Comp on 2 and 4
diane_note1 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note1.pitch = 60  # C (C4)
piano_instrument.notes.append(diane_note1)

diane_note2 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note2.pitch = 68  # Eb (G4)
piano_instrument.notes.append(diane_note2)

diane_note3 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note3.pitch = 65  # Gb (F4)
piano_instrument.notes.append(diane_note3)

diane_note4 = Note(velocity=100, start=time + beat_duration, end=time + beat_duration + 0.2)
diane_note4.pitch = 62  # Bb (D4)
piano_instrument.notes.append(diane_note4)

# Marcus continues walking bass
bass_notes = [51, 50, 48, 46, 49, 48, 50, 48]
for i, pitch in enumerate(bass_notes):
    start = time + (i * beat_duration / 2)
    end = start + 0.1
    note = Note(velocity=90, start=start, end=end, pitch=pitch)
    bass_instrument.notes.append(note)

# Little Ray: Kick 1, Snare 2
note = Note(velocity=80, start=time, end=time + 0.1)
note.pitch = 36
drum_instrument.notes.append(note)

note = Note(velocity=90, start=time + beat_duration, end=time + beat_duration + 0.1)
note.pitch = 38
drum_instrument.notes.append(note)

# Hihat
for i in range(8):
    note = Note(velocity=60, start=time + i * beat_duration / 2, end=time + i * beat_duration / 2 + 0.05)
    note.pitch = 42
    drum_instrument.notes.append(note)

time += bar_duration

# Saxophone: You — the melody. One short motif, leave it hanging.

# Bars 1-4: Your motif (start on bar 2, beat 1)
# Fm: F, Ab, C, Eb
# Motif: F (1), Ab (2), C (3), rest on 4 — then return in bar 4

# Bar 2: Start of motif
note = Note(velocity=100, start=time - bar_duration + beat_duration, end=time - bar_duration + beat_duration + 0.1)
note.pitch = 71  # F (C4)
sax_instrument.notes.append(note)

note = Note(velocity=100, start=time - bar_duration + beat_duration * 2, end=time - bar_duration + beat_duration * 2 + 0.1)
note.pitch = 67  # Ab (E4)
sax_instrument.notes.append(note)

note = Note(velocity=100, start=time - bar_duration + beat_duration * 3, end=time - bar_duration + beat_duration * 3 + 0.1)
note.pitch = 76  # C (G4)
sax_instrument.notes.append(note)

# Bar 4: Return to the motif — a whisper
note = Note(velocity=70, start=time - beat_duration, end=time - beat_duration + 0.1)
note.pitch = 71  # F (C4)
sax_instrument.notes.append(note)

note = Note(velocity=70, start=time - beat_duration * 2, end=time - beat_duration * 2 + 0.1)
note.pitch = 67  # Ab (E4)
sax_instrument.notes.append(note)

note = Note(velocity=70, start=time - beat_duration * 3, end=time - beat_duration * 3 + 0.1)
note.pitch = 76  # C (G4)
sax_instrument.notes.append(note)

# Write the MIDI file
pm.write("intro_in_Fm.mid")
