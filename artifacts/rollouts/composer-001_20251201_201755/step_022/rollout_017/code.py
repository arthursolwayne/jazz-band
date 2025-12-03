
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
    (0.75, 42, 100), # Hihat on 2
    (1.0, 38, 100),  # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),  # D2
    (1.875, 40, 100), # Eb2 (chromatic approach)
    (2.25, 43, 100),  # G2
    (2.625, 41, 100), # F2 (chromatic approach)
    (3.0, 38, 100),   # D2
    (3.375, 40, 100), # Eb2
    (3.75, 43, 100),  # G2
    (4.125, 41, 100), # F2
    (4.5, 38, 100),   # D2
    (4.875, 40, 100), # Eb2
    (5.25, 43, 100),  # G2
    (5.625, 41, 100)  # F2
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    (1.5, 62, 100),  # D4
    (1.5, 67, 100),  # F#4
    (1.5, 71, 100),  # A4
    (1.5, 72, 100),  # C#5

    # Bar 3: Bm7b5 (B, D, F#, A)
    (2.25, 69, 100),  # B4
    (2.25, 62, 100),  # D4
    (2.25, 67, 100),  # F#4
    (2.25, 71, 100),  # A4

    # Bar 4: G7 (G, B, D, F)
    (3.0, 67, 100),   # G4
    (3.0, 71, 100),   # B4
    (3.0, 69, 100),   # D4
    (3.0, 65, 100),   # F4
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on 2
    (2.0, 38, 100),  # Snare on 3
    (2.25, 42, 100), # Hihat on 4
    (2.5, 36, 100),  # Kick on 1
    (2.75, 42, 100), # Hihat on 2
    (3.0, 38, 100),  # Snare on 3
    (3.25, 42, 100), # Hihat on 4
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on 2
    (4.0, 38, 100),  # Snare on 3
    (4.25, 42, 100), # Hihat on 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - D4 - B4 (D - F# - D - B)
sax_notes = [
    (1.5, 62, 100),  # D4
    (1.625, 67, 100), # F#4
    (1.75, 62, 100),  # D4
    (2.0, 69, 100),   # B4
    (2.25, 62, 100),  # D4 (return)
    (2.375, 67, 100), # F#4
    (2.5, 62, 100),   # D4
    (2.75, 69, 100)   # B4
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
