
import pretty_midi
from pretty_midi import Note, NoteList, Instrument

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to D minor (Dm)
key = pretty_midi.key_number_to_key_signature(1)  # D minor

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Define the tempo (160 BPM)
midi.tempo_changes.append(pretty_midi.TempoChange(160, 0))

# Define instrument programs
SAXOPHONE_PROGRAM = 64
BASS_PROGRAM = 33
PIANO_PROGRAM = 0
DRUMS_PROGRAM = 0

# Create instruments
sax = Instrument(program=SAXOPHONE_PROGRAM, is_drum=False)
bass = Instrument(program=BASS_PROGRAM, is_drum=False)
piano = Instrument(program=PIANO_PROGRAM, is_drum=False)
drums = Instrument(program=DRUMS_PROGRAM, is_drum=True)

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Duration per beat (in seconds)
beats_per_bar = 4
notes_per_beat = 4
beat_duration = 60.0 / 160.0  # 0.375 seconds per beat
bar_duration = beat_duration * beats_per_bar  # 1.5 seconds per bar

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(beats_per_bar):
        time = bar * bar_duration + beat * beat_duration
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = Note(36, time, beat_duration * 0.3, velocity=100)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = Note(38, time, beat_duration * 0.3, velocity=100)
            drums.notes.append(note)
        # Hi-hat on every eighth
        for eighth in range(2):
            note_time = time + (eighth * beat_duration / 2)
            note = Note(42, note_time, beat_duration / 2 * 0.2, velocity=80)
            drums.notes.append(note)

# Bar 2-4: Everyone in, saxophone motif

# Define the saxophone motif (Dm scale: D, Eb, F, G, Ab, Bb, C)
# Motif: D (beat 1), rest (beat 2), F (beat 3), rest (beat 4)
# But with rhythmic variation and a unique twist: syncopated on beat 2 and 4

sax_notes = []

# Bar 2
# Beat 1: D (note 62), quarter note
note = Note(62, 1.5, 0.375, velocity=100)
sax.notes.append(note)

# Beat 2: Rest
# No note on beat 2, but syncopated eighth on the "and" of 2
note = Note(62, 1.5 + 0.1875, 0.125, velocity=100)
sax.notes.append(note)

# Beat 3: F (note 65), quarter note
note = Note(65, 1.5 + 0.375, 0.375, velocity=100)
sax.notes.append(note)

# Beat 4: Rest
# Syncopated eighth on the "and" of 4
note = Note(65, 1.5 + 0.75 + 0.1875, 0.125, velocity=100)
sax.notes.append(note)

# Bar 3
# Repeat motif, but with variation: shift to Eb (note 61) on beat 1
note = Note(61, 1.5 * 2, 0.375, velocity=100)
sax.notes.append(note)

# Syncopated eighth on "and" of 2
note = Note(61, 1.5 * 2 + 0.1875, 0.125, velocity=100)
sax.notes.append(note)

# Beat 3: G (note 67), quarter note
note = Note(67, 1.5 * 2 + 0.375, 0.375, velocity=100)
sax.notes.append(note)

# Syncopated eighth on "and" of 4
note = Note(67, 1.5 * 2 + 0.75 + 0.1875, 0.125, velocity=100)
sax.notes.append(note)

# Bar 4
# Repeat motif, now with a variation: shift to Bb (note 62) on beat 1
note = Note(62, 1.5 * 3, 0.375, velocity=100)
sax.notes.append(note)

# Syncopated eighth on "and" of 2
note = Note(62, 1.5 * 3 + 0.1875, 0.125, velocity=100)
sax.notes.append(note)

# Beat 3: C (note 69), quarter note
note = Note(69, 1.5 * 3 + 0.375, 0.375, velocity=100)
sax.notes.append(note)

# Syncopated eighth on "and" of 4
note = Note(69, 1.5 * 3 + 0.75 + 0.1875, 0.125, velocity=100)
sax.notes.append(note)

# Bass line: Walking line, chromatic approaches
# Starts on D (62), walks down to C (60), then up to D (62)
# Bar 2: D -> C -> Bb -> B
# Bar 3: B -> C -> D -> Eb
# Bar 4: Eb -> D -> C -> Bb

bass_notes = []
for bar in range(2, 4):
    bar_start = bar * bar_duration
    for beat in range(4):
        time = bar_start + beat * beat_duration
        if bar == 2:
            if beat == 0:
                note = Note(62, time, beat_duration * 0.2, velocity=80)
            elif beat == 1:
                note = Note(60, time, beat_duration * 0.2, velocity=80)
            elif beat == 2:
                note = Note(59, time, beat_duration * 0.2, velocity=80)
            elif beat == 3:
                note = Note(60, time, beat_duration * 0.2, velocity=80)
        elif bar == 3:
            if beat == 0:
                note = Note(60, time, beat_duration * 0.2, velocity=80)
            elif beat == 1:
                note = Note(62, time, beat_duration * 0.2, velocity=80)
            elif beat == 2:
                note = Note(63, time, beat_duration * 0.2, velocity=80)
            elif beat == 3:
                note = Note(64, time, beat_duration * 0.2, velocity=80)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Eb7 (Eb, G, Bb, D)
# Bar 4: Cm7 (C, Eb, G, Bb)

piano_notes = []

for bar in range(2, 4):
    bar_start = bar * bar_duration
    if bar == 2:
        # Dm7
        # D (62) on 2
        note = Note(62, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # F (65) on 2
        note = Note(65, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # A (69) on 2
        note = Note(69, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # C (69) on 4
        note = Note(60, bar_start + 0.75, 0.125, velocity=80)
        piano.notes.append(note)
    elif bar == 3:
        # Eb7
        # Eb (61) on 2
        note = Note(61, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # G (67) on 2
        note = Note(67, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # Bb (62) on 2
        note = Note(62, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # D (67) on 4
        note = Note(67, bar_start + 0.75, 0.125, velocity=80)
        piano.notes.append(note)
    elif bar == 4:
        # Cm7
        # C (60) on 2
        note = Note(60, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # Eb (62) on 2
        note = Note(62, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # G (67) on 2
        note = Note(67, bar_start + 0.375, 0.125, velocity=80)
        piano.notes.append(note)
        # Bb (62) on 4
        note = Note(62, bar_start + 0.75, 0.125, velocity=80)
        piano.notes.append(note)

# Write MIDI file
midi.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' has been created.")
