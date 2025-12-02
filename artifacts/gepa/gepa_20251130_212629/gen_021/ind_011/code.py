
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds (160 BPM = 6/160 = 0.0375 sec per beat, 1 bar = 1.5 sec)
beat_time = 0.375  # 160 BPM = 60 / 160 = 0.375 seconds per beat

# Create instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS)
piano = Instrument(program=Program.PIANO)
sax = Instrument(program=Program.SAXOPHONE)

pm.instruments = [drums, bass, piano, sax]

# DRUMS (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
def add_drums():
    for bar in range(4):
        for beat in range(4):
            time = bar * 1.5 + beat * 0.375
            # Kick on 1 and 3
            if beat == 0 or beat == 2:
                note = Note(36, time, time + 0.125, velocity=100)
                drums.notes.append(note)
            # Snare on 2 and 4 (beat 1 and 3)
            if beat == 1 or beat == 3:
                note = Note(38, time, time + 0.125, velocity=100)
                drums.notes.append(note)
            # Hihat on every 8th note
            if beat % 2 == 0:
                note = Note(42, time, time + 0.125, velocity=90)
                drums.notes.append(note)
            else:
                note = Note(42, time, time + 0.125, velocity=60)
                drums.notes.append(note)

# BASS (Marcus)
# Walking line in Dm, with chromatic approaches
def add_bass():
    # Dm7: D, F, A, C
    # Walking line with chromatic approach to each chord tone
    notes = [
        # Bar 1: Dm -> D, F, A, C
        Note(62, 0, 0.375, 100),
        Note(65, 0.375, 0.75, 100),
        Note(67, 0.75, 1.125, 100),
        Note(64, 1.125, 1.5, 100),

        # Bar 2: Bb7 -> Bb, D, F, Ab
        Note(59, 1.5, 1.875, 100),
        Note(62, 1.875, 2.25, 100),
        Note(65, 2.25, 2.625, 100),
        Note(61, 2.625, 3.0, 100),

        # Bar 3: G7 -> G, B, D, F
        Note(67, 3.0, 3.375, 100),
        Note(71, 3.375, 3.75, 100),
        Note(69, 3.75, 4.125, 100),
        Note(67, 4.125, 4.5, 100),

        # Bar 4: C7 -> C, E, G, Bb
        Note(60, 4.5, 4.875, 100),
        Note(64, 4.875, 5.25, 100),
        Note(67, 5.25, 5.625, 100),
        Note(62, 5.625, 6.0, 100)
    ]
    for note in notes:
        bass.notes.append(note)

# PIANO (Diane)
# 7th chords, comp on 2 and 4
def add_piano():
    # Dm7 = D, F, A, C
    # Bb7 = Bb, D, F, Ab
    # G7 = G, B, D, F
    # C7 = C, E, G, Bb

    # Bar 1: Dm7 on 2 and 4
    chord_notes = [62, 65, 67, 64]
    for beat in [1, 3]:
        time = beat * 0.375
        for note in chord_notes:
            piano.notes.append(Note(note, time, time + 0.125, 90))

    # Bar 2: Bb7 on 2 and 4
    chord_notes = [59, 62, 65, 61]
    for beat in [1, 3]:
        time = 1.5 + beat * 0.375
        for note in chord_notes:
            piano.notes.append(Note(note, time, time + 0.125, 90))

    # Bar 3: G7 on 2 and 4
    chord_notes = [67, 71, 69, 67]
    for beat in [1, 3]:
        time = 3.0 + beat * 0.375
        for note in chord_notes:
            piano.notes.append(Note(note, time, time + 0.125, 90))

    # Bar 4: C7 on 2 and 4
    chord_notes = [60, 64, 67, 62]
    for beat in [1, 3]:
        time = 4.5 + beat * 0.375
        for note in chord_notes:
            piano.notes.append(Note(note, time, time + 0.125, 90))

# SAX (Dante)
# Motif: D, F, A, D (octave up), F, A, Bb
# Start it, leave it hanging, return and finish it
def add_sax():
    # Bar 1: D F A D
    notes = [
        Note(62, 0, 0.375, 110),
        Note(65, 0.375, 0.75, 110),
        Note(67, 0.75, 1.125, 110),
        Note(69, 1.125, 1.5, 110)
    ]
    for note in notes:
        sax.notes.append(note)

    # Bar 2: F A Bb
    # Omit the D to create tension
    notes = [
        Note(65, 1.5, 1.875, 110),
        Note(67, 1.875, 2.25, 110),
        Note(62, 2.25, 2.625, 110)
    ]
    for note in notes:
        sax.notes.append(note)

    # Bar 3: D F A D
    # Return to the original motif
    notes = [
        Note(62, 3.0, 3.375, 110),
        Note(65, 3.375, 3.75, 110),
        Note(67, 3.75, 4.125, 110),
        Note(69, 4.125, 4.5, 110)
    ]
    for note in notes:
        sax.notes.append(note)

    # Bar 4: F A Bb — leave it open, end with tension
    notes = [
        Note(65, 4.5, 4.875, 110),
        Note(67, 4.875, 5.25, 110),
        Note(62, 5.25, 5.625, 110)
    ]
    for note in notes:
        sax.notes.append(note)

# Add all parts
add_drums()
add_bass()
add_piano()
add_sax()

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file generated: 'dante_intro.mid'")
