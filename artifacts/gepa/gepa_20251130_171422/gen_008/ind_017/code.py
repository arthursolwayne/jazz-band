
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDIClass()

# Set tempo (160 BPM)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempos = [pretty_midi.TempoChange(160, 0)]

# Define MIDI note numbers
F4 = 65
C5 = 72
G5 = 76
Bb5 = 77
D5 = 74
Bb4 = 71
F5 = 77  # Wait, F5 is actually 79
F5 = 79
E4 = 64
D4 = 62
C4 = 60
Bb3 = 59
Ab3 = 57
G3 = 67

# Define durations and times
BPM = 160
BEAT_DURATION = 60.0 / BPM  # 0.375 seconds per beat
BAR_DURATION = BEAT_DURATION * 4  # 1.5 seconds per bar
BEAT_TICKS = int( (60.0 / BPM) * pretty_midi.DEFAULT_RESOLUTION )  # 60 ticks per beat

# Define instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drums use percussion

# Create instruments
sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)

# Add instruments to the MIDI file
pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Define time for each bar
bar_start_times = [0, BAR_DURATION, 2 * BAR_DURATION, 3 * BAR_DURATION]

# Bar 1: Little Ray (drums) alone
drum_notes = [
    (pretty_midi.note_number_to_name(36), 0, 0),  # Kick on 1
    (pretty_midi.note_number_to_name(38), 1, 0),  # Snare on 2
    (pretty_midi.note_number_to_name(42), 2, 0),  # Hihat on 3
    (pretty_midi.note_number_to_name(38), 3, 0),  # Snare on 4
    (pretty_midi.note_number_to_name(42), 3, 0),  # Hihat on 4
    (pretty_midi.note_number_to_name(42), 0.5, 0.5),  # Hihat on 1
    (pretty_midi.note_number_to_name(42), 1.5, 0.5),  # Hihat on 2
    (pretty_midi.note_number_to_name(42), 2.5, 0.5),  # Hihat on 3
    (pretty_midi.note_number_to_name(42), 3.5, 0.5),  # Hihat on 4
]

for note_name, start, duration in drum_notes:
    note_number = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Everyone enters
# Bass line - chromatic walking
bass_notes = [
    (C4, 0, 0.5),  # C4
    (C4, 0.5, 0.5),  # C4
    (Bb3, 1, 0.5),  # Bb3
    (Bb3, 1.5, 0.5),  # Bb3
    (Ab3, 2, 0.5),  # Ab3
    (Ab3, 2.5, 0.5),  # Ab3
    (G3, 3, 0.5),  # G3
    (G3, 3.5, 0.5),  # G3
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    (F4, 1, 0.5), (Bb4, 1, 0.5), (C5, 1, 0.5), (F5, 1, 0.5),  # F7 on 2
    (F4, 3, 0.5), (Bb4, 3, 0.5), (C5, 3, 0.5), (F5, 3, 0.5),  # F7 on 4
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Saxophone - simple, haunting motif
sax_notes = [
    (E4, 0, 0.5),  # Start with E4
    (D4, 1, 0.5),  # Then D4
    (C4, 2, 0.5),  # Then C4
    (E4, 3, 0.5),  # End with E4, hanging
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 3
# Bass (chromatic walking)
bass_notes = [
    (G3, 0, 0.5),  # G3
    (G3, 0.5, 0.5),  # G3
    (F4, 1, 0.5),  # F4
    (F4, 1.5, 0.5),  # F4
    (E4, 2, 0.5),  # E4
    (E4, 2.5, 0.5),  # E4
    (D4, 3, 0.5),  # D4
    (D4, 3.5, 0.5),  # D4
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    (E4, 1, 0.5), (Bb4, 1, 0.5), (D5, 1, 0.5), (G5, 1, 0.5),  # E7 on 2
    (E4, 3, 0.5), (Bb4, 3, 0.5), (D5, 3, 0.5), (G5, 3, 0.5),  # E7 on 4
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Saxophone - motif variation
sax_notes = [
    (E4, 0, 0.5),  # E4
    (D4, 1, 0.5),  # D4
    (C4, 2, 0.5),  # C4
    (E4, 3, 0.5),  # E4
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 4
# Bass (chromatic walking)
bass_notes = [
    (D4, 0, 0.5),  # D4
    (D4, 0.5, 0.5),  # D4
    (C4, 1, 0.5),  # C4
    (C4, 1.5, 0.5),  # C4
    (Bb3, 2, 0.5),  # Bb3
    (Bb3, 2.5, 0.5),  # Bb3
    (Ab3, 3, 0.5),  # Ab3
    (Ab3, 3.5, 0.5),  # Ab3
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    (F4, 1, 0.5), (Bb4, 1, 0.5), (C5, 1, 0.5), (F5, 1, 0.5),  # F7 on 2
    (F4, 3, 0.5), (Bb4, 3, 0.5), (C5, 3, 0.5), (F5, 3, 0.5),  # F7 on 4
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Saxophone - motif variation
sax_notes = [
    (E4, 0, 0.5),  # E4
    (D4, 1, 0.5),  # D4
    (C4, 2, 0.5),  # C4
    (E4, 3, 0.5),  # E4
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro.mid")
print("MIDI file created: jazz_intro.mid")
