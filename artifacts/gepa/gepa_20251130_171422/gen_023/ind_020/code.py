
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),   # Kick on 1
    (0.75, 42, 90),   # Hihat on 2
    (1.0, 38, 110),   # Snare on 3
    (1.5, 42, 90)     # Hihat on 4
]
for time, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Bass line - Marcus: walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0)
    (1.5, 50, 80),    # D
    (1.75, 49, 85),   # C# (chromatic approach)
    (2.0, 48, 80),    # C
    (2.25, 47, 85),   # B
    (2.5, 50, 80),    # D
    (2.75, 51, 85),   # E
    (3.0, 52, 80),    # F

    # Bar 3 (3.0 - 4.5)
    (3.0, 52, 80),    # F
    (3.25, 53, 85),   # F#
    (3.5, 54, 80),    # G
    (3.75, 55, 85),   # G#
    (4.0, 52, 80),    # F
    (4.25, 51, 85),   # E
    (4.5, 50, 80),    # D

    # Bar 4 (4.5 - 6.0)
    (4.5, 50, 80),    # D
    (4.75, 49, 85),   # C#
    (5.0, 52, 80),    # F
    (5.25, 53, 85),   # F#
    (5.5, 55, 80),    # G#
    (5.75, 57, 85),   # A#
    (6.0, 55, 80)     # G#
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    (1.75, 62, 80),   # D7: F# (3rd)
    (1.75, 67, 80),   # D7: A (7th)
    (2.25, 62, 80),   # D7: F#
    (2.25, 67, 80),   # D7: A

    # Bar 3 (3.0 - 4.5)
    (3.25, 62, 80),   # D7: F#
    (3.25, 67, 80),   # D7: A
    (3.75, 62, 80),   # D7: F#
    (3.75, 67, 80),   # D7: A

    # Bar 4 (4.5 - 6.0)
    (4.75, 62, 80),   # D7: F#
    (4.75, 67, 80),   # D7: A
    (5.25, 62, 80),   # D7: F#
    (5.25, 67, 80),   # D7: A
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax - Dante: sparse, expressive, searching
sax_notes = [
    # Bar 2 (1.5 - 3.0)
    (1.5, 62, 90),    # D (start of motif)
    (1.75, 65, 95),   # F (rising)
    (2.0, 62, 85),    # D (return)

    # Bar 3 (3.0 - 4.5)
    (3.0, 67, 100),   # A (response)
    (3.25, 65, 95),   # F
    (3.5, 64, 90),    # E
    (3.75, 62, 85),   # D

    # Bar 4 (4.5 - 6.0)
    (4.5, 67, 100),   # A (resolution)
    (4.75, 65, 95),   # F
    (5.0, 62, 85),    # D
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums continue in bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0)
    (1.5, 36, 100),   # Kick on 1
    (2.0, 38, 110),   # Snare on 3
    (2.25, 42, 90),   # Hihat on 4
    (2.5, 42, 90),    # Hihat on 1 of next bar
    (3.0, 36, 100),   # Kick on 1
    (3.25, 42, 90),   # Hihat on 2
    (3.5, 38, 110),   # Snare on 3
    (3.75, 42, 90),   # Hihat on 4

    # Bar 3 (3.0 - 4.5)
    (4.0, 36, 100),   # Kick on 1
    (4.25, 42, 90),   # Hihat on 2
    (4.5, 38, 110),   # Snare on 3
    (4.75, 42, 90),   # Hihat on 4

    # Bar 4 (4.5 - 6.0)
    (5.0, 36, 100),   # Kick on 1
    (5.25, 42, 90),   # Hihat on 2
    (5.5, 38, 110),   # Snare on 3
    (5.75, 42, 90)    # Hihat on 4
]
for time, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
