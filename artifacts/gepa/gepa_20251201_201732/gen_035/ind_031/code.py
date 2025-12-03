
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define key and time
key = 'D'  # D Major
time_signature = (4, 4)
bpm = 160
bar_length = 6.0  # seconds per 4 bars
beat_length = bar_length / 4  # 1.5 seconds per beat
note_length = beat_length / 2  # 0.75 seconds per half note

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Bar 1: Little Ray on drums (Kick on 1 and 3, Snare on 2 and 4, Hihat on every 8th)
# Time: 0.0 to 1.5 seconds

# Kick on 1 and 3
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.1)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6)

# Snare on 2 and 4
snare = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.85)
snare2 = pretty_midi.Note(velocity=90, pitch=38, start=1.5 * 3, end=1.6 * 3)

# Hihat on every 8th
hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.475)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.85)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.225)
hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6)
hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=1.975)
hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.35)
hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.725)

drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])
pm.instruments[2] = drums

# Bar 2: Marcus on bass (walking line - D2-G2, roots and fifths with chromatic approaches)

# D2 (D2)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + note_length)
bass.notes.append(note)

# Chromatic approach to G2 (F#2, G2)
note = pretty_midi.Note(velocity=100, pitch=40, start=1.5 + note_length, end=1.5 + 2*note_length)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=1.5 + 2*note_length, end=1.5 + 3*note_length)
bass.notes.append(note)

# G2
note = pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 3*note_length, end=1.5 + 4*note_length)
bass.notes.append(note)

# Bar 3: Diane on piano (open voicings, different chord each bar, resolve on the last)

# Bar 2: Dmaj7 (D, F#, A, C#)
note = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.5 + note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.5 + note_length)
piano.notes.append(note)

# Bar 3: Bm7 (B, D, F#, A)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5 + note_length, end=1.5 + 2*note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5 + note_length, end=1.5 + 2*note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=1.5 + note_length, end=1.5 + 2*note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5 + note_length, end=1.5 + 2*note_length)
piano.notes.append(note)

# Bar 4: Fmaj7 (F, A, C, E)
note = pretty_midi.Note(velocity=90, pitch=65, start=1.5 + 2*note_length, end=1.5 + 3*note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 2*note_length, end=1.5 + 3*note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 2*note_length, end=1.5 + 3*note_length)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=74, start=1.5 + 2*note_length, end=1.5 + 3*note_length)
piano.notes.append(note)

# Bar 4: You on sax (melody - one short motif, make it sing, leave it hanging)

# D (D4)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + note_length, end=1.5 + 1.5*note_length)
sax.notes.append(note)

# F# (F#4)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5*note_length, end=1.5 + 2*note_length)
sax.notes.append(note)

# A (A4)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 2*note_length, end=1.5 + 3*note_length)
sax.notes.append(note)

# Leave it hanging at A (you don't resolve in this bar — it’s the intro)
# D (D4) again
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3*note_length, end=1.5 + 3.5*note_length)
sax.notes.append(note)

# Save the MIDI file
pm.write('dante_intro.mid')
