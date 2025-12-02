
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)        # Tenor sax
bass = pretty_midi.Instrument(program=33)       # Double bass
piano = pretty_midi.Instrument(program=0)       # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Time signature is 4/4

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time is in seconds, each bar is 1.5 seconds, 0.375 per beat

# Bass line: Marcus — walking line with chromatic approaches
bass_notes = [
    (2, 0.0),     # D (2)
    (3, 0.375),   # E (3)
    (1, 0.75),    # C (1)
    (2, 1.125),   # D (2)
    (4, 1.5),     # F# (4)
    (5, 1.875),   # G (5)
    (3, 2.25),    # E (3)
    (2, 2.625),   # D (2)
    (5, 3.0),     # G (5)
    (6, 3.375),   # A (6)
    (4, 3.75),    # F# (4)
    (5, 4.125),   # G (5)
    (7, 4.5),     # A# (7)
    (6, 4.875),   # A (6)
    (5, 5.25),    # G (5)
    (4, 5.625),   # F# (4)
]

for note, time in bass_notes:
    pitch = 48 + note  # C = 48, so D is 50
    note_obj = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Diane — 7th chords, comping on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C) on beat 2
    (62, 1.5), (67, 1.5), (71, 1.5), (64, 1.5),
    # Bar 3: G7 (G, B, D, F) on beat 4
    (67, 3.0), (71, 3.0), (62, 3.0), (65, 3.0),
    # Bar 4: C7 (C, E, G, B) on beat 2
    (64, 4.5), (69, 4.5), (71, 4.5), (74, 4.5),
]

for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.3)
    piano.notes.append(note_obj)

# Sax: You — a short motif, make it sing. Start it, leave it hanging. No scale runs.

# D (62), E (64), F# (67), D (62) — with a slight chromatic descent
sax_notes = [
    (62, 1.5),     # D
    (64, 1.625),   # E
    (67, 1.75),    # F#
    (62, 1.875),   # D
    (60, 2.0),     # C (chromatic descent)
    (62, 2.125),   # D again
    (60, 2.25),    # C
    (62, 2.375),   # D
    (64, 2.5),     # E
    (67, 2.625),   # F#
    (62, 2.75),    # D
    (60, 2.875),   # C
    (59, 3.0),     # B
    (60, 3.125),   # C
    (62, 3.25),    # D
    (64, 3.375),   # E
    (67, 3.5),     # F#
    (62, 3.625),   # D
    (60, 3.75),    # C
    (59, 3.875),   # B
    (62, 4.0),     # D
]

for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
