
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
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100),  # Hihat on 2
    (0.75, 36, 100),  # Kick on 3
    (1.125, 42, 100),  # Hihat on 4
    (1.125, 38, 100),  # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 62, 100),  # D2 (root)
    (1.875, 65, 100),  # F2 (fifth) with chromatic approach
    (2.25, 62, 100),  # D2
    (2.625, 60, 100),  # C2 (chromatic)
    # Bar 3
    (3.0, 65, 100),  # F2
    (3.375, 67, 100),  # G2
    (3.75, 65, 100),  # F2
    (4.125, 64, 100),  # E2
    # Bar 4
    (4.5, 62, 100),  # D2
    (4.875, 65, 100),  # F2
    (5.25, 62, 100),  # D2
    (5.625, 60, 100),  # C2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: Diane, open voicings, resolve on the last chord
# Bar 2: Dm7
piano_notes = [
    # Bar 2
    (1.5, 62, 100),  # D
    (1.5, 67, 100),  # G
    (1.5, 70, 100),  # C
    (1.5, 72, 100),  # D
    # Bar 3
    (3.0, 64, 100),  # F
    (3.0, 69, 100),  # A
    (3.0, 72, 100),  # C
    (3.0, 74, 100),  # D
    # Bar 4
    (4.5, 62, 100),  # D
    (4.5, 67, 100),  # G
    (4.5, 70, 100),  # C
    (4.5, 72, 100),  # D
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, start, start + 0.125))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(100, 42, start + 0.375, start + 0.45))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(100, 36, start + 0.75, start + 0.875))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(100, 42, start + 1.125, start + 1.2))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(100, 38, start + 1.125, start + 1.2))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - motif start
    (1.5, 67, 100),  # G4
    (1.75, 69, 100),  # A4
    (2.0, 67, 100),  # G4
    (2.25, 62, 100),  # D4
    # Bar 3 - leave it hanging
    (3.0, 62, 100),  # D4
    (3.25, 62, 100),  # D4
    (3.5, 62, 100),  # D4
    (3.75, 62, 100),  # D4
    # Bar 4 - return, finish the motif
    (4.5, 67, 100),  # G4
    (4.75, 69, 100),  # A4
    (5.0, 67, 100),  # G4
    (5.25, 62, 100),  # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
