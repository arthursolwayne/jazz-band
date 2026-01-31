
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time per bar (160 BPM, 4/4 time)
time_per_bar = 6.0  # seconds per bar
beat_time = time_per_bar / 4  # 1.5 seconds per beat
note_duration = beat_time / 2  # 0.75 seconds per half note

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)  # Tenor Sax

# Bar 1: Drums
# Kick on 1 & 3
kick = pretty_midi.Note(velocity=100, pitch=38, start=0, end=beat_time)
drums.notes.append(kick)
kick = pretty_midi.Note(velocity=100, pitch=38, start=2 * beat_time, end=3 * beat_time)
drums.notes.append(kick)

# Snare on 2 & 4
snare = pretty_midi.Note(velocity=100, pitch=43, start=1 * beat_time, end=1.5 * beat_time)
drums.notes.append(snare)
snare = pretty_midi.Note(velocity=100, pitch=43, start=3 * beat_time, end=3.5 * beat_time)
drums.notes.append(snare)

# Hihat on every 8th
hihat = pretty_midi.Note(velocity=80, pitch=63, start=0, end=beat_time / 2)
drums.notes.append(hihat)
hihat = pretty_midi.Note(velocity=80, pitch=63, start=beat_time / 2, end=beat_time)
drums.notes.append(hihat)
hihat = pretty_midi.Note(velocity=80, pitch=63, start=beat_time, end=1.5 * beat_time)
drums.notes.append(hihat)
hihat = pretty_midi.Note(velocity=80, pitch=63, start=1.5 * beat_time, end=2 * beat_time)
drums.notes.append(hihat)
hihat = pretty_midi.Note(velocity=80, pitch=63, start=2 * beat_time, end=2.5 * beat_time)
drums.notes.append(hihat)
hihat = pretty_midi.Note(velocity=80, pitch=63, start=2.5 * beat_time, end=3 * beat_time)
drums.notes.append(hihat)
hihat = pretty_midi.Note(velocity=80, pitch=63, start=3 * beat_time, end=3.5 * beat_time)
drums.notes.append(hihat)
hihat = pretty_midi.Note(velocity=80, pitch=63, start=3.5 * beat_time, end=4 * beat_time)
drums.notes.append(hihat)

pm.instruments.append(drums)

# Bar 2: Bass
# Walking line: D2 (38), A2 (45), C#2 (42), D2 (38)
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=0, end=beat_time)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=45, start=beat_time, end=2 * beat_time)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=42, start=2 * beat_time, end=3 * beat_time)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=3 * beat_time, end=4 * beat_time)
bass.notes.append(bass_note)

pm.instruments.append(bass)

# Bar 3: Piano
# Dmaj7 (D, F#, A, C#)
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=beat_time, end=1.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=beat_time, end=1.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=72, start=beat_time, end=1.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=75, start=beat_time, end=1.5 * beat_time)
piano.notes.append(piano_note)

# G7 (G, B, D, F)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=2 * beat_time, end=2.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=71, start=2 * beat_time, end=2.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=69, start=2 * beat_time, end=2.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=65, start=2 * beat_time, end=2.5 * beat_time)
piano.notes.append(piano_note)

# Cmaj7 (C, E, G, B)
piano_note = pretty_midi.Note(velocity=100, pitch=60, start=3 * beat_time, end=3.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=64, start=3 * beat_time, end=3.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=3 * beat_time, end=3.5 * beat_time)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=71, start=3 * beat_time, end=3.5 * beat_time)
piano.notes.append(piano_note)

pm.instruments.append(piano)

# Bar 4: Tenor Sax
# Motif: D (62), E (64), D (62), C# (63) — half note on last
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=0, end=beat_time)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=64, start=beat_time, end=2 * beat_time)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=2 * beat_time, end=3 * beat_time)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=63, start=3 * beat_time, end=4 * beat_time)
sax.notes.append(sax_note)

pm.instruments.append(sax)

# Write to MIDI file
pm.write("dante_intro.mid")
