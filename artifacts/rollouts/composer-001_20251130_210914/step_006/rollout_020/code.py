
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
    (1.5, 38, 100),  # Snare on 3
    (2.25, 42, 100), # Hihat on 4
    (3.0, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on 2
    (4.5, 38, 100),  # Snare on 3
    (5.25, 42, 100)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 63, 100), # F (root)
    (1.875, 62, 100), # Eb (chromatic approach)
    (2.25, 60, 100), # D (3rd)
    (2.625, 59, 100), # Db (chromatic approach)
    (3.0, 57, 100), # Bb (5th)
    (3.375, 56, 100), # A (chromatic approach)
    (3.75, 55, 100), # Ab (7th)
    (4.125, 57, 100), # Bb (chromatic approach)
    (4.5, 60, 100), # D (root)
    (4.875, 59, 100), # Db (chromatic approach)
    (5.25, 62, 100), # Eb (3rd)
    (5.625, 61, 100)  # Eb (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 64, 100), # F7: F, A, C, Eb
    (2.25, 69, 100),
    (2.25, 60, 100),
    (2.25, 62, 100),
    # Bar 3
    (3.75, 64, 100),
    (3.75, 69, 100),
    (3.75, 60, 100),
    (3.75, 62, 100),
    # Bar 4
    (5.25, 64, 100),
    (5.25, 69, 100),
    (5.25, 60, 100),
    (5.25, 62, 100)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (2.25, 38, 100), # Snare on 2
    (3.0, 42, 100),  # Hihat on 3
    (3.75, 38, 100), # Snare on 4
    (4.5, 36, 100),  # Kick on 1
    (5.25, 38, 100), # Snare on 2
    (6.0, 42, 100),  # Hihat on 3
    (6.75, 38, 100)  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax (Dante) - one short motif, make it sing
# Start of motif at 1.5s
sax_notes = [
    (1.5, 62, 100),  # F (root)
    (1.6875, 60, 100),  # D (3rd)
    (1.875, 59, 100),  # Db (chromatic)
    (2.0625, 62, 100),  # F (root)
    (2.25, 62, 100),  # F (root)
    (2.4375, 60, 100),  # D (3rd)
    (2.625, 59, 100),  # Db (chromatic)
    (2.8125, 62, 100)   # F (root)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
